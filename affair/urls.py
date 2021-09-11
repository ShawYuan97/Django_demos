from django.urls import path

from . import views

urlpatterns = [
    path('index', views.affair_index_view),
    path('submit_file', views.submit_View),
    path('down_file', views.downfile_View),
    path('downfile/<int:id>', views.downonefile),
]
