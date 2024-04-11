from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contacts.forms import ContactForm
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context={
            'form':form,
        }

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


