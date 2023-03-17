from django.core.paginator import Paginator


def paginator(request, items, items_on_page):
    paginator = Paginator(items, items_on_page)
    page_number = request.GET.get('page')

    return paginator.get_page(page_number)
