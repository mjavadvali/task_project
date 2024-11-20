from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, )


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
    

class ProductStatus(models.IntegerChoices):
    available = 1, _('موجود')
    unavailable = 2, _('ناموجود')

class Product(models.Model):
    title = models.CharField(max_length=70, verbose_name=_("title"))
    slug = models.CharField(max_length=70, verbose_name=_("slug"))
    category = models.ForeignKey(Category, 
                                 verbose_name=_("category"), 
                                 on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.IntegerField(choices=ProductStatus.choices, 
                                    verbose_name=_("available"), 
                                    default=ProductStatus.unavailable.value)
    price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0, verbose_name=_("price")
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title