from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from .filter import ProductFilter

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "Morrois/home.html", {})

def lod_view(request,*args, **kwargs):
    return render(request, "Morrois/lod.html", {})

def browse_view(request,*args,**kwargs):

    f = ProductFilter(request.GET, queryset=Product.objects.all())

    return render(request, 'Morrois/search.html', {'filter': f})

def item_view(request, id):
    instance = get_object_or_404(Product, id=id)
    context={ "instance": instance}
    return render(request, "Morrois/ItemDetail.html", context)


def ltama_view(request,*args, **kwargs):
    return render(request, "Morrois/ltama.html", {})


def about_view(request,*args, **kwargs):
    return render(request, "Morrois/about.html", {})

def essays_view(request,*args, **kwargs):
    return render(request, "Morrois/essays.html", {})

def planets_view(request,*args, **kwargs):
    return render(request, "Morrois/planets.html", {})

def using_view(request,*args, **kwargs):
    return render(request, "Morrois/using.html", {})

def spaces_view(request,*args, **kwargs):
    return render(request, "Morrois/spaces1.html", {})

def amabib_view(request,*args, **kwargs):
    return render(request, "Morrois/amabib.html", {})

def lincolnthornton_view(request,*args, **kwargs):
    return render(request, "Morrois/lincolnthornton.html", {})

def isumbras_view(request,*args, **kwargs):
    return render(request, "Morrois/isumbras.html", {})

def ltoctavian_view(request,*args, **kwargs):
    return render(request, "Morrois/ltoctavian.html", {})

def ltisumbras_view(request,*args, **kwargs):
    return render(request, "Morrois/ltisumbras.html", {})

def perils_view(request,*args, **kwargs):
    return render(request, "Morrois/perils.html", {})

def ltdegravant_view(request,*args, **kwargs):
    return render(request, "Morrois/ltdegravant.html", {})

def news_view(request,*args, **kwargs):
    return render(request, "Morrois/news.html", {})

def barchart_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-barchart.html", {})

def piechart_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-piechart.html", {})

def sankey_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-sankey.html", {})

def roundtree_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-roundtree.html", {})

def treemap_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-treemap.html", {})

def dendrogram_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-dendrogram.html", {})

def sunburst_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-sunburst.html", {})

def treemapzoom_view(request,*args, **kwargs):
    return render(request, "Morrois/d3sparql-treemapzoom.html", {})
