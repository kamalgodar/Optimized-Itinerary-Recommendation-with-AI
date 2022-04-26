from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )

class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','username','password')
        extra_kwargs = {'password':{'write_only':True}}

    def update(self,instance,validated_data):
        user = User.objects.get(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user 

