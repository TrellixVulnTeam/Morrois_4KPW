from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from .filter import ProductFilter

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "home.html", {})

def lod_view(request,*args, **kwargs):
    return render(request, "lod.html", {})

def browse_view(request,*args,**kwargs):

    f = ProductFilter(request.GET, queryset=Product.objects.all())

    return render(request, 'search.html', {'filter': f})

def item_view(request, id):
    instance = get_object_or_404(Product, id=id)
    context={ "instance": instance}
    return render(request, "ItemDetail.html", context)


def ltama_view(request,*args, **kwargs):
    return render(request, "ltama.html", {})


def about_view(request,*args, **kwargs):
    return render(request, "about.html", {})

def essays_view(request,*args, **kwargs):
    return render(request, "essays.html", {})

def planets_view(request,*args, **kwargs):
    return render(request, "planets.html", {})

def using_view(request,*args, **kwargs):
    return render(request, "using.html", {})

def spaces_view(request,*args, **kwargs):
    return render(request, "spaces1.html", {})

def amabib_view(request,*args, **kwargs):
    return render(request, "amabib.html", {})

def lincolnthornton_view(request,*args, **kwargs):
    return render(request, "lincolnthornton.html", {})

def isumbras_view(request,*args, **kwargs):
    return render(request, "isumbras.html", {})

def ltoctavian_view(request,*args, **kwargs):
    return render(request, "ltoctavian.html", {})

def ltisumbras_view(request,*args, **kwargs):
    return render(request, "ltisumbras.html", {})

def perils_view(request,*args, **kwargs):
    return render(request, "perils.html", {})

def ltdegravant_view(request,*args, **kwargs):
    return render(request, "ltdegravant.html", {})

def news_view(request,*args, **kwargs):
    return render(request, "news.html", {})

def d3sparql_view(request,*args, **kwargs):
    return render(request, "d3sparql.html", {})    

def barchart_view(request,*args, **kwargs):
    return render(request, "d3sparql-barchart.html", {})

def piechart_view(request,*args, **kwargs):
    return render(request, "d3sparql-piechart.html", {})

def sankey_view(request,*args, **kwargs):
    return render(request, "d3sparql-sankey.html", {})

def roundtree_view(request,*args, **kwargs):
    return render(request, "d3sparql-roundtree.html", {})

def treemap_view(request,*args, **kwargs):
    return render(request, "d3sparql-treemap.html", {})

def dendrogram_view(request,*args, **kwargs):
    return render(request, "d3sparql-dendrogram.html", {})

def sunburst_view(request,*args, **kwargs):
    return render(request, "d3sparql-sunburst.html", {})

def treemapzoom_view(request,*args, **kwargs):
    return render(request, "d3sparql-treemapzoom.html", {})
