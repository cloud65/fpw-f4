import rest_framework.fields
from rest_framework import serializers

from .models import Categories, EdaIngredients, EdaItems, Eda, Ingredients


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    image = rest_framework.fields.UUIDField()
    class Meta:
        model = Categories
        fields = ('guid', 'name', 'image')


class EdaSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)
    image = rest_framework.fields.UUIDField()
    class Meta:
        model = Eda
        fields = ('guid', 'name', 'categories', 'image')

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('name', 'guid')

class EdaIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientsSerializer(many=False, read_only=True)
    class Meta:
        model = EdaIngredients
        fields = ('ingredient', 'count')

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdaItems
        fields = ('guid', 'step', 'text')

class EdaDetailSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)
    ingredients = EdaIngredientsSerializer(many=True, read_only=True)
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Eda
        fields = ('guid', 'name', 'categories', 'ingredients', 'items', 'image')