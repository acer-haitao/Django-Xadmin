from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
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
        #文本输入信息
        search_data = request.POST.get('input')
        #select自动选择信息
        select_data = request.POST.get('select')

        #address, company, date, id, job, jobaddress, jobname, jobtxt, joburl, wages
        if search_data:
            if select_data == "date":
                getdata = models.job51.objects.filter(Q(date__startswith=search_data)).values().order_by('-date')
                return render(request, 'search.html', {'getdata': getdata})
            elif select_data == "address":
                getdata = models.job51.objects.filter(Q(address__startswith=search_data)).values().order_by('-date')
                return render(request, 'search.html', {'getdata': getdata})
            elif select_data == "job":
                getdata = models.job51.objects.filter(Q(job__contains=search_data)).values().order_by('-date')
                return render(request, 'search.html', {'getdata': getdata})
            elif select_data == "wages":
                getdata = models.job51.objects.filter(Q(wages__contains=search_data)).values().order_by('-date')
                return render(request, 'search.html', {'getdata': getdata})
            elif select_data == "jobname":
                getdata = models.job51.objects.filter(Q(jobname__contains=search_data)).values().order_by('-date')
                return render(request, 'search.html', {'getdata': getdata})
            elif select_data == "company":
                getdata = models.job51.objects.filter(Q(company__contains=search_data)).values().order_by('-date')
                return render(request, 'search.html', {'getdata': getdata})
        else:
            err_msg = "查找失败,请检查输入是否正确！"
            return render(request,'search.html',{"err_msg":err_msg})
    err_msg = "查找失败,请检查输入是否正确！"
    return render(request,'search.html',{"err_msg":err_msg})