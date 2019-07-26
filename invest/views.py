from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Invest, Column
from django.views.decorators.csrf import csrf_exempt
import json

def invest_list(request):
    invest_list = Invest.objects.all()
    column_list = Column.objects.all()
    return render(request, 'invest/invest_list.html', {'invest_list': invest_list, 'column_list': column_list})

@csrf_exempt
def invest_new(request):
        Invest.objects.all().delete()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for b in body:
            Invest(
                team = b.get('team'),
                cat = b.get('cat'),
                lev3 = b.get('lev3'),
                lev4 = b.get('lev4'),
                col_A = b.get('col_A'),
                col_B = b.get('col_B'),
                col_C = b.get('col_C'),
                col_D = b.get('col_D'),
                col_E = b.get('col_E'),
                col_F = b.get('col_F'),
                col_G = b.get('col_G'),
                col_H = b.get('col_H'),
                col_I = b.get('col_I'),
                col_J = b.get('col_J'),
                col_K = b.get('col_K'),
                col_L = b.get('col_L'),
                col_M = b.get('col_M'),
                col_N = b.get('col_N'),
                col_O = b.get('col_O')
            ).save()
            print(str(b))
        return HttpResponse(body)

@csrf_exempt
def invest_new_column(request):
        Column.objects.all().delete()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for b in body:
            #Invest(
                #team = b.get('team'),
            #).save()
            print(str(b))
        return HttpResponse(body)