from rest_framework import serializers
from .models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     goods_front_image = serializers.ImageField()
#     click_num = serializers.IntegerField(default=0)
#
#     def create(self, validated_data):
#         return Goods.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
        # fields = ('name', 'click_num', 'market_price', 'add_time')
