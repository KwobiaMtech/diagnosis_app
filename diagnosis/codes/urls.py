from django.conf.urls import url
from django.urls import path
from .views import CodeListViewSet, FileUpload

urlpatterns = [
    path('', FileUpload.as_view(), name='upload'),
    path('upload/', FileUpload.as_view(), name='upload'),
    # API ROUTES
    url(r'^codes$', CodeListViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),

    url(r'^codes/all$', CodeListViewSet.as_view(
        {
            'get': 'list',
        }
    )),

]
