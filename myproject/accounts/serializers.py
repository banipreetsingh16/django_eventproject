from rest_framework.serializers import ModelSerializer
from .models import Profile
from django.contrib.auth.models import User

class Userserializer(ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')

    def create(self, validated_data):
        user = super(Userserializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ProfileSerializer(ModelSerializer):
    user = Userserializer(required=True)
    class Meta:
        model = Profile
        fields = ('user', 'age', 'address')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Userserializer.create(Userserializer(), validated_data=user_data)
        profile = Profile.objects.create(user=user,**validated_data)
        return profile