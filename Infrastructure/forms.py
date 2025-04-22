from django import forms
from .models import Category, Brand

# فرم دسته‌بندی


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'نام دسته‌بندی',
            'description': 'توضیحات دسته‌بندی',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام دسته‌بندی را وارد کنید'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'توضیحات را وارد کنید'}),
        }

# فرم برند


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'image']
        labels = {
            'name': 'نام برند',
            'description': 'توضیحات برند',
            'image': 'تصویر برند',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام برند را وارد کنید'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'توضیحات را وارد کنید'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
