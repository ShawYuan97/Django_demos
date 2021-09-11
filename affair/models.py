from django.db import models
from login.models import User


# Create your models here.

class Submit_File_Model(models.Model):
    title = models.CharField('标题', max_length=128)
    file = models.FileField('文件', upload_to='uploads/')
    submit_time = models.DateTimeField('提交日期', auto_now_add=True)
    update_time = models.DateTimeField('更新日期', auto_now=True)
    file_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-submit_time']  # 按照创建时间反向排序 优先展示最近的
        verbose_name = '上传文件'
        verbose_name_plural = '上传文件'
