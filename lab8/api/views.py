from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Category, Product

def product_list(request):
    products = Product.objects.all()

    category_id = request.GET.get('category')
    active = request.GET.get('active')
    search = request.GET.get('search')

    if category_id:
        products = products.filter(category_id=category_id)

    if active: #тру фолс
        is_active = active.lower() == 'true'
        products = products.filter(is_active=is_active)

    if search:
        products = products.filter(name__icontains=search)
    return JsonResponse([p.to_json() for p in products], safe=False)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()
    return JsonResponse([c.to_json() for c in categories], safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category.to_json())
    except Category.DoesNotExist:
        return JsonResponse({'not found'}, status=404)

def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
        products = category.products.all()
        return JsonResponse([p.to_json() for p in products], safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'not found'}, status=404)