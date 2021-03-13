from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class CompanyModel(models.Model):
    class Meta:
        db_table = 'company'

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='company')
