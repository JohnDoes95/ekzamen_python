from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserView, CategoryView, ProductView, ExampleView, BasketView

router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'category', CategoryView)
router.register(r'products', ProductView)
router.register(r'example', ExampleView)
router.register(r'baskets', BasketView, base_name='basket')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]