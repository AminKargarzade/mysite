from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')  # Redirect to a success page.
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')  # Redirect if already authenticated
def logout_view(request):
    pass  # Implement logout logic here
def signup_view(request):
    return render(request, 'accounts/signup.html')