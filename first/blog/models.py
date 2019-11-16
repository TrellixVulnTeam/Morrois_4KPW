from django.db import models
COLL_CHOICES = (
    ('Alliterative Morte Arthur', 'Art 8: Alliterative Morte Arthur'),
    ('Octavian', 'Art 10: Octavian'),
    ('Isumbras', 'Art 11: Isumbras'),
    ('Sir Degreuant', 'Art 15: Sir Degreuant'),
)

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    Middle = models.TextField()
    Modern_English = models.TextField()
    Quote = models.TextField()
    Line_Number = models.TextField(default="This is cool!")
    Contributor = models.TextField(default="Contributor")
    Notes = models.TextField(default="Notes")
    Language = models.TextField(default="")
    Tags1 = models.TextField(default="")
    Tags2 = models.TextField(default="")
    Tags3 = models.TextField(default="")
    Tags4 = models.TextField(default="")
    TGNID = models.TextField(default="")
    TGNURL = models.TextField(default="")

    Collection = models.CharField(max_length = 50, choices=COLL_CHOICES, default='Alliterative Morte Arthur')


    def get_absolute_url(self):
        return "/item/%s" %(self.id)
