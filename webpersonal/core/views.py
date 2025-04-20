from django.shortcuts import render

# Create your views here.
def home(request):
    """Metodo home"""
    return render(request, 'core/home.html')

def about(request):
    """Acerca de """
    return render(request, 'core/acerca.html')

def contact(request):
    """contacto"""
    return render(request, 'core/contact.html')
