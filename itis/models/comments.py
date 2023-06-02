from django.db import models


class Comments(models.Model):
    '''
    A mechanism for recording history or detail deemed important for an occurrence(s) of
    Taxonomic Units.

    comment_id: The unique identifier for remarks associated with an occurrence of Taxonomic Units.
    commentator: The name of the person associated with the comment being provided with regard to an occurrence of Taxonomic Units.
    comment_detail: Remarks providing additional information regarding an occurrence of Taxonomic Units.
    comment_time_stamp: The date and time at which a comment associated with an occurrence of Taxonomic Units is entered.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    comment_id = models.IntegerField(primary_key=True)
    commentator = models.CharField(max_length=100)
    comment_detail = models.CharField(max_length=2000)
    comment_time_stamp = models.DateTimeField()
    update_date = models.DateField()

    class Meta:
        db_table = 'comments'
