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

path('Morrois/', views.home_view, name='Morrois'),
path('Morrois/admin/', admin.site.urls),
path('Morrois/search/', views.browse_view, name='browse'),
path('Morrois/lod/', views.lod_view, name='lod'),
path('Morrois/ltama/', views.ltama_view, name='ltama'),
path('Morrois/item/<str:id>/',views.item_view, name='item'),
#url(r'^item/(?P<id>\d+)/$', views.item_view, name="item"),
path('Morrois/about/', views.about_view, name='about'),
path('Morrois/essays/', views.essays_view, name='essays'),
path('Morrois/planets/', views.planets_view, name='planets'),
path('Morrois/using/', views.using_view, name='using'),
path('Morrois/spaces1/', views.spaces_view, name='spaces1'),
path('Morrois/amabib/', views.amabib_view, name='amabib'),
path('Morrois/lincolnthornton/', views.lincolnthornton_view, name='lincolnthornton'),
path('Morrois/isumbras/', views.isumbras_view, name='isumbras'),
path('Morrois/ltoctavian/', views.ltoctavian_view, name='ltoctavian'),
path('Morrois/ltisumbras/', views.ltisumbras_view, name='ltisumbras'),
path('Morrois/perils/', views.perils_view, name='perils'),
path('Morrois/ltdegravant/', views.ltdegravant_view, name='ltdegravant'),
path('Morrois/news/', views.news_view, name='news'),

path('Morrois/d3sparql-barchart/', views.barchart_view, name='d3sparql-barchart'),
path('Morrois/d3sparql-piechart/', views.piechart_view, name='d3sparql-piechart'),
path('Morrois/d3sparql-sankey/', views.sankey_view, name='d3sparql-sankey'),
path('Morrois/d3sparql-roundtree/', views.roundtree_view, name='d3sparql-roundtree'),
path('Morrois/d3sparql-treemap/', views.treemap_view, name='d3sparql-treemap'),
path('Morrois/d3sparql-dendrogram/', views.dendrogram_view, name='d3sparql-dendrogram'),
path('Morrois/d3sparql-sunburst/', views.sunburst_view, name='d3sparql-sunburst'),
path('Morrois/d3sparql-treemapzoom/', views.treemapzoom_view, name='d3sparql-treemapzoom')
]
