from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Invest, Column, Email
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import EmailMessage
from django.urls import reverse

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
        return HttpResponse(body)

@csrf_exempt
def invest_new_column(request):
        Column.objects.all().delete()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for b in body:
            Column(
                col_data = b.get('data'),
                col_title = b.get('title'),
                col_show = b.get('show')
            ).save()
        return HttpResponse(body)

@csrf_exempt
def invest_new_email(request):
        invest_list = Invest.objects.all()
        column_list = Column.objects.all()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        to_list = ['sextansgamma@gmail.com']
        to_list.append(body['to'])
        body_new = body['body_text'] + '\n' + '\n' + '다음 링크를 클릭하여 데이터를 입력하시기 바랍니다' + '\n' + 'https://dtest.run.goorm.io/invest/' + '\n'
        email = EmailMessage(body['subject_text'],body_new,to=to_list)
        if(email.send()):
            return HttpResponseRedirect(reverse('invest:invest_list'))
        else:
            print('There was an error sending an email.') 