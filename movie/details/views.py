from django.shortcuts import render,redirect
from details.models import Movie

def home(request):
    k = Movie.objects.all()  # select*from Book reads all records from table Book
    context = {'movie': k}
    return render(request,'home.html',context)

def add(request):
    if (request.method == "POST"):
        t = request.POST['t']
        d = request.POST['d']
        l = request.POST['l']
        y = request.POST['y']
        p = request.FILES['p']
        m =Movie.objects.create(title=t, description=d, language=l, year=y,poster=p)  # create new record
        m.save()  # save the record inside the table
        return redirect('home')
    return render(request,'add.html')

def booking(request):
    return render(request,'booking.html')

def detail(request,p):
    m=Movie.objects.get(id=p)
    context={'movie':m}
    return render(request,'detail.html',context)

def delete(request,p):
    m= Movie.objects.get(id=p)
    m.delete()
    return redirect('home')
def update(request,p):
    m=Movie.objects.get(id=p)
    if (request.method == "POST"):
        m.title=request.POST['t']
        m.description=request.POST['d']
        m.year=request.POST['y']
        m.language = request.POST['l']
        if (request.FILES.get('p') == None):
            m.save()
        else:
            m.poster = request.FILES.get('p')
            m.save()
        return redirect('home')
    context={'movie':m}
    return render(request,'edit.html',context)


