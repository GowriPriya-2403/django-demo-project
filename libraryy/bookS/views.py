from django.shortcuts import render,redirect
from bookS.models import Book
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
@login_required
def addbooks(request):
    if(request.method=="POST"):
       t=request.POST['t']
       a=request.POST['a']
       l=request.POST['l']
       p=request.POST['p']
       pa=request.POST['pa']
       c=request.FILES.get('c')
       pd=request.FILES.get('pd')
       b=Book.objects.create(title=t,author=a,language=l,price=p,pages=pa,cover=c,pdf=pd)
       b.save()
    return render(request,'add.html')

@login_required
def viewbooks(request):
    k=Book.objects.all()  #select*from Book reads all records from table Book
    context={'book':k}    #passes data from views to html file.context is dictionary type
    return render(request,'view.html',context)
def detail(request,p):
    b=Book.objects.get(id=p)   #reads a particular record from table
    context={'book':b}
    return render(request,'detail.html',context)


def edit(request,p):
    b=Book.objects.get(id=p)
    if (request.method == "POST"):
     b.title = request.POST['t']
     b.author= request.POST['a']
     b.language = request.POST['l']
     b.price = request.POST['p']
     b.pages = request.POST['pa']
    if (request.FILES.get('c')==None):
        b.save()  # save the record inside the table
    else:
        b.cover = request.FILES.get('c')

    if (request.FILES.get('pd')==None):
        b.save()
    else:
        b.pdf = request.FILES.get('pd')
    b.save()

    # return redirect('books:view')
    context = {'book': b}
    return render(request,'edit.html',context)

def delete(request,p):
     b = Book.objects.get(id=p)
     b.delete()
     return redirect('books:view')

from django.db.models import Q
def searchbooks(request):
    b=None
    query=""
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            b=Book.objects.filter(Q(title__icontains=query)   |  Q(author__icontains=query))

    return render(request,'search.html',{'book':b,'query':query})