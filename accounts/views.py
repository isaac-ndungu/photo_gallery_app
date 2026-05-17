from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Account created")
            return redirect('index')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')
