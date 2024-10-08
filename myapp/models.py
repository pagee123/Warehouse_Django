from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # 使用內建的User模型

# Create your models here.

class Product(models.Model):
    serial_number = models.AutoField(primary_key=True)  # 流水號，會自動遞增
    product_name = models.CharField(max_length=100)  # 貨品名稱
    arrival_date = models.DateField(default=timezone.now)  # 進貨日期，預設為當前日期
    quantity = models.PositiveIntegerField()  # 貨品數量，必須為正整數

    def __str__(self):
        return self.product_name
    
    # 增加存入和取出的簡單方法
    def add_quantity(self, amount):
        self.quantity += amount
        self.save()

    def remove_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            self.save()
            return True
        else:
            return False  # 如果數量不足以取出，返回 False
        
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # 動作描述
    timestamp = models.DateTimeField(auto_now_add=True)  # 記錄時間

    def __str__(self):
        return f"{self.user.username} 在 {self.timestamp.strftime('%Y-%m-%d %H:%M')} : {self.action}"