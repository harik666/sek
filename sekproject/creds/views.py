from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def fun_login(request):
    if request.method == 'POST':
        rusr = request.POST['v_usr']
        rpass = request.POST['v_pass']
        user = auth.authenticate(username=rusr, password=rpass)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            print("Invalid credentials")
            return redirect('log')
    return render(request, 'cred_login.html')


def fun_reg(request):
    if request.method == 'POST':
        usrname = request.POST['v_usrname']
        fname = request.POST['v_fname']
        lname = request.POST['v_lname']
        mail = request.POST['v_mail']
        pass1 = request.POST['v_pass']
        cpass = request.POST['v_cpass']
        if pass1 == cpass:
            if User.objects.filter(username=usrname).exists():
                messages.info(request, "username taken")
                print("username taken")
                return redirect('reg')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "mail taken")
                print("mail taken")
                return redirect('reg')
            else:
                objUser = User.objects.create_user(username=usrname,
                                                   password=pass1,
                                                   first_name=fname,
                                                   last_name=lname,
                                                   email=mail)
                objUser.save()
                print('user saved')
                return redirect('log')
        else:
            messages.info(request, "Password not matching")
            print("Password not matching")
            return redirect('reg')

    return render(request, 'cred_register.html')


def fun_logt(request):
    auth.logout(request)
    return redirect('/')

