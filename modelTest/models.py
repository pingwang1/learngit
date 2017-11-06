#encoding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name = '作者'
		verbose_name_plural = verbose_name
	def __unicode__(self):
		return self.name

class AuthorInfo(models.Model):
	sex = models.CharField(max_length=20)
	email = models.EmailField()
	address = models.CharField(max_length=50)
	birthday = models.DateField()
	author = models.OneToOneField(Author)

	class Meta:
		verbose_name = '作者信息'
		verbose_name_plural = verbose_name
	def __unicode__(self):
		return ''

class Publisher(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	province = models.CharField(max_length=20)
	website = models.CharField(max_length=50)

	class Meta:
		verbose_name = '出版社'
		verbose_name_plural = verbose_name
	def __unicode__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=20)
	publish_data = models.DateField()
	author = models.ForeignKey(Author)
	publish = models.ManyToManyField(Publisher)

	class Meta:
		verbose_name = '图书'
		verbose_name_plural = verbose_name
	def __unicode__(self):
		return self.name