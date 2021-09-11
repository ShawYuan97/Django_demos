from django.db import models


# Create your models here.

class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(
        auto_now_add=True)  # auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。 auto_now_add为添加时的时间，更新对象时不会有变动。
    has_confirmed = models.BooleanField(default=False)  # 邮件注册认证

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-create_time']  # 按照创建时间反向排序 优先展示最近的
        verbose_name = '用户'
        verbose_name_plural = '用户'


# 邮件验证模型类
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
