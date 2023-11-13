from django.http import HttpResponse
from django.shortcuts import render

from sekapp.models import Persons


# Create your views here.


def fun_home(request):
    return HttpResponse("Home - HTTP RESPONSE")


def fun_about(request):
    name = "passName"
    return render(request, "page1.html", {'keyy': name})


def fun_contact(request):
    return HttpResponse("Contacts - HTTP RESPONSE")


def fun_detail(request):
    return render(request, "page2.html")


def fun_thanks(request):
    return HttpResponse("THANKS - HTTP RESPONSE")


def fun_calc(request):
    val1 = int(request.GET['a'])
    val2 = int(request.GET['b'])
    return render(request, "res.html", {'res_add': (val1 + val2),
                                        'res_min': (val1 - val2),
                                        'res_multi': (val1 * val2),
                                        'res_div': (val1 / val2)})


def fun_input(request):
    return render(request, "calc.html")


def fun_index(request):
    obj_main = Persons.objects.all()
    return render(request, "index.html", {'res': obj_main})


