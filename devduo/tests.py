from django.test import TestCase

from devduo.models import Field, Mentor, Technology, User, Booking
from datetime import datetime, timezone

# Create your tests here.


def deleteInitData():
    Field.objects.all().delete()
    Technology.objects.all().delete()
    Booking.objects.all().delete()
    Mentor.objects.all().delete()
    User.objects.all().delete()


# deleteInitData()


def InitData():
    field_names = [
        'AI',
        'Blockchain',
        'Big Data',
        'Web',
        'Mobile',
        'IOS'
    ]

    technology_names = [
        'JS',
        'C#',
        'Java',
        'PHP',
        'Ruby',
        'Go'
    ]

    usersCreateParam = [
        {"user_name": "user1", "email": "letronghieu30071@gmail.com",
            "password": "password"},
        {"user_name": "user2", "email": "letronghieu30072@gmail.com",
            "password": "password"},
        {"user_name": "user3", "email": "letronghieu30073@gmail.com",
            "password": "password"},
        {"user_name": "user4", "email": "letronghieu30074@gmail.com",
            "password": "password"},
        {"user_name": "user5", "email": "letronghieu30075@gmail.com",
            "password": "password"},
    ]

    mentorsCreateParam = [
        {
            "user_id": 1,
            "contact": {
                "facebook": "http://linkfb.com",
                "phone": "124312432134"
            },
            "price": 10000
        },
        {
            "user_id": 2,
            "contact": {
                "facebook": "http://linkfb.vn",
                "phone": "11241234"
            },
            "price": 20000
        }
    ]

    fields = []
    for i in range(len(field_names)):
        f = Field.objects.create(
            name=field_names[i]
        )
        fields.append(f)

    technologies = []
    for i in range(len(technology_names)):
        t = Technology.objects.create(
            name=technology_names[i]
        )
        technologies.append(t)

    users = []
    for i in range(len(usersCreateParam)):
        u = User.objects.create(
            user_name=usersCreateParam[i]["user_name"],
            email=usersCreateParam[i]["email"],
            password=usersCreateParam[i]["password"]
        )
        users.append(u)

    mentors = []
    for i in range(len(mentorsCreateParam)):
        mentor = Mentor.objects.create(
            user_id=users[mentorsCreateParam[i]["user_id"]-1],
            contact=mentorsCreateParam[i]["contact"],
            price=mentorsCreateParam[i]["price"]
        )

        mentor.fields.add(fields[i], fields[i+1])
        mentor.technologies.add(technologies[i], technologies[i+1])
        mentors.append(mentor)

    bookingsCreateParam = [
        {
            "mentor": 1,
            "mentee": 2,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc)
        },
        {
            "mentor": 2,
            "mentee": 3,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc)
        }
    ]

    bookings = []
    for i in range(len(bookingsCreateParam)):
        booking = Booking.objects.create(
            mentor=mentors[bookingsCreateParam[i]["mentor"]-1],
            mentee=users[bookingsCreateParam[i]["mentee"]-1],
            duration=bookingsCreateParam[i]["duration"],
            time_start=bookingsCreateParam[i]["time_start"]
        )
    bookings.append(booking)
    print(len(bookings))


InitData()
