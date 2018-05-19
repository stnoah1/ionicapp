from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from user import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    # url(r'^logout/$', login_required(logout_view), name='member_logout'),
]
