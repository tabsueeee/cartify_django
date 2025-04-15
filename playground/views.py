from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

from item.models import Item, Category
from .forms import SignUpForm
# Create your views here.
#request handler


def main(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'items': items, 
        'categories': categories
        })


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playground:login')
    else:
        form = SignUpForm()

    return render (request, 'signup.html',{
        'form': form

    })


def userloggedin(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        return False


def logout_view(request):
        logout(request)
        return redirect('playground:main')