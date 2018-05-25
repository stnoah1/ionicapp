from django.conf.urls import url

from praise.api import views

urlpatterns = [
    url(r'^$', views.PraiseListView.as_view(), name='praise-list'),
]

urlpatterns_user = [
    url(r'^$', views.PraiseHistoryListView.as_view(), name='main'),
]