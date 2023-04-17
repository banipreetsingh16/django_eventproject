"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import CreateNewUser,ListUser,LoginUser,LogoutUser,PassNew,Profile
from events.views import RegisterEvent,EventSearch,EventJoin, LeaveEvent, Report
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'register_event', RegisterEvent, basename='register_event')
router.register(r'search_event', EventSearch, basename='search_event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user', CreateNewUser.as_view()),
    path('list_user', ListUser.as_view()),
    path('login_user', LoginUser.as_view()),
    path('logout_user', LogoutUser.as_view()),
    path('join_event/<int:pk>', EventJoin.as_view()),
    path('new_pass', PassNew.as_view()),
    path('leave_event/<int:pk>', LeaveEvent.as_view()),
    path('report_event', LeaveEvent.as_view()),
    path('profile', Profile.as_view()),
    path('report', Report.as_view()),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += router.urls
