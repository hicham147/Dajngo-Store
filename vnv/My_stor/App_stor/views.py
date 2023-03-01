from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator,EmptyPage
# how you want ot add in the one page

# get the number of the page you ask for in non put 1

# this is action

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        products_count = products.count()

    else:
        products = Product.objects.filter(available=True)
        products_count = products.count()
        
    p = Paginator(products,6)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request,'store/store.html',
                                {'category': category,
                                'categories': categories,
                                'products': page,
                                "products_count":products_count})
    
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()

    return render(request,'store/product-detail.html',{'product': product,'cart_product_form': cart_product_form})
