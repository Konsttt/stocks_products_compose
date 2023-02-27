from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer, StockDetailSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    serializer_class = ProductSerializer


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().prefetch_related('products')  # + prefetch_related для связи m2m
    serializer_class = StockSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]

    # Чтобы добраться до полей связанной сущности foreignkey или m2m, используется двойное подчеркивание "__"
    # 'poducts__title', где products - название поля m2m, title - поле связанной через m2m таблицы.
    # Поиск по части слова.(Search работает только по CharField и TextField)
    search_fields = ['address', 'products__title']

    # products - это название m2m поля из Stock.
    # Фильтр - строгое соответствие слову в запросе.
    filterset_fields = ['products', 'address']

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return StockDetailSerializer  # depth=1 - (для вложенного вывода). Только GET.
        else:
            return StockSerializer  # depth=0. Для POST, PUT, PATCH


