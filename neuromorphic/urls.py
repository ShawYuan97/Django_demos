from django.urls import path
from login.base import checkLogin

from . import views

urlpatterns = [
    path('index', checkLogin(views.index_View)),
    path('simulation', checkLogin(views.neuronsimu_View)),

]
