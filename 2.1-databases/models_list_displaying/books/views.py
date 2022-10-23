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

    date_next = None
    if page_obj.has_next():
        page_next_number = page_obj.next_page_number()
        page_next = paginator.get_page(page_next_number)[0]
        date_next = page_next.pub_date

    date_pre = None
    if page_obj.has_previous():
        page_pre_number = page_obj.previous_page_number()
        page_pre = paginator.get_page(page_pre_number)[0]
        date_pre = page_pre.pub_date


    context = {'page_obj': page_obj, 'date_pre': date_pre, 'date_next': date_next}
    return render(request, template, context)



