from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from hitcount.models import HitCountMixin
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
    


    def __str__(self):
        return self.title
    

class ProductStatus(models.IntegerChoices):
    available = 1, _('موجود')
    unavailable = 2, _('ناموجود')

    

class Product(models.Model, HitCountMixin):
    title = models.CharField(max_length=70, verbose_name=_("title"))
    slug = models.CharField(max_length=70, verbose_name=_("slug"), blank=True)
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

    image = models.ImageField( 
                            upload_to="images/products",
                            verbose_name=_("image"),
                            blank=True,
                            validators= [
                                    FileExtensionValidator(
                                    allowed_extensions=["jpg", "jpeg", "png", "webp"],
                                    message='فرمت عکس باید .jpg, .jpeg, ,webp,  .png باشد'
                                )],
                            )
    
    hit_count_generic = GenericRelation(
                        HitCount, object_id_field='object_pk',
                        related_query_name='hit_count_generic_relation')
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ProductInfo(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    views = models.IntegerField(default=0)
    # number_of_sells = ----------
    

    def __str__(self):
        return f'{self.product}-{self.date}'
    