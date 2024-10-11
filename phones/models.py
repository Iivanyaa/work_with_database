from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace(' ', '-'))
        super().save(*args, **kwargs)
