from rest_framework.serializers import ModelSerializer
from core.models import Book, Journal, BookJournalBase


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
