from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from devduo.crud import filterUserMentorMentee
from .serializers import CreateBookingSerializer, CreateUpdateMentorSerializer, FieldSearializer, GetBookingSerializer, GetMentorSerializer, PatchBookingStatusSerializer, TechnologySearializer, UserSerializer
from .models import Booking, Mentor, Technology, User, Field


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
        serializer = CreateUpdateMentorSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mentor.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_booking(request):
    serializer = CreateBookingSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            print(e.__class__, e.__cause__)
            return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)

        print(serializer.data)
        print(serializer.data.get("mentor"))
        print(serializer.data.get("mentee"))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
