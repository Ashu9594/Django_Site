from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,"username taken")
                return redirect("register")
            elif User.objects.filter(email=email):
                messages.info(request,"email taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                messages.info(request,"password does not match")
                return redirect("register")
        else:   
            messages.info(request,"password does not match")
            return redirect("register")

        return redirect("/")
    else:
        return render(request, "register.html")
    