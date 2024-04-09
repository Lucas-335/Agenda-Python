from django.shortcuts import render, get_object_or_404
from contacts.models import Contact
# Create your views here.

def single_contact(requests,cont_id):
    #contact_ = Contact.objects.filter(id=cont_id).first()
    contact_ = get_object_or_404(Contact, id=cont_id, show=True)
    
    context = {
        'contact': contact_
    }
    
    return render(
        requests,
        'contacts/contact.html',
        context=context,
        )

