from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth.views import LoginView
from .forms import RegistrationSuperUserForm, RegistrationUserForm, LoginUserForm
from .models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


class SuperUserListView(ListView):
    model = User
    template_name = 'b_user/list_view/super_user_list.html'


class SuperUserCreateView(CreateView):
    model = User
    fields = '__all__'
    template_name = 'b_user/create_view/super_user_create.html'
    success_url = '/attach/user/list/'


class SuperUserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'b_user/update_view/super_user_update.html'
    success_url = '/attach/user/list/'


class SuperUserDeleteView(DeleteView):
    model = User
    template_name = 'b_user/delete_view/super_user_confirm_delete.html'
    success_url = '/attach/user/list/'


class SuperUserDetailView(DetailView):
    model = User
    template_name = 'b_user/detail_view/super_user_detail.html'


class UserListView(ListView):
    model = User
    template_name = 'b_user/list_view/user_list.html'


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    template_name = 'b_user/create_view/user_create.html'
    success_url = '/overview/user/list/'


class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'b_user/update_view/user_update.html'
    success_url = '/overview/user/list/'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'b_user/delete_view/user_confirm_delete.html'
    success_url = '/overview/user/list/'


class UserDetailView(DetailView):
    model = User
    template_name = 'b_user/detail_view/user_detail.html'


class RegisterUser(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST or None)
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/account/login/')
        return render(request, 'registration/register.html', {'form': form})


class RegisterSuperUser(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationSuperUserForm(request.POST or None)
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationSuperUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/attach/account/login/')
        return render(request, 'registration/register.html', {'form': form})


class LoginUser(LoginView):
    form = LoginUserForm
    template_name = "registration/login.html"

    def get_success_url(self):
        return reverse_lazy('overview_car_list')


class LoginSuperUser(LoginView):
    form = LoginUserForm
    template_name = "registration/login.html"
    
    def get_success_url(self):
        return reverse_lazy('attach_car_list')


def profile_super_user(request):
    args = {'user': request.user}
    return render(request, 'b_user/detail_view/user_profile.html', args)


def profile_user(request):
    args = {'user': request.user}
    return render(request, 'b_user/detail_view/user_profile_overview.html', args)


def login_user(self, request, *args, **kwargs):
    form = LoginUserForm(request.POST or None)
    if form.is_valid():
        username = request.GET.get('username', '') 
        password = request.GET.get('password', '') 

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/attach/car/list/')
        return render(request, 'registration/login.html', {'form': form})


def login_super_user(request):
    # global isLogin
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    result_user = User.objects.filter(email=email, password=password)

    if result_user.exists():
        request.session['user_email'] = email
        # isLogin = True
        return redirect('/attach/car/list/')
    else:
        message = "Invalid Email or password!!"
        return render(request, 'registration/login.html', {'message': message})


def logout_user(request):
    logout(request)
    return redirect('/')
