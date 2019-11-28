"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url

from blog import views

urlpatterns = [

path('home/', views.home_view, name='home'),
path('admin/', admin.site.urls),
path('search/', views.browse_view, name='browse'),
path('lod/', views.lod_view, name='lod'),
path('ltama/', views.ltama_view, name='ltama'),
url(r'^item/(?P<id>\d+)/$', views.item_view, name="item"),
path('about/', views.about_view, name='about'),
path('essays/', views.essays_view, name='essays'),
path('planets/', views.planets_view, name='planets'),
path('using/', views.using_view, name='using'),
path('spaces1/', views.spaces_view, name='spaces1'),
path('amabib/', views.amabib_view, name='amabib'),
path('lincolnthornton/', views.lincolnthornton_view, name='lincolnthornton'),
path('isumbras/', views.isumbras_view, name='isumbras'),
path('ltoctavian/', views.ltoctavian_view, name='ltoctavian'),
path('ltisumbras/', views.ltisumbras_view, name='ltisumbras'),
path('perils/', views.perils_view, name='perils'),
path('ltdegravant/', views.ltdegravant_view, name='ltdegravant'),
path('news/', views.news_view, name='news'),

path('d3sparql-barchart/', views.barchart_view, name='d3sparql-barchart'),
path('d3sparql-piechart/', views.piechart_view, name='d3sparql-piechart'),
path('d3sparql-sankey/', views.sankey_view, name='d3sparql-sankey'),
path('d3sparql-roundtree/', views.roundtree_view, name='d3sparql-roundtree'),
]
