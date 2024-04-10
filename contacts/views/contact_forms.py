from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from contacts.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
# Create your views here.

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','phone','email']

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()
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


