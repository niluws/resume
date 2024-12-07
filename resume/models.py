from django.db import models
from django.core.validators import RegexValidator


class Team(models.Model):
    photo = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True,
                             validators=[RegexValidator(regex='^09\d{9}$',
                                                        message='Phone number must be entered in the format: "09xxxxxxxxx".')])

    city = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Project(models.Model):
    photo = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    photo = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True,
                             validators=[RegexValidator(regex='^09\d{9}$',
                                                        message='Phone number must be entered in the format: "09xxxxxxxxx".')])

    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.phone


class Form(models.Model):
    full_name = models.CharField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.full_name
