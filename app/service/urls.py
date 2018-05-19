from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from service import views

urlpatterns = [
    url(r'^$', login_required(views.home), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^praise/', include('praise.urls', namespace='praise')),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^api/', include('service.api.urls', namespace='api')),
]
