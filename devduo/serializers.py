from rest_framework import serializers

from devduo.crud import get_mentor_booking_infor

from .models import Booking, Field, Mentor, Technology, User


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
            'bookings': {
                'total_ongoing': ogs,
                'total_finish': fis,
            }
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

    class Meta:
        model = Booking
        fields = '__all__'


class PatchBookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
