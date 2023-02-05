import uuid

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Eda(BaseModel):
    name = models.CharField(max_length=512)

    @property
    def image(self):
        return self.items.order_by('-step').last().guid


class Categories(BaseModel):
    name = models.CharField(max_length=128)
    eda = models.ManyToManyField(Eda, related_name='categories')

    @property
    def image(self):
        return Eda.objects.filter(categories=self).first().image


class Ingredients(BaseModel):
    name = models.CharField(max_length=512)

class EdaIngredients(BaseModel):
    eda = models.ForeignKey(Eda, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='names')
    count = models.CharField(max_length=30)

class EdaItems(BaseModel):
    eda = models.ForeignKey(Eda, on_delete=models.CASCADE, related_name='items')
    step = models.IntegerField()
    text = models.TextField()
    image = models.BinaryField(null=True)