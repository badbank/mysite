from django.db import models
from django.utils import timezone
import datetime

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

RARITY_CHOICE = (
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
    pub_date = models.DateField()

    def __str__(self):
        return self.name

    def is_normal(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(years=2)


class Card(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField()
    job = models.IntegerField(choices=JOB_CHOICE)
    rarity = models.IntegerField(choices=RARITY_CHOICE)
    effect = models.CharField(max_length=800)
    explanation = models.CharField(max_length=800, null=True)
    pub_version = models.ForeignKey(Version, on_delete=models.CASCADE)

    @property
    def real_type(self):
        return type(self).__name__

    def __str__(self):
        return self.name

    @staticmethod
    def all_cards():
        all_minions = list(Minion.objects.all())
        all_magics = list(Magic.objects.all())
        all_dks = list(Dk.objects.all())
        all_weapons = list(Weapon.objects.all())
        all_cards = all_minions + all_magics + all_dks + all_weapons
        return all_cards

    class Meta:
        abstract = True


class Minion(Card):
    attack = models.IntegerField()
    health = models.IntegerField()
    type = models.IntegerField(choices=MINION_TYPE_CHOICE)


class Magic(Card):
    pass


class Weapon(Card):
    attack = models.IntegerField()
    durability = models.IntegerField(default=1)


class Dk(Card):
    skill_name = models.CharField(max_length=50)
    skill_cost = models.IntegerField(null=True)
    skill = models.CharField(max_length=400)
