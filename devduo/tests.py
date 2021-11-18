from django.test import TestCase
from devduo.crud import custom_sql, filterUserMentorMentee, get_mentor_booking_infor, getMentorResponse

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

# init data in database


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
        {
            "user_name": "hoanglong040800",
            "email": "hoanglong040800@gmail.com",
            "image": "https://lh3.googleusercontent.com/a-/AOh14GiXJAU-PAHfIdxF9CvAOjzf8GA-fTpQhg1ObGzhaw=s96-c",
            "password": "password",
            "gg_id": "1371",
            "money": 1000
        },
        {
            "user_name": "u18520093",
            "email": "18520093@gm.uit.edu.vn",
            "image": "https://lh3.googleusercontent.com/a-/AOh14GgdTpsjVBfrdospm3eqFdiDIEy-JeT78PfDDfDQ=s96-c",
            "password": "password",
            "gg_id": "2372",
            "money": 1000
        },
    ]

    mentorsCreateParam = [
        {
            "user_id": 1,
            "contacts": {
                "facebook": "http://linkfb.com",
            },
            "full_name": "Tho Bay Mau",
            "thumbnail": "https://i.ytimg.com/vi/IBaPZ4lELvI/maxresdefault.jpg",
            "price": 10
        },
        {
            "user_id": 2,
            "contacts": {
                "facebook": "http://linkfb.vn",
            },
            "full_name": "ReactJS account",
            "thumbnail": "https://codelearn.io/Upload/Blog/react-js-co-ban-phan-1-63738082145.3856.jpg",
            "price": 5
        }
    ]

    # init fileds data
    fields = []
    for i in range(len(field_names)):
        f = Field.objects.create(
            name=field_names[i]
        )
        fields.append(f)

    # init technologies data
    technologies = []
    for i in range(len(technology_names)):
        t = Technology.objects.create(
            name=technology_names[i]
        )
        technologies.append(t)

    # init users data
    users = []
    for i in range(len(usersCreateParam)):
        u = User.objects.create(
            user_name=usersCreateParam[i]["user_name"],
            email=usersCreateParam[i]["email"],
            password=usersCreateParam[i]["password"],
            gg_id=usersCreateParam[i]["gg_id"],
            image=usersCreateParam[i]["image"],
            money=usersCreateParam[i]["money"]
        )
        users.append(u)

    # init mentors data
    mentors = []
    for i in range(len(mentorsCreateParam)):
        mentor = Mentor.objects.create(
            user=users[mentorsCreateParam[i]["user_id"]-1],
            contacts=mentorsCreateParam[i]["contacts"],
            price=mentorsCreateParam[i]["price"],
            full_name=mentorsCreateParam[i]["full_name"],
            thumbnail=mentorsCreateParam[i]["thumbnail"]
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
            "mentee": 1,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc)
        }
    ]

    # init booking data
    bookings = []
    for i in range(len(bookingsCreateParam)):
        booking = Booking.objects.create(
            mentor=mentors[bookingsCreateParam[i]["mentor"]-1],
            mentee=users[bookingsCreateParam[i]["mentee"]-1],
            duration=bookingsCreateParam[i]["duration"],
            time_start=bookingsCreateParam[i]["time_start"]
        )
    bookings.append(booking)


InitData()

# getMentorResponse(1)
# bookings = filterUserMentorMentee(0, 'mentor')
# print(len(bookings))
# print(bookings)

# res = get_mentor_booking_infor(2, 'ongoing')
# print(res[0])
