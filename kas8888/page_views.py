from django.shortcuts import render

def contact_view(request):
    return render(request, "pages/contact.html")

def about_view(request):
    return render(request, "pages/about.html")
