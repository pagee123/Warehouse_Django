from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    captcha = CaptchaField()  # 加入驗證碼
    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='名子', max_length=100, required=True)
    last_name = forms.CharField(label='姓氏', max_length=100, required=True)
    email = forms.EmailField(label='信箱', required=True)
    username = forms.CharField(label='帳號', max_length=150, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        # 先使用父類的 save 方法來保存用戶名和密碼
        user = super(SignUpForm, self).save(commit=False)
        # 將 email 添加到用戶對象
        user.email = self.cleaned_data['email']
        if commit:
            user.save()  # 保存用戶對象到資料庫
        return user
    
    # 用於新增或更新貨品的表單
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['serial_number','product_name', 'arrival_date', 'quantity']  # 表單顯示的欄位