from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'interests.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def main(request):
    return render(request, 'index.html', {})
