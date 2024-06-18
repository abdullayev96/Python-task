from django.shortcuts import render, redirect
from .models import *
from .forms import CategoryForm, ShopForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse



def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')



@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')



@login_required_decorator
def home_page(request):
    return render(request, "index.html")




@login_required_decorator
def shop_create(request):
    if request.user.is_staff:
        model = Shop()
        form = ShopForm(request.POST or None, request.FILES, instance=model)
        if request.POST and form.is_valid():
            form.save()
            return redirect('shop_list')

        ctx = {
            'model': model,
            'form': form,
        }
        return render(request, "shop/form.html", ctx)

    else:
        return HttpResponse("Unauthorized", status=401)




@login_required_decorator
def shop_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        shops = Shop.objects.filter(Q(title__icontains=q))
    else:
        shops = Shop.objects.all().order_by('-id')
        q = None

    return render(request, 'shop/list.html', {"shops": shops, "q": q})



@login_required_decorator
def shop_edit(request, pk):
    if request.user.is_staff:
       model = Shop.objects.get(pk=pk)
       form = ShopForm(request.POST or None,request.FILES or None, instance=model)
       if request.POST and form.is_valid():
            form.save()
            return redirect("shop_list")
       ctx = {
        "model": model,
        "form": form
       }
       return render(request, "shop/form.html", ctx)

    else:
        return HttpResponse("Unauthorized", status=401)


@login_required_decorator
def shop_delete(request, pk):
    if request.user.is_staff:
        model = Shop.objects.get(pk=pk)
        model.delete()
        return redirect("shop_list")

    else:
        return HttpResponse("Unauthorized", status=401)




@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "category/form.html", ctx)

@login_required_decorator
def category_list(request):
    if 'q' in request.GET:
        q = request.GET['q']

        categories = Category.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    else:
        categories = Category.objects.all().order_by('-id')
        q = None

    ctx = {
        "categories": categories,
        'q':q
    }

    return render(request, 'category/list.html', ctx)




@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "category/form.html", ctx)


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect("category_list")


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None,request.FILES or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "product/form.html", ctx)

@login_required_decorator
def product_list(request):
    if 'q' in request.GET:
        q = request.GET['q']

        products = Product.objects.filter(Q(id__icontains=q) | Q(title__icontains=q))
    else:
        products = Product.objects.all().order_by('-id')
        q = None

    ctx = {
        "products": products,
        'q':q
    }
    return render(request, "product/list.html", ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None,request.FILES or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("product_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "product/form.html", ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect("product_list")