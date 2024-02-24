from django.shortcuts import render
from .models import Contact
from .forms import ContactForm, ContactModelForm
def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         x = Contact(
    #             name = request.POST['name'],
    #             email = request.POST['email'],
    #             message = request.POST['message']
    #         )
    #         x.save()

    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request, 'contact/index.html', {'form':ContactModelForm})
