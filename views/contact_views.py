from django.shortcuts import render
from contacts.models import Contact
# Create your views here.

def index(requests):
    #contact_ = Contact.objects.all()
    contact_ = Contact.objects \
        .filter(show=True)\
        .order_by('id')\
        [:10]
    

    context = {
        'contact': contact_
    }
    return render(
        requests,
        'contacts/index.html',
        context=context
        )
