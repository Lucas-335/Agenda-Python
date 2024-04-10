from django.shortcuts import render, get_object_or_404, redirect
from contacts.models import Contact
from django.db.models import Q
# Create your views here.

def index(requests):
    #contact_ = Contact.objects.all()
    contact_ = Contact.objects \
        .filter(show=True)\
        .order_by('id')\
        [:10]
    

    context = {
        'contact': contact_,
        'index_title':'Contato - '
    }
    return render(
        requests,
        'contacts/index.html',
        context=context
        )

def single_contact(requests,cont_id):
    #contact_ = Contact.objects.filter(id=cont_id).first()
    contact_ = get_object_or_404(Contact, id=cont_id, show=True)
    
    name_title = contact_.first_name
    context = {
        'contact': contact_,
        'contact_title': f'{name_title} - ',
    }
    
    return render(
        requests,
        'contacts/contact.html',
        context=context,
        )

def search(request):
    search_query = request.GET.get('q','').strip()

    if search_query == '':
        return redirect('contacts:index')
    
    contact_ = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(email__icontains=search_query)
            )\
        .order_by('id')\
        [:10] 

    context = {
        'contact': contact_,
        'contact_title': f'Search - ',
    }

    return render(
        request,
        'contacts/index.html',
        context

    )

