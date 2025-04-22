from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import OrderForm
# Create your views here.


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        try:
            if form.is_valid():
                form.save()  # ذخیره داده‌های فرم در پایگاه داده
                return redirect('success')  # هدایت به صفحه موفقیت
            else:
                return render(request, 'order_form.html', {'form': form, 'error_message': 'فرم معتبر نیست! لطفاً دوباره بررسی کنید.'})
        except Exception as e:
            # مدیریت خطاها
            error_message = f"خطایی رخ داده است: {str(e)}"
            return render(request, 'order_form.html', {'form': form, 'error_message': error_message})
    else:
        form = OrderForm()

    return render(request, 'Order.html', {'form': form})


def success_view(request):
    return render(request, 'success.html', {'message': 'سفارش شما با موفقیت ثبت شد!'})


def error_view(request):
    return render(request, 'error.html', {'message': 'متأسفیم، مشکلی رخ داده است. لطفاً دوباره تلاش کنید!'})
