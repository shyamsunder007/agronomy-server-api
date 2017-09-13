from django.conf.urls import patterns, include, url
from django.contrib import admin

from restapp import views

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

       url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^users/', views.UserList.as_view()),

  url(r'^villages/(?P<pk>[0-9]+)/$', views.VillageDetail.as_view()),   
    url(r'^villages/', views.VillageList.as_view()),
  
    url(r'^household/(?P<pk>[0-9]+)/$', views.HouseHoldDetail.as_view()),   
    url(r'^household/', views.HouseholdsList.as_view()),
 
 url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),   
    url(r'^person/', views.PersonList.as_view()),
  
  url(r'^farm/(?P<pk>[0-9]+)/$', views.FarmDetail.as_view()),   
    url(r'^farm/', views.FarmList.as_view()),
  
  url(r'^points/(?P<pk>[0-9]+)/$', views.PointsDetail.as_view()),   
    url(r'^points/', views.PointsList.as_view()),
  
  url(r'^well/(?P<pk>[0-9]+)/$', views.WellDetail.as_view()),   
    url(r'^well/', views.WellList.as_view()),
  
  url(r'^wateryield/(?P<pk>[0-9]+)/$', views.WateryieldDetail.as_view()),   
    url(r'^wateryield/', views.WateryieldList.as_view()),
  
   
  ]