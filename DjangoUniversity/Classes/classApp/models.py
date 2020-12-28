from django.db import models

# djangoClasses class
class djangoClasses(models.Model):
    #title, course_number, instructor_name, duration create inputs
    title = models.CharField(max_length=40)
    course_Number = models.PositiveIntegerField(max_length=2)
    instructor_Name = models.CharField(max_length=40)
    duration = models.FloatField(default=0.0)

    objects = models.Manager()

    def __str__(self):
        return self.title