from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, studentAccountUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account!')
        return redirect('ModuleRegistrationSystem:home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form, 'title': 'Student Registration'})

@login_required
def studentAccount(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = studentAccountUpdateForm(request.POST, request.FILES, instance = request.user.studentaccount)

        u_form.save()
        p_form.save()
        messages.success(request, 'Your account has been successfully updated')
        return redirect('studentAccount')
    
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = studentAccountUpdateForm(instance = request.user.studentaccount)
        context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Account'}
        return render(request, 'users/studentAccount.html', context)