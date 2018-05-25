from django.conf.urls import url

from user.api import views

urlpatterns = [
    url(r'^$', views.user_create_view, name='user-create'),
    url(r'^(?P<token>.*)/$', views.user_detail_view, name='user-detail'),
]
