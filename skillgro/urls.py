"""
URL configuration for skillgro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('index-2.html', views.Home2, name='index-2.htmls'),
    path('courses.html', views.Courses, name='courses.html'),
    path('course-details.html', views.Course_Details, name='course-details.html'),
    path('about-us.html', views.About_Us, name='about-us.html'),
    path('instructors.html', views.Instructors , name='instructors.html'),
    path('instructor-details.html', views.Instructor_Details, name='instructor-details.html'),
    path('events.html', views.Events, name='events.html'),
    path('events-details.html', views.Events_Details , name='events-details.html'),
    path('login.html', views.Login, name='login.html'), 
    path('registration.html', views.Registration, name='registration.html'),
    path('404.html', views.Error404, name='404.html'),
    path('contact.html', views.Contact, name='contact.html'),
    path('shop.html', views.Shop, name='shop,html'),
    path('shop-details.html', views.Shop_Details, name='shop-details.html'),
    path('blog.html', views.Blog, name='blog.html'), 
    path('blog-details.html', views.Blog_Details, name='blog-details.html')
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
