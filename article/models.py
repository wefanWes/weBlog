#-*- coding:utf-8 –*-
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    # content = models.TextField(blank = True, null = True)
    content = RichTextUploadingField ()

    def __unicode__(self) :
        return self.title

#获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    class Meta:
        ordering = ['-date_time']