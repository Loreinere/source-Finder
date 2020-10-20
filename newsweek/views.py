from django.shortcuts import render

posts = [
    {
        'author'        : "Caroline Matusiak",
        'title'         : 'My Boyfriend',
        'content'       : 'My first public',
        'date_posted'   : '28 July 2020'
    },
    {
        'author'        : "Camile Rolbiecki",
        'title'         : 'My Girlfriend',
        'content'       : 'My second public',
        'date_posted'   : '29 July 2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'newsweek/home.html', context)

def about(request):
    return render(request, 'newsweek/about.html', {'title': 'About'})

# Create your views here.
