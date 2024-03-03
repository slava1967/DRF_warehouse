from rest_framework import serializers, validators

from api.models import ApiUser, Warehouse, Product, Order


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    email = serializers.EmailField()
    position = serializers.ChoiceField(choices=ApiUser.POSITION)
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            position=validated_data["position"],
        )
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])

        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        current_user = validated_data.get("user")
        # current_warehouse = validated_data.get("warehouse.name")
        if current_user.position == "SU":
            product = Product.objects.create(
                name=validated_data["name"],
                quantity=validated_data["quantity"],
                warehouse=validated_data["warehouse"],
                user=validated_data["user"]
            )
            product.save()
            return product
        else:
            raise serializers.ValidationError("Customers are not authorized to create products")


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


product_quantity = Product.objects.only("quantity")[0].quantity


def validate_quantity(value):
    if int(value) < 1:
        raise serializers.ValidationError('Minimum quantity is 1')
    if int(value) > product_quantity:
        raise serializers.ValidationError(
            f'Maximum quantity available is {product_quantity}')
    return value


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantity = serializers.IntegerField(validators=[validate_quantity])

    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        current_user = validated_data.get("user")
        # current_warehouse = validated_data.get("product.warehouse")
        if current_user.position == "CO":
            order = Order.objects.create(
                product=validated_data["product"],
                quantity=validated_data["quantity"],
                # warehouse=current_warehouse,
                user=validated_data["user"]
            )
            order.save()
            return order
        else:
            raise serializers.ValidationError("Suppliers are not authorized to create orders")
