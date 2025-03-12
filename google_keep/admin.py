from django.contrib import admin
from .models import Note, Tag

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added']
    filter_horizontal = ('tags',)  # Esto mejora la interfaz para seleccionar tags
