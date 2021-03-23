#APIS for this app will go here

from django.contrib.auth.models import User, Group
from rest_framework import serializers

#This is the user serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

#This is the group serializer
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']