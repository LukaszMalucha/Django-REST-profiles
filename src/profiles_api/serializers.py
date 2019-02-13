from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """"Serializes a name field for APIView Testing"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}  ## make sure it's not readable

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            name=validated_data['name'],
            email=validated_data['email']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'status_text', 'created_on')
        # Allow to create feed for own profile only
        extra_kwargs = {'user_profile': {'read_only': True}}
