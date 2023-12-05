from django.db import models
from core.choices import *

class Subject(models.Model):
    title = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=10, unique=True)
    # max_marks = models.PositiveIntegerField(default=100)
    # min_mark = models.PositiveIntegerField(default=40)
    # mark_obtained = models.PositiveIntegerField(default=0, null=True)
    # grade = models.CharField(max_length=10, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    # def grading_system(self):
    #     """
    #     Calculate and set the grade based on the value of mark_obtained.
    #     """
    #     if not self.mark_obtained:
    #         return

    #     if self.mark_obtained >= 90:
    #         self.grade = 'A+'
    #     elif 70 <= self.mark_obtained < 90:
    #         self.grade = 'A'
    #     elif 60 <= self.mark_obtained < 70:
    #         # self.mark_obtained is between 60-69
    #         self.grade = 'B'
    #     elif 50 <= self.mark_obtained < 60:
    #         # self.mark_obtained is between 50-59
    #         self.grade = 'C'
    #     elif 40 <= self.mark_obtained < 50:
    #         # self.mark_obtained is between 40-59
    #         self.grade = 'D'
    #     else:
    #         # self.mark_obtained is less than 40
    #         self.grade = 'FAILED'
