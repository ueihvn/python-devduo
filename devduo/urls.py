from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('users', views.UserListEngine.as_view()),
    path('users/<int:pk>', views.UserDetailEngine.as_view()),
    path('technologies', views.technology_list),
    path('fields', views.field_list),
    path('mentors', views.MentorListEngine.as_view()),
    path('mentors/search', views.MentorSearch.as_view()),
    path('mentors/filter', views.MentorFilter.as_view()),
    path('mentors/<int:pk>', views.MentorDetailEngine.as_view()),
    path('bookings', views.CreateBookingEngine.as_view()),
    path('bookings/filter', views.BookingFilter.as_view()),
    path('bookings/<int:pk>', views.BookingDetailEngine.as_view()),
    path('<int:user_id>/bookings/mentor', views.get_user_mentor),
    path('<int:user_id>/bookings/mentee', views.get_user_mentee),
    path('login', views.LoginEngine.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/$', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
