
import re
from django.db import connection
from devduo.models import Booking, Mentor


def getMentorResponse(id):
    mentor = Mentor.objects.get(pk=id)
    print(mentor.id)
    return mentor


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def custom_sql():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT distinct id FROM devduo_booking WHERE mentor_id = %s and status = %s", [2, 'ongoing'])
        row = dictfetchall(cursor)

    return(row)


def get_mentor_booking_infor(mentorid, status):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT distinct mentor_id, COUNT(id) as total 
            FROM devduo_booking 
            where mentor_id = %s and status = %s
            GROUP BY mentor_id 
            """, [mentorid, status])
        row = dictfetchall(cursor)
    if len(row) == 0:
        return 0
    elif len(row) == 1:
        return row[0]['total']


def filterUserMentorMentee(id, type):
    booking = []
    if type == 'mentor':
        booking = Booking.objects.filter(mentor=id)
    elif type == 'mentee':
        booking = Booking.objects.filter(mentee=id)
    return booking
