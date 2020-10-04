from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('', about, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio-page/', portfolio_page, name='portfolio-page'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
