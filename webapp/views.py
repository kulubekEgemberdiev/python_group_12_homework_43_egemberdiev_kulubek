from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, "index.html")


def first_view(request):
    return render(request, "first_page.html")


def second_view(request):
    return render(request, "second_page.html")


def third_view(request):
    return render(request, "third_page.html")
