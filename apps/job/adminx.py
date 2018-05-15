from xadmin import views
from job.models import job51
from xadmin.sites import site
# Register your models here.

class Job51Admin(object):
    refresh_times = [10,20,50]
    list_filter =['job','company','jobaddress','date','wages','joburl']
    search_fields =['date','jobaddress']
    list_display = ['job','company','jobaddress','date','wages','joburl']
    model_icon = 'fa fa-home fa-fw'
    ordering = ['-date']

site.register(job51,Job51Admin)

#添加主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
site.register(views.BaseAdminView, BaseSetting)


#修改头文件及脚本显示
class GlobalSetting(object):
    site_title = "喻晓生后台管理系统"
    site_footer = "http://daydayup11.cn"
    menu_style = "accordion"
site.register(views.CommAdminView, GlobalSetting)




