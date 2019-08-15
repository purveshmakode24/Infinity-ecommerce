from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category, Cart
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .forms import AddToCartForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    men_products = Product.objects.filter(category=1)
    women_products = Product.objects.filter(category=2)
    all_accessories = Product.objects.filter(category=3)
    acc_bags = Product.objects.filter(subcategory='bag')
    acc_shoes = Product.objects.filter(subcategory='shoes')
    acc_watches = Product.objects.filter(subcategory='watches')
    try:
        user = User.objects.get(username=request.user)
        current_user_cart_entries_count = user.current_user_cart.all().count()
        context = {
            'category': category,
            'all_products': all_products,
            'men_products': men_products,
            'women_products': women_products,
            'all_accessories': all_accessories,
            'acc_bags': acc_bags,
            'acc_shoes': acc_shoes,
            'acc_watches': acc_watches,
            # 'custom_cat_slug': custom_cat_slug,
            'current_user_cart_entries_count': current_user_cart_entries_count,
        }
        return render(request, 'index.html', context)
    except User.DoesNotExist:
        user = None

        context = {
            'category': category,
            'all_products': all_products,
            'men_products': men_products,
            'women_products': women_products,
            'all_accessories': all_accessories,
            'acc_bags': acc_bags,
            'acc_shoes': acc_shoes,
            'acc_watches': acc_watches,
            # 'custom_cat_slug': custom_cat_slug,
        }
        return render(request, 'index.html', context)


def products(request):
    all_products = Product.objects.all()
    men_products = Product.objects.filter(category=1)
    women_products = Product.objects.filter(category=2)
    all_accessories = Product.objects.filter(category=3)
    acc_bags = Product.objects.filter(subcategory='bag')
    acc_shoes = Product.objects.filter(subcategory='shoes')
    acc_watches = Product.objects.filter(subcategory='watches')
    try:
        user = User.objects.get(username=request.user)
        current_user_cart_entries_count = user.current_user_cart.all().count()
        context = {
            'all_products': all_products,
            'men_products': men_products,
            'women_products': women_products,
            'all_accessories': all_accessories,
            'acc_bags': acc_bags,
            'acc_shoes': acc_shoes,
            'acc_watches': acc_watches,
            'current_user_cart_entries_count': current_user_cart_entries_count,
        }
        return render(request, 'product.html', context)
    except User.DoesNotExist:
        user = None

        context = {
            'all_products': all_products,
            'men_products': men_products,
            'women_products': women_products,
            'all_accessories': all_accessories,
            'acc_bags': acc_bags,
            'acc_shoes': acc_shoes,
            'acc_watches': acc_watches,
        }
        return render(request, 'product.html', context)


def products_cat(request, cat_id, c_slug):
    # category_men = Category.objects.filter(id=1)
    # category_women = Category.objects.filter(id=2)
    # category_acc = Category.objects.filter(id=3)
    # all_products = Product.objects.all()

    # women_products = Product.objects.filter(category=2)
    # all_accessories = Product.objects.filter(category=3)

    # acc_bags = Product.objects.filter(subcategory='bag')
    # acc_shoes = Product.objects.filter(subcategory='shoes')
    # acc_watches = Product.objects.filter(subcategory='watches')

    # cat_id =1 for men, cat_id=2 women, cat_id=3 for Accessories
    # category = Category.objects.all()
    # for x in category:
    #     modal_cat_id = x.id
    #     modal_cat_slug = x.slug
    #
    # if modal_cat_id == cat_id and modal_cat_slug == slug:
    #     print(modal_cat_id)
    current_cat_products = Product.objects.filter(category_id=cat_id)
    try:
        user = User.objects.get(username=request.user)
        current_user_cart_entries_count = user.current_user_cart.all().count()
        context = {
            'current_cat_products': current_cat_products,
            'slug': c_slug,
            'cat_id': cat_id,
            'current_user_cart_entries_count': current_user_cart_entries_count,
        }
        return render(request, 'product-category.html', context)
    except User.DoesNotExist:
        user = None
        # else:
        #     return HttpResponse("Error:404")
        # if cat_id == 1:
        #     context = {
        #         'current_cat_products': current_cat_products,
        #         'slug': slug,
        #         'cat_id': cat_id,
        #     }
        #
        # elif cat_id == 2:
        #     context = {
        #         'current_cat_products': current_cat_products,
        #         'slug': slug,
        #         'cat_id': cat_id,
        #     }
        # else:
        #     context = {
        #         'current_cat_products': current_cat_products,
        #         'slug': slug,
        #         'cat_id': cat_id,
        #     }
        context = {
            'current_cat_products': current_cat_products,
            'slug': c_slug,
            'cat_id': cat_id,
        }
        return render(request, 'product-category.html', context)


def product_overview(request, cat_id, c_slug, p_id, p_slug):
    current_product_overview = Product.objects.filter(id=p_id)
    add_to_cart_form = AddToCartForm()
    try:
        user = User.objects.get(username=request.user)
        current_user_cart_entries_count = user.current_user_cart.all().count()
        context = {
            'current_product_overview': current_product_overview,
            'current_product_slug': p_slug,
            'product_id': p_id,
            'cat_id': cat_id,
            'c_slug': c_slug,
            'current_user_cart_entries_count': current_user_cart_entries_count,
            'form': add_to_cart_form,
        }
        return render(request, 'overview.html', context)
    except User.DoesNotExist:

        context = {
            'current_product_overview': current_product_overview,
            'current_product_slug': p_slug,
            'product_id': p_id,
            'cat_id': cat_id,
            'c_slug': c_slug,
            'form': add_to_cart_form,
        }
        return render(request, 'overview.html', context)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_detail(request):
    return render(request, 'blog-detail.html', {})


def cart(request):
    user = User.objects.get(username=request.user)
    current_user_cart_entries = user.current_user_cart.all()
    current_user_cart_entries_count = user.current_user_cart.all().count()
    for item in current_user_cart_entries:
        item_count = item.count
        entry_price = item.entry_price
        context = {
            'current_user_cart_entries': current_user_cart_entries,
            'current_user_cart_entries_count': current_user_cart_entries_count,
            'item_count': item_count,
            'entry_price': entry_price,
        }
        return render(request, 'shoping-cart.html', context)


@login_required
def add_to_cart(request, user_id, p_id):
    # if request.method == 'POST':
    #     req_product_size = request.POST.get('size')
    #     req_product_color = request.POST.get('color')
    #     quantity_of_items = request.POST.get('num-product')
    #     try:
    #         form = Cart(user_id=user_id, product_id=p_id, size=req_product_size, color=req_product_color,
    #                     count=quantity_of_items)
    #         form.save()
    #         messages.success(request, f'Post has been Successfully Added!')
    #     except Exception as e:
    #         print(e)
    # else:
    #     # return render(request, '404.html')
    #     # return redirect('error_404')
    #     return HttpResponse('Error:404')
    # return redirect('infinity_home')
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['count']
            size = form.cleaned_data['size']
            color = form.cleaned_data['color']
            price = request.POST.get('price')
            entry_price = float(price) * int(count)
            print(entry_price)
            add_to_c_form = Cart(user_id=user_id, product_id=p_id, size=size, color=color,
                                 count=count, price=price, entry_price=entry_price)
            # messages.success(request, f'Post has been Successfully Added!')
            add_to_c_form.save()
            return redirect('infinity_home')
    else:
        return HttpResponse("error:404")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account for {username} has been created Successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
