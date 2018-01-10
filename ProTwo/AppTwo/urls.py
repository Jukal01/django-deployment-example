from django.conf.urls import url
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    url(r'^help/$',views.help,name='help'),
    url(r'^user/$',views.user,name='user'),
    url(r'^sign_up/$',views.sign_up,name='signup'),     
]    
