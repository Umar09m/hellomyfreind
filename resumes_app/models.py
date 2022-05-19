from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="pdf_files")
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Закладки'
        verbose_name_plural = 'Закладки'
        unique_together = (('user', 'wished_resume'),)

    def __str__(self):
        return f"{self.user} {self.wished_resume}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        unique_together = (('name',),)


class Partners(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="partners")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'
        unique_together = (('title', 'link'),)