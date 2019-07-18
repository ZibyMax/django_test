from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def get_info(self):
        return ProductInfo.objects.filter(product=self)

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.info