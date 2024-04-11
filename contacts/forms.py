from django.core.exceptions import ValidationError
from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            

            if field == 'first_name':
                ...
            else:
                self.fields[field].widget.attrs.update({
                    'placeholder':'Escreva aqui'
                })

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Escreva aqui'
            },
        ),
        help_text='Escreva seu primeiro nome'
    )

    class Meta:
        model = Contact
        fields = ['first_name','last_name','phone','email','description','category']

    def clean(self):
        cleaned_data = self.cleaned_data
        
        if cleaned_data['first_name'] == cleaned_data['last_name']:
            self.add_error(
                None,
                ValidationError(
                    'Primeiro nome igual ao segundo',
                    code='invalid'
                )
            )
        return super().clean()
    
    