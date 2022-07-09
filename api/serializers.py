from rest_framework import serializers
class StudentSerial(serializers.Serializer):
    name = serializers.CharField(max_length=1000)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
class ProjectSerial(serializers.Serializer):
   
    ProjectName = serializers.CharField(max_length=20)
    ProjectStatus= serializers.CharField(max_length=50)
    Department= serializers.CharField(max_length=50)
    ClientName= serializers.CharField(max_length=10)
    
    Technology= serializers.CharField(max_length=50)
    StartDate= serializers.DateField()
    EndDate= serializers.DateField()
    EstimatedHours= serializers.IntegerField()


