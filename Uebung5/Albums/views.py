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
        # fill form with the submitted data
        form = AlbumForm(request.POST)

        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.user = request.user
            new_album.save()
            return redirect('album-detail', pk=new_album.pk)

    else:
        # GET: page is opened for first time, so show an empty form
        form = AlbumForm()

    return render(request, 'album-create.html', {'form': form})


@login_required
def album_delete(request, pk):
    single_album = Album.objects.get(id=pk)

    if request.method == 'POST':
        Album.objects.filter(id=pk).delete()
        return redirect('album-list')

    # GET: show confirmation page
    return render(request, 'album-delete.html', {'single_album': single_album})