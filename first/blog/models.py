from django.db import models
COLL_CHOICES = (
    (0, 'Art 8: Alliterative Morte Arthur'),
    (1, 'Art 10: Octavian'),
    (2, 'Art 11: Isumbras'),
    (3, 'Art 15: Sir Degreuant'),
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

    Collection = models.IntegerField(choices=COLL_CHOICES, default=0)


    def get_absolute_url(self):
        return "/item/%s" %(self.id)
