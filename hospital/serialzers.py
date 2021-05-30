from rest_framework import serializers

class HospitalSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    established_date=serializers.IntegerField()
    city=serializers.CharField(max_length=20)
    address=serializers.CharField(max_length=100)