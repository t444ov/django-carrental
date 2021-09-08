from django.urls import path
from .views import (
    SuperCarListView,
    CarListView,
    WebsiteCarListView,
    SuperRentCarListView
)
from .views import (
    SuperCarCreateView,
    SuperRentCarCreateView
)
from .views import (
    SuperCarUpdateView,
    SuperRentCarUpdateView
)
from .views import (
    SuperCarDeleteView,
    SuperRentCarDeleteView
)
from .views import (
    SuperCarDetailView,
    CarDetailView,
    WebsiteCarDetailView,
    SuperRentCarDetailView
)
from .views import (
    rent_car_list,
    rent_car
)

urlpatterns = [
    path('attach/car/list/', SuperCarListView.as_view(), name='attach_car_list'),
    path('overview/car/list/', CarListView.as_view(), name='overview_car_list'),
    path('car/list/', WebsiteCarListView.as_view(), name='car_list'),
    path('attach/rent_car/list/', SuperRentCarListView.as_view(), name='rent_car_list'),

    path('attach/car/create/', SuperCarCreateView.as_view(), name='car_create'),
    path('attach/rent_car/create/', SuperRentCarCreateView.as_view(), name='rent_car_create'),

    path('attach/car/<int:pk>/update/', SuperCarUpdateView.as_view(), name='car_update'),
    path('attach/rent_car/<int:pk>/update/', SuperRentCarUpdateView.as_view(), name='rent_car_update'),

    path('attach/car/<int:pk>/delete/', SuperCarDeleteView.as_view(), name='car_delete'),
    path('attach/rent_car/<int:pk>/delete/', SuperRentCarDeleteView.as_view(), name='rent_car_delete'),

    path('attach/car/<int:pk>/detail/', SuperCarDetailView.as_view(), name='car_detail'),
    path('overview/car/<int:pk>/detail/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/detail/', WebsiteCarDetailView.as_view(), name='car_detail'),
    path('attach/rent_car/<int:pk>/detail/', SuperRentCarDetailView.as_view(), name='rent_car_detail'),

    path('overview/rent_car/list/', rent_car_list, name='client_rent_car'),
    path('overview/car/<int:pk>/rent/', rent_car, name='rent_car'),
]
