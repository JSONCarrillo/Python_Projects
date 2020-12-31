from django.db import models


# djangoClasses class
class djangoClasses(models.Model):
    # title, course_number, instructor_name, duration create inputs
    title = models.CharField(max_length=40)
    course_Number = models.PositiveIntegerField(default=0)
    instructor_Name = models.CharField(max_length=40)
    duration = models.FloatField(default=0.0)

    objects = models.Manager()

    # Changes object name from Object to the title of the object
    def __str__(self):
        return self.title
