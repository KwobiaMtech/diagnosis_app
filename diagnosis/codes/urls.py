from django.conf.urls import url
from django.urls import path
from codes import views
from codes.views import CodeListViewSet

urlpatterns = [
    path('upload/', views.FileUpload.as_view(),name='upload'),

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
