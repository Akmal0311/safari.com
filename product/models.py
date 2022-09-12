from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=111)
    image = models.ImageField(default='mountain.jpg')
    size = models.CharField(max_length=11)
    color = models.CharField(max_length=11)
    price = models.IntegerField()
    like = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=111)

    def __str__(self):
        return self.name


class Type(models.Model):

    name = models.CharField(max_length=111)

    def __str__(self):
        return self.name
