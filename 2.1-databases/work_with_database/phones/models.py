from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    id = models. AutoField(primary_key=True)
    name = models.CharField(max_length= 100, null=False)
    slug = models.SlugField(max_length = 200)
    price = models.IntegerField()
    image = models.CharField(max_length= 254)
    release_date = models.CharField(max_length=10, null=False)
    lte_exists = models.BooleanField()

#   def __str__(self):
 #       return self.title
    def __str__(self):
        return f'{self.id}, {self.name}: {self.slug}'
