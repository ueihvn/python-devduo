
from django.db import connection
from devduo.models import Booking, Mentor


def getMentorResponse(id):
    mentor = Mentor.objects.get(pk=id)
    print(mentor.id)
    return mentor


def custom_sql():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT distinct id FROM devduo_booking WHERE mentor_id = %s and status = %s", [1, 'pending'])
        row = dictfetchall(cursor)

    print(row)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def filterUserMentorMentee(id, type):
    booking = []
    if type == 'mentor':
        booking = Booking.objects.filter(mentor=id)
    elif type == 'mentee':
        booking = Booking.objects.filter(mentee=id)
    return booking
