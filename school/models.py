from django.db import models

#  School Model
class School(models.Model):
    name = models.CharField(max_length=255)  # School name
    number_of_classes = models.IntegerField()  # Total number of classes
    area = models.DecimalField(max_digits=10, decimal_places=2)  # Total area with precision (e.g., 12345.67)

    def __str__(self):
        return self.name

#  Classroom Model
class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")
    name = models.CharField(max_length=255)  # Classroom name
    area = models.DecimalField(max_digits=8, decimal_places=2)  # Area with precision (e.g., 1234.56)

    def __str__(self):
        return f'{self.name} - {self.school.name}'
    
#FloatField in Django can lead to precision issues