from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction
from decimal import Decimal
from devduo.crud import filterUserMentorMentee
from .serializers import CreateBookingSerializer, CreateUpdateMentorSerializer, FieldSearializer, GetBookingSerializer, GetMentorSerializer, PatchBookingStatusSerializer, PatchMentorStatusSerializer, TechnologySearializer, UserSerializer
from .models import Booking, Mentor, Technology, User, Field
from .filters import MentorFilter


# users
# api view -> working with function based view
@api_view(['GET', 'POST'])
def user_list(request):
    # List all user, or create new user
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def user_detail(request, pk):
    # Retrieve, update or delete a user
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# technology
@api_view(['GET'])
def technology_list(request):
    # List all technology
    technologies = Technology.objects.all()
    serializer = TechnologySearializer(technologies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# field
@api_view(['GET'])
def field_list(request):
    # List all technology
    fields = Field.objects.all()
    serializer = FieldSearializer(fields, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def mentor_list(request):
    # List all user, or create new user
    if request.method == 'GET':
        mentors = Mentor.objects.all()
        serializer = GetMentorSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CreateUpdateMentorSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)
                return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def mentor_detail(request, pk):
    # Retrieve, update or delete a user
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GetMentorSerializer(mentor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CreateUpdateMentorSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PatchMentorStatusSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mentor.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class MentorSearch(generics.ListAPIView):
    search_fields = ['full_name', 'description']
    filter_backends = [filters.SearchFilter]
    queryset = Mentor.objects.all()

    serializer_class = GetMentorSerializer


@api_view(['POST'])
@transaction.atomic
def create_booking(request):
    serializer = CreateBookingSerializer(data=request.data)
    if serializer.is_valid():
        try:
            total_price = Decimal(serializer.validated_data.get('total_price'))
            mentor = serializer.validated_data.get('mentor')
            mentee = serializer.validated_data.get('mentee')
            mentor_user = User.objects.get(pk=mentor.user.id)

            # mentee = User.objects.get(pk=mentee_id)
            # mentor = Mentor.objects.get(pk=mentor_id)
            if mentor.status != True:
                return Response({"message": "cannot book mentor status false"}, status=status.HTTP_400_BAD_REQUEST)
            mentee.money = mentee.money - total_price
            mentor_user.money = mentor_user.money + total_price
            mentor.status = False

            serializer.save()
            mentor.save()
            mentor_user.save()
            mentee.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e.__class__, e.__cause__)
            return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH'])
def booking_detail(request, pk):
    # Retrieve, update or delete a user
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GetBookingSerializer(booking)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PatchBookingStatusSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_mentor(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)
    bookings = filterUserMentorMentee(user_id, 'mentee')
    serializer = GetBookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_mentee(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)
    bookings = filterUserMentorMentee(user_id, 'mentor')
    serializer = GetBookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class MentorFilter(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = GetMentorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MentorFilter
