from rest_framework import serializers
from .models import stock

class stockserializer(serializers.ModelSerializer):
    class Meta:
        model=stock
        fields=(
            'stock_name','stock_amount','price_value','description','bought_date'
        )