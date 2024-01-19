from django.views.generic import CreateView, DetailView, ListView

from .forms import NotesForm
from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = "/smart/notes"


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"

