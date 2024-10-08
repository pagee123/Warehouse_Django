from django.contrib import admin

# Register your models here.
from .models import Product

# 註冊 Product 模型到 admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'product_name', 'arrival_date', 'quantity')  # 顯示欄位
    search_fields = ('product_name',)  # 可以用貨品名稱進行搜尋
    list_filter = ('arrival_date',)  # 允許根據進貨日期過濾