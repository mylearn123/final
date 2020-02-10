from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Carcustomizations.models import Customerlist
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getter(request):
    if request.method=='GET':
        print(request.method)
        objj=Customerlist.objects.all().values()
        print("your desc is :",objj)
        lists=list(objj)
        dicts={'address':lists}

    # return HttpResponse("hiii")
        return JsonResponse(dicts)
    elif request.method=='POST':
        print("Request body contents => ",request.body)
        print("Request body type =>",type(request.body))
        python_obj =json.loads(request.body)
        print("Request type=>",type(python_obj))
        print(python_obj)
        print(python_obj['name'])
        print(python_obj['address'])
        print(python_obj['title'])


        objj=Customerlist.objects.create(name=python_obj['name'],title=python_obj['title'],address=python_obj['address'],date='2020-12-1')
        o=objj.save()
        # dicts={'name':objj.name,
        #     'title':objj.title,
        #     'address':objj.address,
        #     'date':objj.date}
        return JsonResponse({
            "message":"POST successfully"
        })

    else:
        return HttpResponse("please type anotger mehod")


@csrf_exempt
def getters(request,ID):
    objj=Customerlist.objects.get(Postid=ID)

    if request.method=='GET':
        print(request.method)
        dicts={'payaaaa':objj.name}
     
        return JsonResponse(dicts)
    elif request.method=='DELETE':
        objj.delete()
        return JsonResponse({'deletd':'message'})

    elif request.method=='PUT':
        # updatee=Customerlist.objects.put(Postid=ID)

        obb= json.loads(request.body)
        objj.name=obb['name']
        objj.title=obb['title']
        objj.address=obb['address']
        objj.save()
        # updatee.ots.all()
        # updatee.save
        return JsonResponse({'updated':'message'})

    else:
        return HttpResponse("anotehr")

# @csrf_exempt
# def deleter(request,ID):
#     if request.method=='DELETE':
#         Order = Customerlist.objects.get(Postid=ID)
#         Order.delete()
#         print(Order)
#         return JsonResponse({'message':"Deleted"})



