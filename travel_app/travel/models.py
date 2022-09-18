from django.db import models

# Create your models here.
class PriceModel(models.Model):
    dist_base_price = models.FloatField()
    dist_additional_price = models.FloatField()
    time_factor_multi = models.IntegerField()
    additional_distance = models.FloatField()
    is_admin = models.BooleanField(default=True)
