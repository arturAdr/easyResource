from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

from EasyResource.fields import JSONSchemaField

class Shoe(models.Model):

    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    informations = JSONField()
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    price = models.FloatField()
    sizes = JSONSchemaField(schema = { 
        "type": "array",
        "items": {
            "type": "object",
            "required": [
                "size",
                "available_quantity"
            ],
            "additionalProperties": False,
            "properties": {
                "size": {
                    "type": "integer",
                },
                "available_quantity": {
                    "type": "integer"
                }
            }
        }
    })

    class Meta:
        verbose_name = u'Shoe'
        verbose_name_plural = u'Shoes'

    def __str__(self):
        return self.name