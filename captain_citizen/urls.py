from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('help_requests', views.HelpRequestList.as_view(), name='help_request_list'),
    path('help_requests/<int:pk>', views.HelpRequestDetail.as_view(), name='help_request_detail')
]