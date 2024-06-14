# Create your views here.
from django.shortcuts import render

def agregasi(input):
  result = input + 1
  return result





def page_landing(request):
  return render (request, 'app_landing/index.html')



def page_about(request):

  context = {
    "Nama": "Sepyan Purnama",
    "Agregasi ": agregasi(5)
  }
  return render (request, 'app_landing/about.html',context)


def page_profil(request):
  return render (request, 'app_landing/profil.html')

def page_informasi(request):
  return render (request, 'app_landing/informasi.html')

def page_visi_misi(request):
  return render (request, 'app_landing/visi-misi.html')
