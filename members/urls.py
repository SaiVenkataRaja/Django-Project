# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.members, name='members'),        # matches /members/
#     path('<int:id>/', views.details, name='details'), # matches /members/1/
#     path('members/', views.members, name='members')

# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_members, name='all_members'),  # this matches /members/
    path('<int:id>/', views.member_details, name='member_details'),  # this matches /members/1/
]
