from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_id = models.CharField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')