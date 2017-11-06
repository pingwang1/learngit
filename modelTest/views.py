#encoding:utf-8
from django.shortcuts import render
import datetime

# Create your views here.
class TestCls(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def show(self):
		return u"%s的年龄是%d,%s"%(self.name,self.age,self.sex)

def show_mes(request):
	testC = TestCls(u"张三",18,u"不知道")
	cont = {"content":testC}
	return render(request,"modelTest/index.html",cont)

def filterTest(request):
	testList = ['qw','agdgsa','QDhs','hsaof']
	dt=datetime.datetime.now()
	return render(request,"modelTest/index.html",{"testList":testList,"dt":dt})