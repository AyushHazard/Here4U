from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from .models import *
from django.contrib.auth import authenticate, login, logout
from rest_framework_jwt.settings import api_settings

class ClientdataSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        # final = User.objects.get(id=user.id)
        validated_data.update({'User':user})
        client = Clientdata.objects.create(**validated_data)
        client.save()
        return client
    class Meta:
        model = Clientdata
        fields = ['Name','Gender','Age','Email','State','City','Marital_Status','Educational_Status']

class CounsellordataSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        # final = User.objects.get(id=user.id)    

        validated_data.update({'User':user})    
        counsellor = Counsellordata.objects.create(**validated_data)
        
        # print(validated_data)    
        # counsellor.User = user
        counsellor.save()
        return counsellor  
        
    class Meta:
        model = Counsellordata
        fields = ['Name','Gender','Age','Profile_pic','Email','State','City','Education','Expertise','Summary','Consultation_start','Consultation_end']

class CounsellordataGETSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Counsellordata
        fields = ['User','Name','Gender','Age','Profile_pic','Email','State','City','Education','Expertise','Summary','Consultation_start','Consultation_end']               

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True) # We also need to make sure the serializer recognizes and stores the submitted password, but doesn’t include it in the returned JSON. So we add the ‘password’ field to fields, but above that also specify that the password should be write only.

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        new_user = authenticate(username=validated_data['username'],password=validated_data['password'])
        request = self.context.get("request")
        login(request, new_user)

        return user

    class Meta:
        model = User
        fields = ['token','username','password']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)




class DescriptionSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        # final = User.objects.get(id=user.id)    

        validated_data.update({'User':user})    
        description = Description.objects.create(**validated_data)
        
        # print(validated_data)    
        # counsellor.User = user
        description.save()
        return description

    class Meta:
        model = Description
        fields = ['Message','extra_data']

class BookingSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        validated_data.update({'client_id':validated_data['client_key'],'counsellor_id':validated_data['counsellor_key']})
        obj = Bookings.objects.create(**validated_data)
        obj.save()
        return obj
    class Meta:
        model = Bookings
        fields =['client_key','counsellor_key','Booking_time']


class ActiveCounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveCounsellor
        fields = ['user','Counsellor','Booking_time']       

class ActiveClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveClient
        fields = '__all__'      

