from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Section(models.Model):
    Department_Choices = [
        ("CS", "Computer Science"),
        ("EE", "Electrical Engineering"),
    ]
    name = models.CharField(max_length=4, unique=True,null=False, default='0000')
    department = models.CharField(
        max_length=30, choices=Department_Choices, null=False, default='None')

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Section"


class Student(models.Model):
    Major_Choices = [
        ("CS", "Computer Science"),
        ("SE", "Software Engineering"),
        ("AI", "Artificial Intelligence"),
        ("CYS", "Cyber Security"),
        ("EE", "Electrical Engineering"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student')
    nuid = models.CharField(max_length=4, unique=True,
                            null=False, default='0000')
    batch = models.CharField(max_length=2, null=False, default='00')
    major = models.CharField(
        max_length=30, choices=Major_Choices, null=False, default='None')
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="students")

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Course(models.Model):
    name = models.CharField(max_length=30, unique=True,
                            null=False, default='None')
    course_id = models.CharField(
        primary_key=True, max_length=6, blank=False, null=False)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Faculty(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="faculty")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="faculty")

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('schedule', 'Schedule'),
        ('complete', 'Complete'),
        ('in_progress', 'In Progress'),
    ]
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="appointments")
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='submitted')

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('in_progress', 'In Progress'),
        ('pending', 'Pending'),
    ]
    SERVICE_CHOICES = [
        ('change_withdrawal', 'Course Withdrawal'),
        ('change_section', 'Change Section'),
        ('change_course', 'Change Course'),
        ('tuition_fees', 'Tuition Fees'),
    ]
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="tickets")
    issues_explanation = models.TextField()
    service = models.CharField(
        max_length=30, choices=SERVICE_CHOICES, null=False, default='None')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='submitted')

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


class Notification(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    notification_content = models.TextField()
    status = models.CharField(max_length=10)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"


class Report(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reports")
    ReportContent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"