from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib.auth import authenticate
from cart.forms import CartAddProductForm
from unicodedata import name
from django.shortcuts import render, redirect
from .models import User, CRUD
from .forms import UserComment, UserForm, CRUDCreate
from django.shortcuts import get_object_or_404
from .models import Category, Product
# Create your views here.



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    print(request.POST)
    error = ''
    if request.method == 'POST':
        form = UserComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            #redirect('home')    --- после логина на хоум, а пока не надо
        else:
            error = 'Форма была невеноой'

    form = UserComment()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/contacts.html', context)


def register(request):
    print(request.POST, "REGISTER")
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #redirect('home')    --- после логина на хоум, а пока не надо
        else:
            error = 'Форма была невеноой'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/register.html')


def login(request):
    print(request.POST)
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                alert = True
                return render(request, "main/register.html", {"alert": alert})
    return render(request, "main/register.html")

#def logout(request):


















#CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---CRUD---


def crudindex(request):
    shelf = CRUD.objects.all()
    return render(request, 'main/comments.html', {'shelf': shelf})


def crud_upload(request):
    upload = CRUDCreate()
    if request.method == 'POST':
        upload = CRUDCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('main:comment')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'main:comment'}}">reload</a>""")


    else:
        return render(request, 'main/upload_form.html', {'upload_form': upload})


def crud_update(request, crud_id):
    crud_id = int(crud_id)
    try:
        crud_sel = CRUD.objects.get(id=crud_id)
    except CRUD.DoesNotExist:
        return redirect('main:comment')
    crud_form = CRUDCreate(request.POST or None, instance=crud_sel)
    if crud_form.is_valid():
       crud_form.save()
       return redirect('main:comment')
    return render(request, 'main/upload_form.html', {'upload_form': crud_form})


def crud_delete(request, crud_id):
    crud_id = int(crud_id)
    try:
        crud_sel = CRUD.objects.get(id=crud_id)
    except CRUD.DoesNotExist:
        return redirect('main:comment')
    crud_sel.delete()
    return redirect('main:comment')
