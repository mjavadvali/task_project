from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", 
                  "description", 
                  "price","stock", "image"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['category'].required = True
        self.fields['description'].required = True
        self.fields['image'].required = True
        self.fields['stock'].required = True




    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
       
    #     self.fields['title'].widget.attrs.update({
    #             'placeholder': kwargs['instance'].title
    #         })

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"