from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=1000)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

class Project(models.Model):
    TECHNOLOGY=(
        ('Android','Android'),
        ('iOS','iOS'),
        ('Java','Java'),
        ('.Net','.Net'),
        ('Angular','Angular'),
        ('PHP','PHP'),
        ('Tableau','Tableau'),
        ('Power BI','Power BI'),
        ('Selenium','Selenium'),
        ('AWS','AWS'),
        ('Azure','Azure'),
        ('Python','Python'),
        ('Tensorflow','Tensorflow')
    )
    ROLE=(
        ('Digital Services','Digital Services'),
        ('Analytics','Analytics'),
        ('Java','Java'),
        ('QA','QA'),
        ('MS Tech','MS Tech'),
        ('BA','BA'),
        ('UI/UX','UI/UX')
    )
    STATUS=(
        ('NEW','NEW'),
        ('IN PROGRESS','IN PROGRESS'),
        ('COMPLETED','COMPLETED'),
        ('CANCELLED','CANCELLED')
    )
    #ProjectId=models.IntegerField(primary_key=True)
    ProjectName =models.CharField(max_length=20,unique=True)
    ProjectStatus=models.CharField(max_length=50,choices=STATUS)
    Department=models.CharField(max_length=50,choices=ROLE)
    ClientName=models.CharField(max_length=10,null=False)
    # Country = models.CountryField(MULTIPLE=True)
    Technology=models.CharField(max_length=50, choices=TECHNOLOGY)
    StartDate=models.DateField()
    EndDate=models.DateField()
    EstimatedHours=models.IntegerField()