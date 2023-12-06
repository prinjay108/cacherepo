from django.shortcuts import render
# from django.views.decorators.cache import cache_page

# Create your views here.
# @cache_page(30) #view based cache
def home(request):
    return render(request,'home.html')

