from django.shortcuts import render
from django.http import HttpResponse  # http response sends back html/basic webpage
from django.http import Http404
from .models import Album, Song

# Create your views here.
'''def index(request):
    all_objects = Album.objects.all()
    html = ''
    for album in all_objects:
        url = "/music/" + str(album.id) + "/"
        html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums, }  # Information that this template (index.html) needs in order to work
    return render(request, 'music/index.html', context)  # this function returns valid HttpResponse
    # return HttpResponse(template.render(context, request))


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
        # ^^^^^^look for album with id written in url, the one they passed
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    return render(request, 'music/detail.html', {'album': album})
    # You can also pass the dictionary file as is