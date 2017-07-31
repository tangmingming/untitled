from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = 'snippet'

urlpatterns = [
    url(r'^list', views.list, name="list"),
    url(r'^detail/(?P<pk>[0-9]+)', views.detail, name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)