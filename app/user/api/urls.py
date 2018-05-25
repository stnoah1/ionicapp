from django.conf.urls import url, include

from praise.api.urls import urlpatterns_user
from user.api import views

urlpatterns = [
    url(r'^$', views.user_create_view, name='user-create'),
    url(r'^self/$', views.user_detail_view, name='user-detail'),
    url(r'^self/praises/', include(urlpatterns_user, namespace='praise')),
]
