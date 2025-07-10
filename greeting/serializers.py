from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    name = serializers.CharField()
    department = serializers.CharField()
    experience = serializers.IntegerField()