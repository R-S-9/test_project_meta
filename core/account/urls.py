from django.urls import path

from .create_user.resource import Registration
from .activate.resource import ActivateUser
from .login.resource import Login


urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('activate/<str:uuid>', ActivateUser.as_view(), name='activate'),
    path('login/', Login.as_view(), name='login'),
]
