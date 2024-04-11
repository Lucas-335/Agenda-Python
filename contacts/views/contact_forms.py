
from django.shortcuts import render, redirect
from contacts.forms import ContactForm
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context={
            'form':form,
        }
        
        if form.is_valid():
            # contact = form.save(commit = False)
            # contact.show = False
            form.save()
            return redirect('contacts:create')
            
        return render(
            request,
            'contacts/create.html',
            context=context,
        )

    form = ContactForm()
    context = {
        'form':form
    }

    return render(
        request,
        'contacts/create.html',
        context=context
        )


