from django.shortcuts import render, redirect
from api.models import Member3
from .Form import ContactForm
from .ModelForm import ModelForms

# def contact_view(request):
#     contact_form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         if contact_form.is_valid:
#             simpan_data = Member3.objects.create(
#                 namapertama = contact_form.cleaned_data.get('namapertama'),
#                 namabelakang = contact_form.cleaned_data.get('namabelakang'),
#                 periode = contact_form.cleaned_data.get('alamat'),
#                 date = contact_form.cleaned_data.get('date')
#             )
#             contact_form.save()
#             return redirect('Contact:kontakList')
#     context = {
#         'form_saya': contact_form
#     }
#     return render(request, 'contact.html', {'form': contact_form})

# from django.shortcuts import render, redirect
# from .Form import ContactForm  # Importing the ContactForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data (this example simply prints it to the console)
#             print(form.cleaned_data)
#             # Here you might want to redirect to a new URL,
#             # or handle the form data by saving it to a database, etc.
#             return redirect('public/')  # Placeholder for where to redirect after successful form submission
#     else:
#         form = ContactForm()  # An unbound form for GET request

#     # Render the form with the context on a template named 'contact.html'
#     return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, redirect
from .Form import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ModelForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/public/')  # Gantikan 'home' dengan nama URL tujuan Anda
    else:
        form = ContactForm()
    return render(request, 'Contact/contact.html', {'form': form})
