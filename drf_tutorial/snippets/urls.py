from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    #ex: /snippets/
    url(r'^snippets/$', views.snippet_list),

    #ex /snippets/[pk]
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
