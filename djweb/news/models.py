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

    def __self__(self):
        return self.title
