from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')


def Home2(request):
    return render(request, 'index-2.html')


def Courses(request):
    return render(request, 'courses.html')


def Course_Details(request):
    return render(request, 'course-details.html')

def About_Us(request):
    return render(request, 'about-us.html')

def Instructors(request):
    return render(request, 'instructors.html')

def Instructor_Details(request):
    return render(request, 'instructor-details.html')

def Events(request):
    return render(request, 'events.html')

def Events_Details(request):
    return render(request, 'events-details.html')

def Login(request):
    return render(request, 'login.html')

def Registration(request):
    return render(request, 'registration.html')

def Error404(request):
    return render(request, '404.html')

def Contact(request):
    return render(request,  'contact.html')

def Shop(request):
    return render(request, 'shop.html')

def Shop_Details(request):
    return render(request, 'shop-details.html')

def Blog(request):
    return render(request, 'blog.html')

def Blog_Details(request):
    return render(request, 'blog-details.html')