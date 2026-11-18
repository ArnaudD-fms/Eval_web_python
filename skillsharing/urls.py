from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'skillsharing'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("help_requests/", views.HelpRequestListView.as_view(), name="help_requests"),
    path(
        "help_request/add/",
        views.HelpRequestCreateView.as_view(),
        name="add_help_request",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name='skillsharing/login.html',
            next_page="skillsharing:index"
        ),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="skillsharing:index"
        ),
        name="logout"
    )
]
