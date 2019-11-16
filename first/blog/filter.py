import django_filters
from .models import Product
from django import forms

COLL_CHOICES = (
    ('Alliterative Morte Arthur', 'Art 8: Alliterative Morte Arthur'),
    ('Octavian', 'Art 10: Octavian'),
    ('Isumbras', 'Art 11: Isumbras'),
    ('Sir Degreuant', 'Art 15: Sir Degreuant'),
)

class ProductFilter(django_filters.FilterSet):
    Collection = django_filters.MultipleChoiceFilter(choices=COLL_CHOICES, widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Product
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['Collection']
