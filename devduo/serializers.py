from re import T
from rest_framework import serializers

from devduo.crud import get_mentor_booking_infor

from .models import Booking, Field, Mentor, Rating, Technology, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'gg_id', 'email', 'user_name', 'image', 'money']


class PatchUserMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['money']


class PutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['gg_id', 'email', 'user_name', 'image', 'password']


class TechnologySearializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class FieldSearializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class CreateUpdateMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'


class UpdateMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        exclude = ['user']


class PatchMentorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['status']


class GetMentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    technologies = TechnologySearializer(many=True, read_only=True)
    fields = FieldSearializer(many=True, read_only=True)
    bookings = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        fields = '__all__'

    def get_bookings(self, obj):
        ogs = get_mentor_booking_infor(obj.user.id, 'ongoing')
        fis = get_mentor_booking_infor(obj.user.id, 'finish')
        bookings = {
            'total_ongoing': ogs,
            'total_finish': fis,
        }
        return bookings


class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'mentor', 'mentee', 'duration',
                  'status', 'time_start', 'total_price']


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
    is_rating = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'

    def get_is_rating(self, obj):
        rating = Rating.objects.filter(booking=obj.id)
        return len(rating) != 0


class PatchBookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CreateRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'booking', 'rating', 'comment']


class UpdateRatingSerializer(serializers.ModelSerializer):
    booking = GetBookingSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'rating', 'comment', 'booking']


class RatingSerializer(serializers.ModelSerializer):
    booking = GetBookingSerializer()

    class Meta:
        model = Rating
        fields = ['id', 'booking', 'rating', 'comment']
