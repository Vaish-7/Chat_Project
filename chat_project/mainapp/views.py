from django.shortcuts import render, redirect
#user needs to be redirected after login
from django.contrib.auth import login
from .forms import SignUpForm
#views and forms are in same folder

# Create your views here.
def frontpage(request):
    return render(request,'mainapp/frontpage.html')

def signup(request):
    if request.method == 'POST': 
    # checking if submit button is clicked
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage') #name in views of frontpage fun
    else:
        form=SignUpForm()
    return render(request, 'mainapp/signup.html', {'form': form})