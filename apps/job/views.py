from django.shortcuts import render
from django.http import JsonResponse

from job import models
# Create your views here.

def dbtojson(request):
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))

    getdata = models.job51.objects.values('id','job','jobaddress','date','wages','jobname','joburl','jobtxt')
    all_page =int(getdata.count())/limit
    remain_page = int(getdata.count())%limit
    if remain_page > 0:
        all_page+=1

    start_page = (page -1)*limit
    end_page = start_page +limit
    #print('start',start_page,'endpage',end_page)

    tmp = {"code":0,"msg":"","count":getdata.count(),"data":list(getdata[start_page:end_page])}
    return JsonResponse(tmp, safe=False)


def index(request):
    return render(request,'jobtable.html')

def search(request):
    if request.method == 'POST':
        search_data = request.POST.get('input')
        select_data = request.POST.get('select')
        print(search_data,select_data)
        return render(request,'message.html')