from django.shortcuts import render

# Create your views here.
def msg(request):
    if request.method == 'POST':
        # 获取列表分类
        tmp = request.POST.get('type')

        # 获取输入框输入的文本数据--日期、地点等
        data = request.POST.get('content')

        # 密码验证
        pwd = request.POST.get('pwd')
        print(data)

    return render(request,'message.html')