from django.shortcuts import render, get_object_or_404
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

favorite = False
def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums, }  # Information that this template (index.html) needs in order to work
    return render(request, 'music/index.html', context)  # this function returns valid HttpResponse
    # return HttpResponse(template.render(context, request))


def detail(request, album_id):
    # isntead of album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    # gets something from album class and checks it for 404

    return render(request, 'music/detail.html', {'album': album})
    # You can also pass the dictionary file as is

def favorite(request):

    return HttpResponse('')