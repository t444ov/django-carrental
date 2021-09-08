from django.urls import path
from .views import (
    SuperUserListView,
    UserListView
)
from .views import (
    SuperUserCreateView,
    UserCreateView
)
from .views import (
    SuperUserUpdateView,
    UserUpdateView
)
from .views import (
    SuperUserDeleteView,
    UserDeleteView
)
from .views import (
    SuperUserDetailView,
    UserDetailView
)
from .views import (
    RegisterSuperUser,
    RegisterUser,
    LoginSuperUser,
    LoginUser,
    profile_super_user,
    profile_user
)
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('attach/user/list/', SuperUserListView.as_view(), name='user_list'),
    path('overview/user/list/', UserListView.as_view(), name='user_list'),

    path('attach/user/create/', SuperUserCreateView.as_view(), name='user_create'),
    path('overview/user/create/', UserCreateView.as_view(), name='user_create'),

    path('attach/user/<int:pk>/update/', SuperUserUpdateView.as_view(), name='user_update'),
    path('overview/user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),

    path('attach/user/<int:pk>/delete/', SuperUserDeleteView.as_view(), name='user_delete'),
    path('overview/user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    path('attach/user/<int:pk>/detail/', SuperUserDetailView.as_view(), name='user_detail'),
    path('overview/user/<int:pk>/detail/', UserDetailView.as_view(), name='user_detail'),

    path('attach/account/register/', RegisterSuperUser.as_view(), name='registration'),
    path('account/register/', RegisterUser.as_view(), name='registration'),

    path('attach/account/login/', LoginSuperUser.as_view(), name='login'),
    path('account/login/', LoginUser.as_view(), name='login'),

    path('attach/profile/', profile_super_user, name='profile'),
    path('overview/profile/', profile_user, name='profile'),

    path(
        'attach/account/logout/', 
        auth_views.LogoutView.as_view(
            template_name='registration/logged_out.html',
            extra_context={'next_page': settings.LOGOUT_REDIRECT_URL}
        ), 
        name='logout_user'
    ),
    path(
        'account/logout/', 
        auth_views.LogoutView.as_view(
            template_name='registration/logged_out.html',
            extra_context={'next_page': settings.LOGOUT_REDIRECT_URL}
        ),
        name='logout_user'
    ),
]
