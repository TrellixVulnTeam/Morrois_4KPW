import django_filters
from .models import Product
from django import forms

COLL_CHOICES = (
    ('Alliterative Morte Arthur', 'Art 8: Alliterative Morte Arthur'),
    ('Octavian', 'Art 10: Octavian'),
    ('Isumbras', 'Art 11: Isumbras'),
    ('Sir Degreuant', 'Art 15: Sir Degreuant'),
)

TAG1_CHOICES = (
    ('place','Place'),
    ('person','Person'),
    ('thing','Thing'),
)

TAG2_CHOICES = (
    ('animal','animal'),
    ('geogName','geogName'),
    ('good','good'),
    ('imagName','imagName'),
    ('language','language'),
    ('nationality','nationality'),
    ('persName','persName'),
    ('personGrp','personGrp'),
    ('placeName','placeName'),
    ('roleName','roleName'),
    ('transport','transport'),
)

TAG3_CHOICES = (
    ('addName','addName'),
    ('armor','armor'),
    ('country','country'),
    ('currency','currency'),
    ('ecclesiastical','ecclesiastical'),
    ('empire','empire'),
    ('faith','faith'),
    ('food','food'),
    ('geogFeat','geogFeat'),
    ('horse','horse'),
    ('imagName','imagName'),
    ('nationality','nationality'),
    ('political','political'),
    ('region','region'),
    ('roleName','roleName'),
    ('settlement','settlement'),
    ('spoken','spoken'),
    ('street','street'),
    ('textile','textile'),
    ('weapon','weapon'),
    ('written','written'),
)

TAG4_CHOICES = (
    ('beverage','beverage'),
    ('continent','continent'),
    ('faith','faith'),
    ('hill','hill'),
    ('islands','islands'),
    ('lake','lake'),
    ('mountains','mountains'),
    ('peninsula','peninsula'),
    ('planet','planet'),
    ('political','political'),
    ('region','region'),
    ('river','river'),
    ('sea','sea'),
    ('valley','valley'),

)

class ProductFilter(django_filters.FilterSet):
    Collection = django_filters.MultipleChoiceFilter(choices=COLL_CHOICES, widget=forms.CheckboxSelectMultiple)
    Tags1 = django_filters.MultipleChoiceFilter(choices=TAG1_CHOICES, widget=forms.CheckboxSelectMultiple)
    Tags2 = django_filters.MultipleChoiceFilter(choices=TAG2_CHOICES, widget=forms.CheckboxSelectMultiple)
    Tags3 = django_filters.MultipleChoiceFilter(choices=TAG3_CHOICES, widget=forms.CheckboxSelectMultiple)
    Tags4 = django_filters.MultipleChoiceFilter(choices=TAG4_CHOICES, widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Product
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['Collection', 'Tags1', 'Tags2', 'Tags3', 'Tags4']
