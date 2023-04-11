from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=50)
    domen = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Institute(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=50)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Teacher(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.surname)
class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Course(models.Model):
    year = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)
    subjects = models.ManyToManyField(Subject)
    def __str__(self):
        return str(self.year)
class Group(models.Model):
    name = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.surname)

class Question(models.Model):
    textField = models.CharField(max_length=50)
    def __str__(self):
        return self.textField
class TeacherLectureAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    informative = GenericRelation(Rating)
    actuality = GenericRelation(Rating)

    def __str__(self):
        return '{} {} {}'.format(self.teacher.firstname, self.teacher.lastname, self.teacher.surname)

