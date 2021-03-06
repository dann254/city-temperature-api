"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.locations import views

router = routers.DefaultRouter()
router.register(r'api/locations', views.LocationsViewSet, basename='locations')
# location_list = views.LocationsViewSet.as_view({'get':'list'})
# location_detail = views.LocationsViewSet.as_view({'get':'retrieve'})

urlpatterns = [
    path('', include(router.urls)),

    #LOCATION URLS
    # path('locations/', location_list, name='locations-list'),
    # path('locations/<str:message>/<int:days>', location_detail, name='locations-detail')
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/locations/', views.LocationsView.as_view(), name="locations")
]
