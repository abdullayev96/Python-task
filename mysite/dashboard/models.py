from django.db import models
from baseapp.models import BaseModel



class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name="Kategoriya:")
    description = models.TextField()
    parent = models.ForeignKey("Category", on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Kategoriya_"


class Shop(models.Model):
    title = models.CharField(max_length=300, verbose_name="Do'kon nomi:")
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = "Do'kon_"



class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Mahsulot nomi:")
    description = models.TextField(verbose_name="Mahsulot haqida:")
    amount = models.IntegerField()
    price = models.FloatField()
    images = models.ManyToManyField(Shop, related_name="images")
    activate = models.BooleanField(default=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Mahsulot_"
