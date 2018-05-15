# _*_ encoding:utf-8 _*_
from message.models import Msg
from xadmin.sites import site

class MsgAdmin(object):
    list_display = ['name','msg_content','msg_email','msg_time']
    search_fileds = ['name','msg_content','msg_email','msg_time']
    list_filter = ['name','msg_content','msg_email','msg_time','msg_sex']
    model_icon = 'fa fa-book fa-fw'

site.register(Msg,MsgAdmin)