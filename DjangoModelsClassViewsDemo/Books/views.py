from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from .forms import BookForm


# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'  # Default: object_list
    template_name = 'book-list.html'  # Default: book_list.html


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'single_book'  # Default: book
    template_name = 'book-detail.html'  # Default: book_detail.html


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book-create.html'  # Default: book_form.html
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)