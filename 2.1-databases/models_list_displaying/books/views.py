from django.core.paginator import Paginator
from django.shortcuts import render
import datetime
from books.models import Book



def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    context = {'books' : books_objects, }
    return render(request, template, context)


def books_review(request, year, month, day):
    template = 'books/books_review.html'
    page_number = request.GET.get('page')
    date = datetime.date(year, month, day)
    books_obj = Book.objects.all().order_by('pub_date')
    paginator = Paginator(books_obj, 1)
    if page_number is None:
        page_numbers = paginator.num_pages
        for x in range(1, page_numbers + 1):
            page = paginator.get_page(x)
            for p in page:
                if date == p.pub_date:
                    page_number = x
                    break

    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, template, context)

