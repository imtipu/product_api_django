from django.db import models

# Create your models here.
from django.utils.text import slugify


def product_unique_slug(modelclass, field):
    original_slug = slugify(field)
    unique_slug = original_slug
    num = 1
    while modelclass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (original_slug, num)
        num += 1
    return unique_slug


class Product(models.Model):
    title = models.CharField(default=None, max_length=256, null=False, blank=False)
    slug = models.SlugField(null=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, max_length=32, null=False)
    currency = models.CharField(default='BDT', max_length=10, null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'products'

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.title) != self.slug:
                self.slug = product_unique_slug(Product, self.title)
        else:
            self.slug = product_unique_slug(Product, self.title)
        super(Product, self).save(*args, **kwargs)


class AttributeVariants(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, related_name="attribute_variants",
    )
    type = models.CharField(default=None, max_length=32, null=False)
    name = models.CharField(default=None, max_length=32, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, max_length=32, null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.product.title

    class Meta:
        db_table = 'attribute_variants'



