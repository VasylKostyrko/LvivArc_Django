from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('obj/<int:id>/', views.arc_object, name='arc_object'),
    path('list/<int:id>/', views.list_objects, name='list_objects'),
    path('404/', views.error404, name='error404'),
]
