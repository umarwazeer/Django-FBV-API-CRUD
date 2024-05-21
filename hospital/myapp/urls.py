from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_ulr, name="api_ulr"),
    path('text/', views.text, name="text"),
    path('get_all/', views.get_all, name="get_all"),
    path('get_data/<int:id>/', views.get_data, name="get_data"),
    path('post_data/', views.post_data, name="post_data"),
    path('update_task/<int:id>/', views.update_task, name="update_task"),
    path('delete_task/<int:_id>/', views.delete_task, name="delete_task"),
    path('patch/<int:id>/', views.patch, name="patch_data")
]
