from django.shortcuts import render
from .models import Note, Tag   

# Create your views here.
def note_list(request):
    """View for showing all notes"""
    notes = Note.objects.all()
    tags = Tag.objects.all()
    return render(request, 'google_keep/note_list.html',{'notes': notes, 'tags':tags})
