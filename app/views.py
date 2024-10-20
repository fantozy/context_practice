from django.shortcuts import render

def ip_address_processor(request):
    return {"ip_address": request.META['REMOTE_ADDR']}

def index(request):
    return render(request, 'index.html', ip_address_processor(request))

def user(request):
    username = "Nika"
    password = "123321"
    email = "nika@mziuri.ge"
    context = {
        "user": username, 
        "password": password,
        "email": email,
    }
    return render(request, 'user.html', context=context)