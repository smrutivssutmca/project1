from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),
    url(r'^register_user$', views.register_user, name='register_user'),
    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^change_password$', views.change_password, name='change_password'),
    url(r'^create_checkin$', views.create_checkin, name='create_checkin'),
    url(r'^save_checkin$', views.save_checkin, name='save_checkin'),
    url(r'^get_checkin$', views.get_checkin, name='get_checkin'),
    url(r'^delete_checkin/(?P<pk>.*)$', views.delete_checkin, name='delete_checkin'),
    url(r'^edit_checkin$', views.edit_checkin, name='edit_checkin'),
    url(r'^edit_re/(?P<pk>.*)$', views.edit_re, name='edit_re'),
]