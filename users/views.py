from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, studentAccountUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .models import studentAccount

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We have emailed you instructions to reset your password."
    success_url = '/'
    
    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()  

            student = studentAccount.objects.get(user=user)
            student.Course = form.cleaned_data.get('course')
            student.save()
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
def student_account(request):
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

