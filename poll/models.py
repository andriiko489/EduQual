from django.db import models
from star_ratings.models import Rating, AbstractBaseRating


class University(models.Model):
    name = models.CharField(max_length=50, unique=True)
    domain = models.CharField(max_length=50, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name


class Institute(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Institute"
        verbose_name_plural = "Institutes"
        unique_together = ('name', 'university')

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"
        unique_together = ('name', 'institute')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.surname}"


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    type = models.CharField(max_length=20, default="Лекція")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.subject.name


class DaySchedule(models.Model):
    name = models.CharField(max_length=50, blank=True)
    lessons = models.ManyToManyField(Lesson)
    def __str__(self):
        return self.name


class WeekSchedule(models.Model):
    name = models.CharField(max_length=50, blank=True)
    days = models.ManyToManyField(DaySchedule)
    def __str__(self):
        return self.name

class Course(models.Model):
    year = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)
    subjects = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return str(self.year)


class Group(models.Model):
    name = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    schedule = models.ForeignKey(WeekSchedule, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.surname}"


class Question(models.Model):
    textField = models.CharField(max_length=50)

    def __str__(self):
        return self.textField

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class AssessmentField(models.Model):
    question = models.TextField(max_length=100)
    num = models.IntegerField(default=5)
    def __str__(self):
        return f"{self.question}"

class TeacherAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    fields = models.ManyToManyField(AssessmentField)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.text}"
