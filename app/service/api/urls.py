from django.conf.urls import url, include

from service.api import views

urlpatterns = [
    url(r'^token$', views.token_retrieve_view, name='token-retrieve'),
    url(r'^users/', include('user.api.urls', namespace='user')),
]
