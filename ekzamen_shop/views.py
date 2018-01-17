from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserSerializers,
    ExampleSerializers,
    ProductSerializers,
    CategorySerializers,
    BasketSerializers
)
from .models import User, Products, Category, ExampleBasket, Basket


class CategoryView(GenericViewSet,
                   mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class ProductView(GenericViewSet,
                  mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializers
    queryset = Products.objects.all()


class BasketView(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializers

    def get_queryset(self):
        username = self.request.user
        if username is not None:
            queryset = Basket.objects.filter(user_id=username)
            return queryset
        else:
            queryset = Basket.objects.all()
            return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserView(GenericViewSet,
               mixins.CreateModelMixin):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class ExampleView(GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExampleSerializers
    queryset = ExampleBasket.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
