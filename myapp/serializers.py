

from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=20)
    domicile = serializers.CharField(max_length=100)
    family_name = serializers.CharField(max_length=100)        

    def create(self, validated_data):
        """
        Create and return a new `Author` instance, given the validated data.
        """
        return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Author` instance, given the validated data.
        """
        instance['name'] = validated_data.get('name', instance['name'])
        instance['number'] = validated_data.get('number', instance['number'])
        instance['domicile'] = validated_data.get('domicile', instance['domicile'])
        instance['family_name'] = validated_data.get('family_name', instance['family_name'])
        return instance
    

class BookSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=20)
    price = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)     