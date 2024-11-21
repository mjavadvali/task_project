from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", 
                  "description", "available", 
                  "price", "image"]

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
       
    #     self.fields['title'].widget.attrs.update({
    #             'placeholder': kwargs['instance'].title
    #         })

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"