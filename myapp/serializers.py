#Serializers 會將 Django 的模型數據轉換為 JSON 格式，方便通過 API 提供給 App 使用。
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['serial_number', 'product_name', 'arrival_date', 'quantity']  # 定義需要序列化的字段

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # 定義需要序列化的使用者字段