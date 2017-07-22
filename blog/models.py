from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 用户模型
class User(AbstractUser):
    #     #null：
    #     If True, Django will store empty values as NULL in the database. Default
    # is False.
    #     如果为True，空值将会被存储为NULL，默认为False。
    # blank：
    #     If True, the field is allowed to be blank. Default is False.
    #     如果为True，字段允许为空，默认不允许。
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True,
                               null=True, verbose_name="用户头像")

    qq = models.CharField(max_length=20, verbose_name='qq')
    # unique  =true 不能出现相同的内容，否则会出异常
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='电话号码')

    class Meta:
        # verbose_name的意思很简单，就是给你的模型类起一个更可读的名字：
        # verbose_name = "pizza"
        # verbose_name_plural
        # 这个选项是指定，模型的复数形式是什么，比如：
        # verbose_name_plural = "stories"
        # 如果不指定Django会自动在模型名称后加一个’s’
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # ordering=['order_date'] # 按订单升序排列
        # ordering=['-order_date'] # 按订单降序排列，-表示降序
        # ordering=['?order_date'] # 随机排序，？表示随机
        ordering = ['-id']

    def __str__(self):
        return self.username


# 标签

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'

        verbose_name_plural = verbose_name

        ordering = [id]

    def __str__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')

    index = models.IntegerField(default=999, verbose_name='显示顺序（从小到大）')

    class Meta:
        verbose_name = '分类'

        verbose_name_plural = verbose_name

        ordering = ['index', 'id']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')

    desc = models.CharField(max_length=50, verbose_name='文章描述')

    content = models.TextField(verbose_name='文章内容')

    click_count = models.IntegerField(default=0, verbose_name='点击次数')

    is_recommend = models.BooleanField(default=True, verbose_name='是否推荐')

    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间'
                                        )
