from django.db import models

# Create your models here.
class job51(models.Model):
    job = models.CharField(max_length=256,verbose_name=u"名称")
    company = models.CharField(max_length=512,verbose_name=u"公司")
    address = models.CharField(max_length=512,verbose_name=u"地址")
    wages = models.CharField(max_length=256,verbose_name=u"薪资")
    date = models.CharField(max_length=256,verbose_name=u"发布日期")
    jobname = models.CharField(max_length=256,verbose_name=u"职位类别")
    joburl = models.CharField(max_length=512,verbose_name=u"链接")
    jobtxt = models.CharField(max_length=512,blank = True,verbose_name=u"岗位职责")
    jobaddress = models.CharField(max_length=256,blank = True,verbose_name=u"上班地点")
    class Meta:
        verbose_name = u"51job数据表"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}{1}'.format(self.job,self.date)