from django.urls import path
from . import views

# from django.conf.urls import url


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('signup2/', views.signup2_view, name="signup2"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
