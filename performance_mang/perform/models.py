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

FEEDBACK_TYPE = (
    ('one', 'Reporting To'),
    ('two', 'Peer-To-Peer'),
    ('three', '360-Degree'),
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



# Add a kra
class KRA(models.Model):
    title = models.CharField(max_length=200)
    desciption = models.TextField(null=True)

    def __str__(self):
        return self.title



# tag kra here
class TagKra(models.Model):
    kra_name = models.ForeignKey(KRA, on_delete=models.CASCADE)
    weightage = models.IntegerField()

    def __str__(self):
        return self.kra_name


# Add Job

class Job(models.Model):
    name = models.CharField(max_length=50, verbose_name='Job Name')
    hours = models.IntegerField()
    start_date = models.DateField(default=datetime.datetime.now)
    end_date = models.DateField(default=datetime.datetime.now)
    desc = models.TextField()

    def __str__(self):
        return self.name



# Add goals
class Goals(models.Model):
    start_date = models.DateField(default=datetime.date.today, verbose_name='Start Date')
    due_date = models.DateField(default=datetime.date.today, verbose_name='Due date')
    goal_name = models.CharField(max_length=100, verbose_name='Goal Name')
    priority = models.CharField(choices=PRIORITY, max_length=10, default=1)
    desciption = models.TextField()
    progress = models.IntegerField()
    assigned_by = models.ForeignKey(Managers, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Staff, on_delete = models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)
    associate_job = models.ManyToManyField(Job, blank=True)

    def __str__(self):
        return self.goal_name



# Add feedback categories
class Feedback_Cateog(models.Model):
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.categories


# Feedback setting
class Feedback_setting(models.Model):
    feed_type = models.CharField(max_length=20, choices=FEEDBACK_TYPE, default='one')
    categories = models.ManyToManyField(Feedback_Cateog, related_name='Categories')

    def __str__(self):
        return self.feed_type


# Give Feedback
class Feedback(models.Model):
    categories = models.ForeignKey(Feedback_Cateog, on_delete=models.CASCADE, null=True)
    feedback_area = models.TextField(verbose_name='Feedback')
    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name



# Add skill
class Skill(models.Model):
    add_skill = models.TextField()

    def __str__(self):
        return self.add_skill


# Tag Skills
class Tag_skill(models.Model):
    domain = models.CharField(max_length=100)
    select_skill = models.ManyToManyField(Skill, related_name='Skills')

    def __str__(self):
        return self.domain

