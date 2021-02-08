from django.db import models

# Create your models here.

"""
```
Category Code,Diagnosis Code,Full Code,Abbreviated Description,Full Description,Category Title
A0,1234,A01234,"Comma-ind anal ret","Comma-induced anal retention","Malignant neoplasm of anus and anal canal"
```
"""


class ICD(models.Model):
    name = models.CharField(max_length=150, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Codes(models.Model):
    category_code = models.CharField(max_length=100, blank=True, default='')
    diagnosis_code = models.CharField(max_length=100, blank=True, default='',unique=True)
    full_code = models.CharField(max_length=100, blank=True, default='', unique=True)
    ab_description = models.CharField(max_length=250, blank=True, default='')
    full_description = models.CharField(max_length=250, blank=True, default='')
    category_title = models.CharField(max_length=150, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    ICD = models.ForeignKey(ICD, related_name='Codes', on_delete=models.CASCADE)

    def __str__(self):
        return self.category_title
