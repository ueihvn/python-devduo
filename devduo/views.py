from django.db.models import query
from django.http import HttpResponse
from django_filters.filters import OrderingFilter
from rest_framework.decorators import api_view
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from devduo.crud import filterUserMentorMentee
from .serializers import CreateBookingSerializer, CreateUpdateMentorSerializer, FieldSearializer, GetBookingSerializer, GetMentorSerializer, LoginSerializer, PatchBookingStatusSerializer, PatchMentorStatusSerializer, PatchUserMoneySerializer, PutUserSerializer, TechnologySearializer, UpdateMentorSerializer, UserSerializer
from .models import Booking, Mentor, Technology, User, Field
from .filters import BookingFilterClass, MentorFilter
from devduo import serializers


# users
class UserListEngine(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# api view -> working with function based view


# @api_view(['GET', 'POST'])
# def user_list(request):
#     # List all user, or create new user
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#             except Exception as e:
#                 print(e.__class__, e.__cause__)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailEngine(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    serializer_class = PutUserSerializer

    def put(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PutUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = PatchUserMoneySerializer

    def patch(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatchUserMoneySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def user_detail(request, pk):
#     # Retrieve, update or delete a user
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


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


class MentorListEngine(generics.GenericAPIView):
    serializer_class = GetMentorSerializer
    queryset = Mentor.objects.all()

    def get(self, request, *args, **kwargs):
        mentors = Mentor.objects.all()
        serializer = GetMentorSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer_class = CreateUpdateMentorSerializer

    def post(self, request, *args, **kwargs):
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


# @api_view(['GET', 'POST'])
# def mentor_list(request):
#     # List all user, or create new user
#     if request.method == 'GET':
#         mentors = Mentor.objects.all()
#         serializer = GetMentorSerializer(mentors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateUpdateMentorSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#             except Exception as e:
#                 print(e.__class__, e.__cause__)
#                 return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorDetailEngine(generics.GenericAPIView):
    serializer_class = GetMentorSerializer
    queryset = Mentor.objects.all()

    def get(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            mentor = Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GetMentorSerializer(mentor)
        return Response(serializer.data)

    serializer_class = UpdateMentorSerializer

    def put(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            mentor = Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateMentorSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = PatchMentorStatusSerializer

    def patch(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            mentor = Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatchMentorStatusSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = request.path[request.path.rfind('/') + 1:]
        try:
            mentor = Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        mentor.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def mentor_detail(request, pk):
#     # Retrieve, update or delete a user
#     try:
#         mentor = Mentor.objects.get(pk=pk)
#     except Mentor.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = GetMentorSerializer(mentor)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CreateUpdateMentorSerializer(mentor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = PatchMentorStatusSerializer(mentor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         mentor.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class MentorSearch(generics.ListAPIView):
    search_fields = ['full_name']
    filter_backends = [filters.SearchFilter]
    queryset = Mentor.objects.all()

    serializer_class = GetMentorSerializer


class CreateBookingEngine(generics.GenericAPIView):
    serializer_class = CreateBookingSerializer
    queryset = Booking.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CreateBookingSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # total_price = Decimal(
                #     serializer.validated_data.get('total_price'))
                # mentor = serializer.validated_data.get('mentor')
                # mentee = serializer.validated_data.get('mentee')
                # mentor_user = User.objects.get(pk=mentor.user.id)

                # # mentee = User.objects.get(pk=mentee_id)
                # # mentor = Mentor.objects.get(pk=mentor_id)
                # if mentor.status != True:
                #     return Response({"message": "cannot book mentor status false"}, status=status.HTTP_400_BAD_REQUEST)
                # mentee.money = mentee.money - total_price
                # mentor_user.money = mentor_user.money + total_price
                # mentor.status = False

                serializer.save()
                # mentor.save()
                # mentor_user.save()
                # mentee.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e.__class__, e.__cause__)
                return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @transaction.atomic
# def create_booking(request):
#     serializer = CreateBookingSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             total_price = Decimal(serializer.validated_data.get('total_price'))
#             mentor = serializer.validated_data.get('mentor')
#             mentee = serializer.validated_data.get('mentee')
#             mentor_user = User.objects.get(pk=mentor.user.id)

#             # mentee = User.objects.get(pk=mentee_id)
#             # mentor = Mentor.objects.get(pk=mentor_id)
#             if mentor.status != True:
#                 return Response({"message": "cannot book mentor status false"}, status=status.HTTP_400_BAD_REQUEST)
#             mentee.money = mentee.money - total_price
#             mentor_user.money = mentor_user.money + total_price
#             mentor.status = False

#             serializer.save()
#             mentor.save()
#             mentor_user.save()
#             mentee.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(e.__class__, e.__cause__)
#             return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetailEngine(generics.GenericAPIView):
    serializer_class = GetBookingSerializer
    queryset = Booking.objects.all()

    def patch(self, request, *args, **kwargs):
        number = request.path[request.path.rfind('/') + 1:]
        try:
            booking = Booking.objects.get(pk=int(number))
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatchBookingStatusSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            bookingRes = Booking.objects.get(pk=int(number))
            res = GetBookingSerializer(bookingRes)
            return Response(res.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = GetBookingSerializer

    def get(self, request, *args, **kwargs):
        number = request.path[request.path.rfind('/') + 1:]
        try:
            booking = Booking.objects.get(pk=int(number))
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GetBookingSerializer(booking)
        return Response(serializer.data)


# @api_view(['GET', 'PATCH'])
# def booking_detail(request, pk):
#     # Retrieve, update or delete a user
#     try:
#         booking = Booking.objects.get(pk=pk)
#     except Booking.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = GetBookingSerializer(booking)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = PatchBookingStatusSerializer(booking, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class BookingFilter(generics.ListAPIView):
    queryset = Booking.objects.all().order_by('-id')
    serializer_class = GetBookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookingFilterClass


class LoginEngine(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                email = serializer.validated_data.get("email")
                user = User.objects.get(email=email)
                mentor = Mentor.objects.get(user=user.id)
                data_res = {
                    "mentor_id": mentor.id,
                    "user_id": user.id
                }
                return Response(data_res, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({"message": "user not found with given email"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e.__class__, e.__cause__)
                return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login(request):
#     serializer = LoginSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             email = serializer.validated_data.get("email")
#             user = User.objects.get(email=email)
#             mentor = Mentor.objects.get(user=user.id)
#             data_res = {
#                 "mentor_id": mentor.id,
#                 "user_id": user.id
#             }
#             return Response(data_res, status=status.HTTP_201_CREATED)
#         except User.DoesNotExist:
#             return Response({"message": "user not found with given email"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             print(e.__class__, e.__cause__)
#             return Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
