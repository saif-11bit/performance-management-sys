from django.db import models
import datetime


PRIORITY = (
    (0, 'Low Priority'),
    (1, 'Medium Priority'),
    (2, 'High Priority' ), 
    (3, 'Highest Priority'),
    (4, 'No Priority'),
)

STATUS = (
    (0, 'Pending'),
    (1, 'Completed'),
    (2, 'Overdue' ), 
    (3, 'Delayed'),
)

class Managers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Manager Name')
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):

    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(verbose_name='Mobile Number')
    pan = models.CharField(max_length=15, verbose_name='PAN Number')
    date_joined = models.DateField(default=datetime.date.today, verbose_name="date of joining")
    

    def __str__(self):
        return f"{self.name}"


class KRA(models.Model):
    tag_to = models.ForeignKey(Staff, on_delete=models.CASCADE)
    to_achieve = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_to

class Goals(models.Model):
    start_date = models.DateField(default=datetime.date.today, verbose_name='Start Date')
    due_date = models.DateField(default=datetime.date.today, verbose_name='Due date')
    goal_name = models.CharField(max_length=100, verbose_name='Goal Name')
    priority = models.CharField(choices=PRIORITY, max_length=10, default=1)
    desciption = models.TextField()
    progress = models.CharField(max_length=100)
    assigned_by = models.ForeignKey(Managers, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Staff, on_delete = models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)


    def __str__(self):
        return self.goal_name


class Feedback(models.Model):
    feedback_area = models.TextField(verbose_name='Feedback')
    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name


class Skillset(models.Model):
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.domain

