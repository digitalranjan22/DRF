from rest_framework import serializers
class StudentSerial(serializers.Serializer):
    name = serializers.CharField(max_length=1000)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)



