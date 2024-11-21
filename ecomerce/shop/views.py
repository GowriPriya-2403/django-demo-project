from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from shop.models import Category,Product


def home(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'home.html',context)

def product(request,i):
    c=Category.objects.get(id=i)
    p=Product.objects.filter(Category=c)
    context={'cat':c,'pro':p}
    return render(request,'product.html',context)

def productdetails(request,i):
    p=Product.objects.get(id=i)
    context={'pro':p}
    return render(request,'detail.html',context)

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
        else:
            return HttpResponse("password not same")
            return redirect('shop:home')

    return render(request,'register.html')



def u_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']

        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            return HttpResponse("invalid credentials")

    return render(request,'login.html')
@login_required
def u_logout(request):
    logout(request)
    return redirect('shop:u_login')

def addcategories(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES.get('i')
        d=request.POST['d']
        c = Category.objects.create(name=n, image=i,desc=d)
        c.save()

    return render(request,'addcategories.html')

def addproduct(request):
    if(request.method == "POST"):
       n=request.POST.get('n')
       d=request.POST.get('d')
       s=request.POST.get('s')
       t=request.POST.get('t')
       i=request.FILES.get('i')
       c=request.POST.get('c')
       cat=Category.objects.get(name=c)   # retrive a category rec matching with that name
       p=Product.objects.create(name=n,desc=d,price=s,stock=t,image=i,Category=cat)
       p.save()
    return render(request,'addproduct.html')

def addstock(request,i):
    p=Product.objects.get(id=i)
    if (request.method == "POST"):
        p.stock=request.POST['t']
        p.save()
        return redirect('shop:detail',i)
    context={'pro':p}
    return render(request, 'addstock.html',context)



