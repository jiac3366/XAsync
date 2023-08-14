from djongo import models


class Person(models.Model):
    _id = models.ObjectIdField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    school = models.CharField(max_length=30)
    is_archived = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime"]
