from django.shortcuts import render

# Create your views here.

def contacts(requests):
    return render(
        requests,
        'contacts/index.html'
        )
