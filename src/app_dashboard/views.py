from django.shortcuts import render
from .queries import book_create

# Create your views here.

def page_index(request):
  query = book_create('Harry Potter - Azkaban', 'JK.Rowling', 'Fiction')
  print(query)
  return render(request,"app_landing/about.html")

  # return render (request,"app_dashboard/index.html")

def page_beranda(request):
    return render(request, "app_dashboard/beranda.html")

def page_status(request):
  return render(request, "app_dashboard/status.html")