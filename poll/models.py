from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

class University(models.Model):
    name = models.CharField(max_length=50)
    domen = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Institute(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='institutes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='specializations')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'


class Teacher(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.surname)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Course(models.Model):
    year = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True, related_name='courses')
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Group(models.Model):
    name = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='groups')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(maxlength=30)
    surname = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
def __str__(self):
    return '{} {} {}'.format(self.firstname, self.lastname, self.surname)

class Meta:
    verbose_name = 'Student'
    verbose_name_plural = 'Students'
class Question(models.Model):
    text_field = models.CharField(max_length=50)
def __str__(self):
    return self.text_field

class Meta:
    verbose_name = 'Question'
    verbose_name_plural = 'Questions'
class TeacherLectureAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teacher_lecture_assessments')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_lecture_assessments')
    informative = GenericRelation(Rating)
    actuality = GenericRelation(Rating)
def __str__(self):
    return '{} {} {}'.format(self.teacher.firstname, self.teacher.lastname, self.teacher.surname)

class Meta:
    verbose_name = 'Teacher Lecture Assessment'
    verbose_name_plural = 'Teacher Lecture Assessments'
