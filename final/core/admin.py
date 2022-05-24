from django.contrib import admin
from core.models import Book, Journal, BookJournalBase
# Register your models here.
admin.site.register(Book)
admin.site.register(Journal)