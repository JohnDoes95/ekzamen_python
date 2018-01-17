from rest_framework import serializers
from .models import User, Category, Products, ExampleBasket, Basket


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ()


class BasketSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Basket
        exclude = ()
        fields = ('user', 'elements', 'status',)

    def create(self, validated_data):
        user = validated_data['user']
        elements = validated_data['elements']
        status = validated_data['status']
        basket = Basket(
            user=user,
            elements=elements,
            status=status,
        )
        basket.save()
        return basket


class ExampleSerializers(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=6)

    class Meta:
        model = ExampleBasket
        exclude = ()
        fields = ('owner', 'quantity', 'product', 'price',)

    def create(self, validated_data):
        owner = validated_data['owner']
        quantity = validated_data['quantity']
        product = validated_data['product']
        cost = Products.objects.get(name=product)
        example = ExampleBasket(
            owner=owner,
            quantity=quantity,
            product=product,
            price=cost.price * quantity,
        )
        example.save()
        return example


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
