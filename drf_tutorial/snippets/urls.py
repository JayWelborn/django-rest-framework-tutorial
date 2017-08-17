from django.conf.urls import url

from snippets import views

urlpatterns = [
    #ex: /snippets/
    url(r'^$', views.snippet_list),

    #ex /snippets/[pk]/
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail)
]
