from datetime import datetime
from typing import Tuple
from django.db.models.base import Model
from rest_framework import serializers

from .models import Booking, Field, Mentor, Technology, User
from devduo import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'gg_id', 'email', 'user_name', 'image', 'money')


class TechnologySearializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class FieldSearializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class MentorBookingInforSearializer(serializers.Serializer):
    total_ongoing = serializers.IntegerField()
    total_cancel = serializers.IntegerField()
    total_mentee = serializers.IntegerField()

    class Meta:
        fields = ['total_ongoing', 'total_cancel', 'total_mentee']


class CreateUpdateMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'


class GetMentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    technologies = TechnologySearializer(many=True, read_only=True)
    fields = FieldSearializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        fields = '__all__'


# class GetMentorSerializerTest(serializers.Serializer):
#     mentor = GetMentorSerializer()
#     bookings = MentorBookingInforSearializer()


class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['mentor', 'mentee', 'duration', 'status']


class BookingMenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'user_name', 'image']


class BookingMentorSerialzer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = ['user', 'id', 'full_name', 'thumbnail', 'status']


class GetBookingSerializer(serializers.ModelSerializer):
    mentor = BookingMentorSerialzer(read_only=True)
    mentee = BookingMenteeSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


class PatchBookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']
