from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """"Serializes a name field for APIView Testing"""

    name = serializers.CharField(max_length=10)

