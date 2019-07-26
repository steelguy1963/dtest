from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Column
from django.views.decorators.csrf import csrf_exempt
import json

def post_list(request):
    post_list = Post.objects.select_related('column').all()
    for p in post_list:
        print(str(p))
    col_list = Column.objects.all()
    #for c in col_list:
    #    print(str(c))
    context1 = {'post_list': post_list}
    context2 = {'col_list': col_list}
    for post in post_list:
        return JsonResponse(
           {'row_id': post.row_id,
            #'column': post.column,
            'value': post.value
           }
            #,json_dumps_params = {'ensure_ascii': True
        )

def post_json(request):
    post_list = Post.objects.select_related('column').all()
    for p in post_list:
        print(str(p))
    col_list = Column.objects.all()
    #for c in col_list:
    #    print(str(c))
    context1 = {'post_list': post_list}
    context2 = {'col_list': col_list}
    return JsonResponse({
        #'row_id': post_list.row_id,
        #'column': post_list.column,
        #'value': post_list.value,
    }, json_dumps_params = {'ensure_ascii': True})

@csrf_exempt
def post_new(request):
        Post.objects.all().delete()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for b in body:
            Post(
                #team = b.get('team'),
            ).save()
            print(str(b))
        return HttpResponse(body)

def post_delete(request):
    return HttpResponse()