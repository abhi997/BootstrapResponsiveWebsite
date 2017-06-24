from django.shortcuts import render


# Create your views here.

def Home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)
def About(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)