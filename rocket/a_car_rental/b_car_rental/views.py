from django.shortcuts import render, redirect
from .models import Car, RentCar
from b_user.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
import time


class SuperCarListView(ListView):
    model = Car
    template_name = 'b_car_rental/list_view/super_car_list.html'


class CarListView(ListView):
    model = Car
    template_name = 'b_car_rental/list_view/car_list.html'


class WebsiteCarListView(ListView):
    model = Car
    template_name = 'b_car_rental/list_view/website_car_list.html'


class SuperCarCreateView(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'b_car_rental/create_view/super_car_create.html'
    success_url = '/attach/car/list/'


class SuperCarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'b_car_rental/update_view/super_car_update.html'
    success_url = '/attach/car/list/'


class SuperCarDeleteView(DeleteView):
    model = Car
    template_name = 'b_car_rental/delete_view/super_car_confirm_delete.html'
    success_url = '/attach/car/list/'


class SuperCarDetailView(DetailView):
    model = Car
    template_name = 'b_car_rental/detail_view/super_car_detail.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'b_car_rental/detail_view/car_detail.html'


class WebsiteCarDetailView(DetailView):
    model = Car
    template_name = 'b_car_rental/detail_view/website_car_detail.html'


class SuperRentCarListView(ListView):
    model = RentCar
    template_name = 'b_car_rental/list_view/super_rent_car_list.html'


class SuperRentCarCreateView(CreateView):
    model = RentCar
    fields = '__all__'
    template_name = 'b_car_rental/create_view/super_rent_car_create.html'
    success_url = '/attach/rent_car/list/'


class SuperRentCarUpdateView(UpdateView):
    model = RentCar
    fields = '__all__'
    template_name = 'b_car_rental/update_view/super_rent_car_update.html'
    success_url = '/attach/rent_car/list/'


class SuperRentCarDeleteView(DeleteView):
    model = RentCar
    template_name = 'b_car_rental/delete_view/super_rent_car_confirm_delete.html'
    success_url = '/attach/rent_car/list/'


class SuperRentCarDetailView(DetailView):
    model = RentCar
    template_name = 'b_car_rental/detail_view/super_rent_car_detail.html'


def rent_car_list(request):
    user = request.user.id
    rent_car = RentCar.objects.filter(client=user)
    if rent_car.exists():
        rent_cars = rent_car
        return render(request, 'b_car_rental/list_view/rent_car_list.html', {'rent_cars': rent_cars})
    else:
        message = "You haven't rented any car yet!!"
        return render(request, 'b_car_rental/list_view/rent_car_list.html', {'message': message})


def rent_car(request, pk):
    # username = request.user.username
    user = request.user.id
    client = User.objects.get(id=user)
    car = Car.objects.get(pk=pk)
    date_of_issue = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # datetime.datetime.now()
    planned_return_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # datetime.datetime.now()
    try:
        order = RentCar.objects.create(
            client=client,
            car=car,
            date_of_issue=date_of_issue,
            planned_return_date=planned_return_date
        )
    except:
        order = RentCar.objects.get(
            client=client,
            car=car,
            date_of_issue=date_of_issue,
            planned_return_date=planned_return_date
        )

    return render(request, 'b_car_rental/list_view/rent_car_list.html', {'order': order}) \
           and redirect('/overview/rent_car/list/')
