from django.shortcuts import render
from .models import Note, Tag   

# Create your views here.
def note_list(request):
    """View for showing all notes"""
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html',{'notes': notes})
