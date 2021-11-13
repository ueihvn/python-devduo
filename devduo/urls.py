from django.urls import path

from devduo.models import Field
from . import views

urlpatterns = [
    path('users', views.user_list),
    path('users/<int:pk>', views.user_detail),
    path('technologies', views.technology_list),
    path('fields', views.field_list),
    path('mentors', views.mentor_list),
    path('mentors/search', views.MentorSearch.as_view()),
    path('mentors/filter', views.MentorFilter.as_view()),
    path('mentors/<int:pk>', views.mentor_detail),
    path('bookings', views.create_booking),
    path('bookings/<int:pk>', views.booking_detail),
    path('<int:user_id>/bookings/mentor', views.get_user_mentor),
    path('<int:user_id>/bookings/mentee', views.get_user_mentee)
]
