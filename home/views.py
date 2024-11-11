from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home/home.html")
def faq(request):
    return render(request, "home/faq_support.html")
def terms(request):
    return render(request, "home/terms_privacy.html")
def home(request):
    return render(request, "home/home.html")

def custom_404(request, exception):
    return render(request, 'home/404.html', status=404)

def custom_500(request):
    return render(request, 'home/500.html', status=500)