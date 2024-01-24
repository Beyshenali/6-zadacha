from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    image = models.ImageField(
        upload_to="portrait/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.title}"
    
class Blok(models.Model):
    title_blok1 = models.CharField(
        max_length=155,
        verbose_name="Заголовок блока1"
    ) 
    title_description_blok1 = models.CharField(
        max_length=2, default="m",
        verbose_name="Надпис после заголовок блока1"
    )   
    description_blok1 = models.TextField(
        verbose_name="Описание блока1"
    )

    title_blok2 = models.CharField(
        max_length=155,
        verbose_name="Заголовок блока2"
    ) 

    title_description_blok2 = models.CharField(
        max_length=2,default="m",
        verbose_name="Надпис после заголовок блока2"
    )

    description_blok2 = models.TextField(
        verbose_name="Описание блока2"
    )

    title_blok3 = models.CharField(
        max_length=155,
        verbose_name="Заголовок блока3" 
    )

    title_description_blok3 = models.CharField(
        max_length=2,default="m",
        verbose_name="Надпис после заголовок блока3"
    )
    
    description_blok3 = models.TextField(
        verbose_name="Описание блока3"
    )

    def __str__(self):
        return f"{self.title_blok1}"

class Blok_Area(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок блока"
    )
    title1 = models.CharField(
        max_length=155,
        verbose_name="Заголовок Текста"
    )
    description1 = models.TextField(
        verbose_name="Описание первого текста"
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name="Заголовок второго текста"
    )
    description2 = models.TextField(
        verbose_name="Описание второго текста"
    )
    title3 = models.CharField(
        max_length=155,
        verbose_name="Заголовок третего текста"
    )
    description3 = models.TextField(
        verbose_name="Описание третего текста"
    )
    title_link =models.CharField(
        max_length=155,
        verbose_name="Описания для ссылка"
    )
    link = models.URLField(
        verbose_name="Ссылка для Портфоля"
    )
    image = models.ImageField(
        upload_to="portrait/",
        verbose_name="Фотография блока"
    )
    def __str__(self):
        return f"{self.title}"

class Meta:
    verbose_name="Настройки сайта"
    verbose_name_plural="Настройки сайта"
