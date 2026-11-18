from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .forms import AlbumForm
from .models import Album


class AlbumListView(ListView):
    model = Album
    context_object_name = 'album_list'  # Default: object_list
    template_name = 'album-list.html'  # Default: album_list.html


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'single_album'  # Default: album
    template_name = 'album-detail.html'  # Default: album_detail.html


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album-create.html'  # Default: album_form.html
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumDeleteView(DeleteView):
    model = Album
    context_object_name = 'single_album'  # Default: album
    template_name = 'album-delete.html'  # Default: album_confirm_delete.html
    success_url = reverse_lazy('album-list')
