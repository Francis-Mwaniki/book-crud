from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    # create
    path('new/', views.book_create, name='book_create'),
    # update
    path('<int:pk>/edit/', views.book_update, name='book_update'),
    # delete
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]