from django.shortcuts import redirect, render
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    search = request.GET.get('search-area')
    if search:
        contacts = Contact.objects.filter(fullname__icontains=search)
    else:
        contacts = Contact.objects.all()
        search = ''
    return render(request, 'index.html', {'contacts': contacts, 'search': search})


def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})


def addContact(request):
    if request.method == "POST":
        new_contact = Contact(
            fullname=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address'],
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.fullname = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})
