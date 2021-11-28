
from devduo.models import Field, Mentor, Technology, User, Booking, Rating
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
            "gg_id": "1234",
            "email": "hoanglong040800@gmail.com",
            "user_name": "Long Tran",
            "image": "https://lh3.googleusercontent.com/a-/AOh14GiXJAU-PAHfIdxF9CvAOjzf8GA-fTpQhg1ObGzhaw=s96-c",
            "money": 1000
        },

        {
            "gg_id": "4321",
            "email": "18520093@gm.uit.edu.vn",
            "user_name": "ReactJS Mastery",
            "image": "https://codelearn.io/Upload/Blog/react-js-co-ban-phan-1-63738082145.3856.jpg",
            "money": 500
        },

        {
            "gg_id": "4321",
            "email": "user3@gmail.com",
            "user_name": "Bill Gates",
            "image": "https://vcdn-vnexpress.vnecdn.net/2021/05/17/c63e9e030f06b15d6f90eb4e7a8131-8418-7213-1621222868.jpg",
            "money": 500
        },

        {
            "gg_id": "4321",
            "email": "user4@gmail.com",
            "user_name": "Elon Musk",
            "image": "https://vnn-imgs-a1.vgcloud.vn/icdn.dantri.com.vn/2021/06/14/elon-muskgetty-1623687014239.jpg",
            "money": 500
        },

        {
            "gg_id": "4321",
            "email": "user5@gmail.com",
            "user_name": "Jeff Bezos",
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_%2839074799225%29_%28cropped%29.jpg",
            "money": 500
        },

        {
            "gg_id": "4321",
            "email": "user6@gmail.com",
            "user_name": "Mark Zuckerberg",
            "image": "https://vnn-imgs-a1.vgcloud.vn/icdn.dantri.com.vn/2021/07/15/mark-zuckerberg-1626347263236.jpg",
            "money": 500
        }
    ]

    mentorsCreateParam = [
        {
            "user_id": 1,
            "contacts": {
                "email": "joedoe@gmail.com",
                "github": "https://github.com/joedoe",
                "website": "https://joedoe.com",
                "facebook": "https://facebook.com/?profile.id=123",
                "linkedin": "https://linkedin.com/joedoe"
            },
            "full_name": "Long Tran",
            "thumbnail": "https://lh3.googleusercontent.com/a-/AOh14GiXJAU-PAHfIdxF9CvAOjzf8GA-fTpQhg1ObGzhaw=s96-c",
            "price": 100
        },
        {
            "user_id": 2,
            "contacts": {
                "github": "https://github.com/somebody",
                "website": "https://somebodywebsite.com",
                "facebook": "https://fb.com/somebody",
                "linkedin": "https://linkedin.com/somebody"
            },
            "full_name": "ReactJS Mastery",
            "thumbnail": "https://codelearn.io/Upload/Blog/react-js-co-ban-phan-1-63738082145.3856.jpg",
            "price": 5
        },
        {
            "user_id": 3,
            "contacts": {
                "github": "https://github.com/somebody",
                "website": "https://somebodywebsite.com",
                "facebook": "https://fb.com/somebody",
                "linkedin": "https://linkedin.com/somebody"
            },
            "full_name": "Bill Gates",
            "thumbnail": "https://vcdn-vnexpress.vnecdn.net/2021/05/17/c63e9e030f06b15d6f90eb4e7a8131-8418-7213-1621222868.jpg",
            "price": 250
        },
        {
            "user_id": 4,
            "contacts": {
                "github": "https://github.com/somebody",
                "website": "https://somebodywebsite.com",
                "facebook": "https://fb.com/somebody",
                "linkedin": "https://linkedin.com/somebody"
            },
            "full_name": "Elon Musk",
            "thumbnail": "https://vnn-imgs-a1.vgcloud.vn/icdn.dantri.com.vn/2021/06/14/elon-muskgetty-1623687014239.jpg",
            "price": 50
        },
        {
            "user_id": 5,
            "contacts": {
                "github": "https://github.com/somebody",
                "website": "https://somebodywebsite.com",
                "facebook": "https://fb.com/somebody",
                "linkedin": "https://linkedin.com/somebody"
            },
            "full_name": "Jeff Bezos",
            "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_%2839074799225%29_%28cropped%29.jpg",
            "price": 150
        },
        {
            "user_id": 6,
            "contacts": {
                "github": "https://github.com/somebody",
                "website": "https://somebodywebsite.com",
                "facebook": "https://fb.com/somebody",
                "linkedin": "https://linkedin.com/somebody"
            },
            "full_name": "Mark Zuckerberge",
            "thumbnail": "https://vnn-imgs-a1.vgcloud.vn/icdn.dantri.com.vn/2021/07/15/mark-zuckerberg-1626347263236.jpg",
            "price": 250
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
            # password=usersCreateParam[i]["password"],
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

        mentor.fields.add(fields[i % len(fields)], fields[(
            i+1) % len(fields)], fields[(i+2) % len(fields)])
        mentor.technologies.add(
            technologies[i % len(technologies)], technologies[(i+1) % len(technologies)], technologies[(i+2) % len(technologies)])
        mentors.append(mentor)

    bookingsCreateParam = [
        {
            "mentor": 1,
            "mentee": 2,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "ongoing"
        },
        {
            "mentor": 3,
            "mentee": 4,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "ongoing"
        },
        {
            "mentor": 5,
            "mentee": 6,
            "duration": 3,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "ongoing"
        },
        {
            "mentor": 1,
            "mentee": 6,
            "duration": 1,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "ongoing"
        },
        {
            "mentor": 2,
            "mentee": 4,
            "duration": 3,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "finish"
        },
        {
            "mentor": 5,
            "mentee": 6,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "finish"
        },
        {
            "mentor": 1,
            "mentee": 5,
            "duration": 3,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "finish"
        },
        {
            "mentor": 4,
            "mentee": 6,
            "duration": 2,
            "time_start": datetime.now(tz=timezone.utc),
            "status": "finish"
        },
    ]

    # init booking data
    bookings = []
    for i in range(len(bookingsCreateParam)):
        if bookingsCreateParam[i]["status"] != None:
            booking = Booking.objects.create(
                mentor=mentors[bookingsCreateParam[i]["mentor"]-1],
                mentee=users[bookingsCreateParam[i]["mentee"]-1],
                duration=bookingsCreateParam[i]["duration"],
                time_start=bookingsCreateParam[i]["time_start"],
                status=bookingsCreateParam[i]["status"],
            )
            bookings.append(booking)
        else:
            booking = Booking.objects.create(
                mentor=mentors[bookingsCreateParam[i]["mentor"]-1],
                mentee=users[bookingsCreateParam[i]["mentee"]-1],
                duration=bookingsCreateParam[i]["duration"],
                time_start=bookingsCreateParam[i]["time_start"]
            )
            bookings.append(booking)

    # init rating data
    ratingCreateParam = [
        {
            "booking": 5,
            "rating": 1,
            "comment": "ko duoc ti nao"
        },
        {
            "booking": 6,
            "rating": 4,
            "comment": "day co tam"
        },
        {
            "booking": 7,
            "rating": 5,
            "comment": "qua tuyet voi"
        },
        {
            "booking": 8,
            "rating": 3,
            "comment": "tam duoc"
        },
    ]
    ratings = []
    for i in range(len(ratingCreateParam)):
        rating = Rating.objects.create(
            booking=bookings[ratingCreateParam[i]["booking"]-1],
            rating=ratingCreateParam[i]["rating"],
            comment=ratingCreateParam[i]["comment"],
        )
        ratings.append(rating)


InitData()

# getMentorResponse(1)
# bookings = filterUserMentorMentee(0, 'mentor')
# print(len(bookings))
# print(bookings)

# res = get_mentor_booking_infor(2, 'ongoing')
# print(res[0])

# ratings = Rating.objects.order_by(
#     '-id').filter(booking__mentor=1)
# print(ratings)
