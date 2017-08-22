from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

# format_suffix_patterns allows urls to be appended with suffixes
# indicating type of content requested (e.g. .json, .html, etc)
urlpatterns = format_suffix_patterns([
    # ex: /
    url(r'^$', views.api_root),
    # ex: /snippets/
    url(r'^snippets/$', 
        views.SnippetList.as_view(),
        name='snippet-list'),

    # ex: /snippets/[pk]
    url(r'^snippets/(?P<pk>[0-9]+)/$', 
        views.SnippetDetail.as_view(),
        name='snippet-detail'),

    # ex: /snippets/[pk]/highlight/
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),

    # ex: /users/
    url(r'^users/$', 
        views.UserList.as_view(),
        name='user-list'),

    # ex: /users/[pk]
    url(r'^users/(?P<pk>[0-9]+)/$', 
        views.UserDetail.as_view(),
        name='user-detail'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]