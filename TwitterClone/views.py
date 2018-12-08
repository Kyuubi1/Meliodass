from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import QuickLogin, Signup, CreatePost

from . models import Account

from  django.contrib.auth.models import User
# Create your views here.


# class IndexView(View):
#     def get(self, request):
#         return render(request, 'TwitterClone/index.html')


class Qlogin(View):
    def get(self, request):
        lg = QuickLogin()
        return render(request, 'TwitterClone/index.html', {'up': lg})


class PostLogin(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user_login = authenticate(username=username, password=password)
        print(user_login)
        if user_login is None:
            lg = QuickLogin()
            context = {'up': lg}
            return render(request, 'TwitterClone/index.html', context)
        login(request, user_login)
        tg = username
        pt = CreatePost()
        return render(request, 'TwitterClone/home.html', {'acc': tg, 'post':pt})


class LoginView(View):
    def get(self, request):
        lg = QuickLogin()
        return render(request, 'TwitterClone/Login.html', {'up': lg})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_login = authenticate(username=username, password=password)
        print(user_login)
        if user_login is None:
            lg = QuickLogin()
            context = {'up': lg}
            return render(request, 'TwitterClone/Login.html', context)
        login(request, user_login)
        tg = username
        pt = CreatePost()
        return render(request, 'TwitterClone/home.html', {'acc': tg, 'post': pt})


class SignupView(View):
    def get(self, request):
        si = Signup()
        return render(request, 'TwitterClone/Sign-up.html', {'in': si})

    def post(self, request):
        si = Signup(request.POST)
        if si.is_valid():

            user = Account()
            user.username = si.cleaned_data.get('username')
            user.set_password(si.cleaned_data.get('password'))
            user.email = si.cleaned_data.get('email')
            user.phone = si.cleaned_data.get('phone')
            user.sex = si.cleaned_data.get('sex')
            # user.is_staff = False
            # user.is_superuser = True
            user.save()
            user.refresh_from_db()
            lg = QuickLogin()
            return render(request, 'TwitterClone/Login.html', {'up': lg})

        else:
            # return render(request, 'TwitterClone/Sign-up.html', {'in': si})
            return HttpResponse('false')


class PostView(View):
    def get(self, request):

        return render(request, 'TwitterClone/home.html', {'post': pt})




