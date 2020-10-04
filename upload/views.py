from django.shortcuts import render

def upload(request):
    return render(request, 'upload/upload.html',
                 {'section': 'publications'})


# Create your views here.
