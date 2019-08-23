import django_filters
from .models import Product

COLL_CHOICES = (
    (0, 'Art 8: Alliterative Morte Arthur'),
    (1, 'Art 10: Octavian'),
    (2, 'Art 11: Isumbras'),
    (3, 'Art 15: Sir Degreuant'),
)

class ProductFilter(django_filters.FilterSet):
    Collection = django_filters.MultipleChoiceFilter(choices=COLL_CHOICES)


    class Meta:
        model = Product
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['Collection']
