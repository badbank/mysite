from django.db import models

JOB_CHOICE = (
    (1, '法师'),
    (2, '猎人'),
    (3, '战士'),
    (4, '萨满祭司'),
    (5, '德鲁伊'),
    (6, '牧师'),
    (7, '潜行者'),
    (8, '圣骑士'),
    (9, '术士'),
    (10, '污手党（猎人、战士、圣骑士）'),
    (11, '暗金教（法师、牧师、术士）'),
    (12, '青莲帮（萨满祭司、德鲁伊、潜行者）'),
    (13, '中立'),
    (14, '衍生')
)

AMOUNT_CHOICE = (
    (1, '基本（无色）'),
    (2, '普通（白色）'),
    (3, '稀有（蓝色)'),
    (4, '史诗（紫色）'),
    (5, '传说（橙色）'),
    (6, '衍生（无色）')
)

MINION_TYPE_CHOICE = (
    (1, '无'),
    (2, '野兽'),
    (3, '恶魔'),
    (4, '元素'),
    (5, '龙'),
    (6, '鱼人'),
    (7, '机械'),
    (8, '海盗'),
    (9, '图腾'),
    (10, '全部')
)


class Version(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


class Minion(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField('cost')
    job = models.CharField(max_length=50, choices=JOB_CHOICE)
    amount = models.CharField(max_length=30, choices=AMOUNT_CHOICE)
    others = models.CharField(max_length=800)
    attact = models.IntegerField('attact')
    health = models.IntegerField('health')


class Magic(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField('cost')
    others = models.CharField(max_length=800)
    job = models.CharField(max_length=10, choices=JOB_CHOICE)
    amount = models.CharField(max_length=30, choices=AMOUNT_CHOICE)


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField('cost')
    others = models.CharField(max_length=800)
    job = models.CharField(max_length=10, choices=JOB_CHOICE)
    amount = models.CharField(max_length=30, choices=AMOUNT_CHOICE)
    attact = models.IntegerField('attact')
    times = models.IntegerField('times you can use')


class Dk(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField('cost')
    others = models.CharField(max_length=800)
    job = models.CharField(max_length=10, choices=JOB_CHOICE)
    amount = models.CharField(max_length=30, choices=AMOUNT_CHOICE)
    ablity_name = models.CharField(max_length=50)
    ablity_cost = models.IntegerField('ability cost')
    ablity = models.CharField(max_length=400)
