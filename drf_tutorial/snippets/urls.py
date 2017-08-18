from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    #ex: /snippets/
    url(r'^snippets/$', views.SnippetList.as_view()),

    #ex /snippets/[pk]
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
