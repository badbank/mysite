from django.db import models
from django.utils import timezone
import datetime

RARITY_CHOICE = (
    (1, '基本'),
    (2, '普通'),
    (3, '稀有'),
    (4, '史诗'),
    (5, '传说'),
    (6, '衍生')
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
    ordering = models.IntegerField()

    def __str__(self):
        return self.name

    def is_normal(self):
        if timezone.localdate() >= self.pub_date >= timezone.localdate() - datetime.timedelta(days=730):
            return '标准'
        elif timezone.localdate() < self.pub_date:
            return '新版本预览'
        else:
            return '狂野'


class Job(models.Model):
    name = models.CharField(max_length=100, verbose_name='职业名称')
    color = models.CharField(max_length=100, verbose_name='职业颜色')

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=50, verbose_name='卡牌名称')
    cost = models.IntegerField(verbose_name='卡牌费用')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='所属职业')
    rarity = models.IntegerField(choices=RARITY_CHOICE, verbose_name='卡牌稀有度')
    effect = models.CharField(max_length=800, verbose_name='卡牌效果')
    explanation = models.CharField(max_length=800, null=True, verbose_name='卡牌背景描述')
    pub_version = models.ForeignKey(Version, on_delete=models.CASCADE, verbose_name='公布版本')

    @property
    def real_type_name(self):
        return type(self).__name__

    @property
    def real_rarity_name(self):
        if self.rarity == 1:
            return 'basic'
        elif self.rarity == 2:
            return 'normal'
        elif self.rarity == 3:
            return 'rare'
        elif self.rarity == 4:
            return 'epic'
        elif self.rarity == 5:
            return 'legendary'
        else:
            return 'derived'

    def __str__(self):
        return self.name

    @staticmethod
    def all_cards():
        all_minions = list(Minion.objects.all())
        all_magics = list(Spell.objects.all())
        all_heroes = list(Hero.objects.all())
        all_weapons = list(Weapon.objects.all())
        all_skills = list(Skill.objects.all())
        all_cards = all_minions + all_magics + all_heroes + all_weapons + all_skills
        return all_cards

    class Meta:
        abstract = True

    def is_normal(self):
        if timezone.localdate() >= self.pub_version.pub_date >= timezone.localdate() - datetime.timedelta(days=730):
            return '标准'
        elif timezone.localdate() < self.pub_version.pub_date:
            return '新版本预览'
        else:
            return '狂野'


class Minion(Card):
    attack = models.IntegerField(verbose_name='攻击力')
    health = models.IntegerField(default=1, verbose_name='生命值')
    type = models.IntegerField(choices=MINION_TYPE_CHOICE, verbose_name='类型')


class Spell(Card):
    pass


class Weapon(Card):
    attack = models.IntegerField(verbose_name='攻击力')
    durability = models.IntegerField(default=1, verbose_name='耐久度')


class Hero(Card):
    armor = models.IntegerField(verbose_name='护甲值')
    skill_name = models.CharField(max_length=50, verbose_name='英雄技能名称')
    skill_cost = models.IntegerField(verbose_name='技能费用（-1为被动英雄技能）', null=True)
    skill = models.CharField(max_length=400, verbose_name='英雄技能效果')


class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name='英雄技能名称')
    cost = models.IntegerField(verbose_name='技能费用（-1为被动英雄技能）')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='所属职业')
    effect = models.CharField(max_length=800, verbose_name='英雄技能效果')
    rarity = (6, '衍生')
    pub_version = models.ForeignKey(Version, on_delete=models.CASCADE, verbose_name='公布版本')

    @property
    def real_rarity_name(self):
        return 'derived'

    def __str__(self):
        return self.name

    @property
    def real_type_name(self):
        return type(self).__name__
