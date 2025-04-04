from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import User
from .forms import UserForm


def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'کاربر با موفقیت ذخیره شد.')
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')


def user_account(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_account.html', {'user': user})


def create_or_edit_user(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = User()
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'اطلاعات کاربر با موفقیت به‌روزرسانی شد.')
            return redirect('user_account', user_id=user.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'user': user})


#
