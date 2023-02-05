import uuid

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters

from .serializers import CategoriesSerializer, EdaSerializer, EdaDetailSerializer
from .models import Categories, Eda, EdaItems

@cache_page(86400)
def get_image(request, guid):
    try:
        data = EdaItems.objects.get(pk=uuid.UUID(guid))
    except EdaItems.DoesNotExist:
        return None
    return HttpResponse(data.image, content_type='image/png')

class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all().order_by('name')
    serializer_class = CategoriesSerializer

class EdaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Eda.objects.all()
    filter_backends = [filters.SearchFilter]
    serializer_class = EdaSerializer

    def get_queryset(self):
        print(self.request.query_params)
        category = self.request.query_params.get('search')
        return Eda.objects.filter(categories=category)

    def retrieve(self, request, pk=None):
        queryset = Eda.objects.all()
        eda = get_object_or_404(queryset, pk=pk)
        serializer = EdaDetailSerializer(eda)
        return Response(serializer.data)


