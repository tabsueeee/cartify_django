from django.urls import path

from .import views
app_name = 'messaging'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_message, name='new'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('', views.inbox, name='inbox'),
]
