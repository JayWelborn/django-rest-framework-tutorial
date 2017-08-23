from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from snippets import views


"""
Registering the viewsets with the router is similar to providing a 
urlpattern. We include two arguments - the URL prefix for the views, and the 
viewset itself.

The DefaultRouter class we're using also automatically creates the API root view
for us, so we can now delete the api_root method from our views module.
"""
# Instantiate new router and register viewsets
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', 
                              namespace='rest_framework'))
]


# This is what it looks like to bind urls explicitly by sending
# dictionary arguments to the as_view method of our View_Sets

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
#     })

# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
#     })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight',
#     },
#     renderer_classes=[renderers.StaticHTMLRenderer]
#     )

# user_list = UserViewSet.as_view({
#     'get': 'list',
#     })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve',
#     })
# 
# urlpatterns = format_suffix_patterns([
#     # ex: /
#     url(r'^$', api_root),

#     # ex: /snippets/
#     url(r'^snippets/$', 
#         snippet_list, 
#         name='snippet-list'),

#     # ex: /snippets/[pk]
#     url(r'^snippets/(?P<pk>[0-9]+)/$', 
#         snippet_detail, 
#         name='snippet-detail'),

#     # ex: /snippets/[pk]/highlight
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', 
#         snippet_highlight, 
#         name='snippet-highlight'),

#     # ex: /users/
#     url(r'^users/$',
#         user_list,
#         name='user-list'),

#     # ex: /users/pk/
#     url(r'users/(?P<pk>[0-9]+)/$',
#         user_detail,
#         name='user-detail'),
#     ])


# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework'))
# ]


# # format_suffix_patterns allows urls to be appended with suffixes
# # indicating type of content requested (e.g. .json, .html, etc)
# urlpatterns = format_suffix_patterns([
#     # ex: /
#     url(r'^$', views.api_root),
#     # ex: /snippets/
#     url(r'^snippets/$', 
#         views.SnippetList.as_view(),
#         name='snippet-list'),

#     # ex: /snippets/[pk]
#     url(r'^snippets/(?P<pk>[0-9]+)/$', 
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),

#     # ex: /snippets/[pk]/highlight/
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),

#     # ex: /users/
#     url(r'^users/$', 
#         views.UserList.as_view(),
#         name='user-list'),

#     # ex: /users/[pk]
#     url(r'^users/(?P<pk>[0-9]+)/$', 
#         views.UserDetail.as_view(),
#         name='user-detail'),
# ])