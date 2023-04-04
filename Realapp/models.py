from django.db import models

# Create your models here.
class stock(models.Model):
    stock_name=models.CharField(max_length=100000)
    stock_amount=models.IntegerField()
    price_value=models.IntegerField()
    description=models.TextField()
    bought_date=models.DateTimeField(auto_now=True)
    def __self__(self):
        return self.name

