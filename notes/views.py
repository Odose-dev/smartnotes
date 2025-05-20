from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm

from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes 
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"  #not compulsory
    

class NotesLiked(View):
    def post(self, request, pk):
      note = get_object_or_404(Notes, pk=pk)
      note.no_of_likes += 1
      note.save()
      return redirect('notes.detail', pk=note.pk)


class isPublic(View):
    def post(self, request, pk):
      note = get_object_or_404(Notes, pk=pk)
      print(note.is_public)
      note.is_public = True
      note.save()
      return redirect('notes.detail', pk=note.pk)
  

class NotesUnliked(View):
    def post(self, request, pk):
      note = get_object_or_404(Notes, pk=pk)
      note.no_of_likes -= 1
      note.save()
      return redirect('notes.detail', pk=note.pk)

   
 

class NotesUpdateView(UpdateView):
   model = Notes
   success_url = '/smart/notes'
   form_class = NotesForm

class NotesCreateView(CreateView):
   model = Notes
   success_url = '/smart/notes'
   form_class = NotesForm
   login_url = '/admin'
   
   def form_valid(self, form):
       self.object = form.save(commit=False)
       self.object.user = self.request.user
       self.object.save()
       return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes" #this corresponds to the "picker" from the html view
    template_name = "notes/note_list.html"  #not compulsory
    login_url = "/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all() 
    


class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes" #this corresponds to the "picker" from the html view
    template_name = "notes/popular_notes.html"  #not compulsory
    queryset = Notes.objects.filter(no_of_likes__gte=1)
    
    
            
    

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note" #this corresponds to the "picker" from the html view
    template_name = "notes/note_details.html"  

def view_note_details(request, pk):
    try:
        note_details = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render (request,'notes/note_details.html', {'note': note_details})
    