from django.views.generic import ListView
from .models import Category, Product
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm, CategoryForm
from django.http import JsonResponse
from django.utils.text import slugify
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class ProductList(ListView):
    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'products/products_list.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        products = self.get_queryset() 
        return render(request, self.template_name, {'products': products, 'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.FILES, request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            new_product = form.save(commit=False)
            new_product.slug = slugify(title)  
            new_product.save()
            return redirect('product_list')
        else:
            print(form.errors) 
            print(request.POST) 
        products = self.get_queryset()  
        return render(request, self.template_name, {'products': products, 'form': form})

class ProductDetail(View):
    template_name = 'products/product_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)

        hit_count = HitCount.objects.get_for_object(product)
        HitCountMixin.hit_count(request, hit_count) 
        return render(request, 
                      template_name=self.template_name, 
                      context={'product': product, 'form': form})
    
    def post(self, request, pk):
        if request.user.is_superuser:
            product = get_object_or_404(Product, pk=pk)
            if 'delete' in request.POST:
                product.delete()
                return redirect('products_list')
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_detail', pk=pk)
            return render(request, 
                        template_name=self.template_name, 
                        context={'product': product, 'form': ProductForm})
        else:
            return JsonResponse({'error': 'Only admin users can update the product.'}, status=403)
    
        
    def delete(self, request, pk):
        if request.user.is_superuser:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Only admin users can delete the product.'}, status=403)
            

class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'categories/categories_list.html'


class CategoryDetail(View):
    template_name = 'categories/category_detail.html'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 
                      template_name=self.template_name, 
                      context={'category': category, 'form': form})
    
    
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        if request.user.is_superuser:
            if 'delete' in request.POST:
                category.delete()
                return redirect('categories_list')
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('category_detail', pk=pk)
            return render(request, 
                        template_name=self.template_name, 
                        context={'category': category, 'form': form})
        else:
            return JsonResponse({'error': 'Only admin users can update the product.'}, status=403)

        
            
    def delete(self, request, pk):
        if request.user.is_superuser:
            category = get_object_or_404(Category, pk=pk)
            category.delete()
            return JsonResponse({'message': 'Category deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Only admin users can delete the category.'}, status=403)
        


class CategoryProductsList(View):  
    def get(self, request, pk):
        if Category.objects.filter(pk=pk).exists():
            category = get_object_or_404(Category, pk=pk)
            products = Product.objects.filter(category=category)
        return render(request, 'categories/category_products.html' ,{'products': products})