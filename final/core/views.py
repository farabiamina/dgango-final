from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from core.models import Book, Journal
from core.serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookViewSet(viewsets.ViewSet):
    def get_books(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def add_book(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_book(self, request, book_id=None):
        queryset = Book.objects.all()
        my_book = get_object_or_404(queryset, pk=book_id)
        serializer = BookSerializer(my_book)
        return Response(serializer.data)

    def update_book(self, request, book_id=None):
        queryset = Book.objects.all()
        my_book = get_object_or_404(queryset, pk=book_id)
        serializer = BookSerializer(instance=my_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete_book(self, request, book_id=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=book_id)
        book.delete()
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser,)


class JournalViewSet(viewsets.ViewSet):
    def get_journals(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def add_journal(self, request):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_journal(self, request, j_id=None):
        queryset = Journal.objects.all()
        my_j = get_object_or_404(queryset, pk=j_id)
        serializer = JournalSerializer(my_j)
        return Response(serializer.data)

    def update_journal(self, request, j_id=None):
        queryset = Journal.objects.all()
        my_journal = get_object_or_404(queryset, pk=j_id)
        serializer = JournalSerializer(instance=my_journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete_journal(self, request, j_id=None):
        queryset = Journal.objects.all()
        journal = get_object_or_404(queryset, pk=j_id)
        journal.delete()
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser, )
