from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        pswd1 = request.POST.get('pswd1')
        pswd2 = request.POST.get('pswd2')

        if pswd1 == pswd2:
            user = request.user
            user.set_password(pswd1)
            user.save()
            messages.success(request, 'Contraseña actualizada')
            return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden')

    return render(request, 'profile.html')
    
def remove_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        user = request.user
        user.inventory = [product for product in user.inventory if product[0] != product_name]
        user.save()
        return redirect('profile')