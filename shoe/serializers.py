from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = ('sku', 'name', 'details', 'informations', 'tags', 'price', 'sizes')
