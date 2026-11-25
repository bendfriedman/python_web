from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Album
from .forms import AlbumForm


def album_list(request):
    all_albums = Album.objects.all()
    context = {'album_list': all_albums}
    return render(request, 'album-list.html', context)


def album_detail(request, pk):
    single_album = Album.objects.get(id=pk)
    context = {'single_album': single_album}
    return render(request, 'album-detail.html', context)

@login_required
def album_create(request):

    if request.method == 'POST':
        # fill the Django form with the submitted data
        form = AlbumForm(request.POST)

        if form.is_valid():
            new_album = form.save(commit=False)   # build the object, don't save yet
            new_album.user = request.user
            new_album.save()
            return redirect('album-detail', pk=new_album.pk)

        # Invalid: fall through to render() below, and the form shows its errors

    else:
        # GET: the page is opened for the first time, so show an empty form
        form = AlbumForm()

    return render(request, 'album-create.html', {'form': form})