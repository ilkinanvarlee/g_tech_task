from django.shortcuts import render
from apps.user.forms import ProfileForm
from apps.web.models import Product


def profile_view(request):
    products = Product.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {'form': form,
               'products': products}

    return render(request, 'user/user_dashboard.html', context)

