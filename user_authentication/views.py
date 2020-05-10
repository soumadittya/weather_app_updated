from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Extended_UserCreationForm, Modified_UserCreationForm, \
    Select_cities
from .models import Selected_cities
from main.api_weather import make_request_query_set, make_request_name
from django.core.mail import send_mail
from main.image_select import image

def signup(request):
    if request.method == 'POST':
        form = Modified_UserCreationForm(request.POST)
        extended_form = Extended_UserCreationForm(request.POST)
        if form.is_valid() and extended_form.is_valid():
            form_saved = form.save()
            user = extended_form.save(commit = False)
            user.user = form_saved
            user.save()
            return render(request, 'congratulation.html',
                          {'username': form.cleaned_data.get('username')})
        else:
            try:
                return HttpResponse('<h1>Something went wrong.</h1>')
            except:
                pass
    else:
        form = Modified_UserCreationForm
        extended_form = Extended_UserCreationForm
        return render(request, 'signup.html', {'form' : form,
                                               'extended_form': extended_form})

@login_required
def profile_home(request):
    hometown = ''
    city_list = ''
    var = Selected_cities.objects.filter(user__username = request.user.username)
    hometown, city_list = make_request_query_set(query_set = var)

    if hometown == '' or city_list == '':
        return render(request, 'setup_account.html', {})
    else:
        img = image(hometown['set']['weather'][0]['icon'])

        return render(request, 'profile_home.html',
                      {'hometown': hometown,'details' : city_list, 'image_theme': img})

@login_required
def profile_settings(request):
    if request.method == 'POST':
        save = True
        select_city_form = Select_cities(request.POST)
        if select_city_form.is_valid():
            if Selected_cities.objects.filter(user__username = request.user.username).count() >= 6:
                messages.success(request, 'You cannot add more than 6 cities.')
                return redirect('profile_settings')
            else:
                var = Selected_cities.objects.filter(user__username=request.user.username)
                for i in var:
                    if i.cities == request.POST['cities']:
                        save = False

                if save == True:
                    if request.POST.get('hometown') == 'on':
                        Selected_cities.objects.filter(user__username = request.user.username).update(hometown= False)
                        print('------process done-------')
                    user = select_city_form.save(commit=False)
                    user.user = request.user
                    user.save()

                messages.success(request, 'City has been added.')
                return redirect('profile_settings')
    else:
        select_city_form = Select_cities
        return render(request, 'profile_settings.html', {'select_city_form': select_city_form})

@login_required
def delete_city(request, city_id):
    var = Selected_cities.objects.get(pk = city_id)
    var.delete()
    messages.success(request, 'City has been deleted')
    return redirect('profile_home')

@login_required
def set_hometown(request, hometown_id):
    var = Selected_cities.objects.get(id = hometown_id)
    print('------',type(var), '----------', var.user_id)
    Selected_cities.objects.filter(user__id = var.user_id).update(hometown = False)
    Selected_cities.objects.filter(id = hometown_id).update(hometown = True)
    return redirect('profile_home')