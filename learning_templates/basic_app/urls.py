from django.urls import path
from. import views

app_name='basic_app'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
"""
    path('relative/',views.relative,name='relative'),
    path('other',views.other,name='other'),
    """
