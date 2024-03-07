import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import ProductDocument


class ProductDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta:
        document = ProductDocument
        fields = (
            'id',
            'name',
            'description',
            'size',
            'product_type'
        )
