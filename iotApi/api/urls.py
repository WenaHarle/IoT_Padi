from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ShowAll, name='data-list'),
    path('detail/<int:pk>/', views.ViewData, name='data-detail'),
    path('day/<int:dayInput>/', views.Viewday, name='data-day'),
    path('create/', views.CreateData, name='data-create'),
    path('update/<int:pk>/', views.updateData, name='data-update'),
    path('delete/<int:pk>/', views.deleteData, name='data-delete'),
    path('data/add/', views.create_data, name='create_data'),
]