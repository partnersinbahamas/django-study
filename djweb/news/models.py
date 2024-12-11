from django.db import models

# Create your table models for Data Base here.

# To create this model in DB you need to make migration
# to create migrations file use => python manage.py makemigrations

# To run migrations run python manage.py migrate
class Article(models.Model):
    title = models.CharField('Name', max_length=50)
    desctiption = models.CharField('Desctiption', max_length=250)
    text = models.TextField('State')
    date = models.DateTimeField('Date')

    """
    __self__
    used to provide a string representation of a model object
    and when displaying model objects in the Django admin panel
    """
    def __str__(self):
        return self.title
    
    class Meta:
        # to see rigth names in admin
        verbose_name = "Article"
        verbose_name_plural = "Articles"
