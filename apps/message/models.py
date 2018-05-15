from django.db import models
from datetime import datetime


class Msg(models.Model):
    name = models.CharField(max_length=32,verbose_name=u"姓名")
    msg_time = models.DateTimeField(default=datetime.now,verbose_name=u"时间")
    msg_content = models.TextField(max_length=128,verbose_name=u"留言内容")
    msg_email = models.EmailField(verbose_name=u"邮件")
    msg_title = models.CharField(max_length=32,verbose_name=u"标题")
    msg_sex = models.CharField(max_length=10,choices=(("B",u'男'),("G",u'女')),verbose_name=u'性别')
    class Meta:
        verbose_name = u"留言结构表"
        verbose_name_plural = verbose_name