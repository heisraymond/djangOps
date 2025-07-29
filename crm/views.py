from django.shortcuts import render, redirect

from . models import DailyNote
from . forms import DailyNoteForm

def home(request):
    if request.method == 'POST':
        print(request)
        # Assign the form to a var ' form'
        form = DailyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(home)
    else:
        form = DailyNoteForm()
    
    notes = DailyNote.objects.all()

    return render(request, 'index.html', {'myForm': form, 'myNotes': notes})
