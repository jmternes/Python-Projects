from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=True, blank=True, default=None)

    object = models.Manager()

    def __str__(self):
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campuses"