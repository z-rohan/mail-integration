from django.urls import path
from .views import SendMail
urlpatterns=[
    path('se/',SendMail)

]