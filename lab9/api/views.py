from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    # ВАЖНО: queryset должен быть здесь, в самом начале класса!
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    
    # Настройки поиска и сортировки
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'price']

    def get_queryset(self):
        # Берем базовый набор данных
        queryset = Product.objects.all()
        
        # Фильтрация по категории ?category=1
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            
        # Фильтрация по статусу ?is_active=true
        is_active = self.request.query_params.get('is_active')
        if is_active:
            val = is_active.lower() == 'true'
            queryset = queryset.filter(is_active=val)
            
        return queryset

    @action(detail=False, methods=['get'])
    def active(self, request):
        products = Product.objects.filter(is_active=True)
        filtered_products = self.filter_queryset(products)
        serializer = self.get_serializer(filtered_products, many=True)
        return Response(serializer.data)