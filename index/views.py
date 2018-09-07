from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import random
import os,time
# Create your views here.
from random import choice

def login_views(request):
    return render(request,'login.html')


def register_views(request):
    if request.method=="GET":
        return render(request,'register.html')
    else:
        #　接受用户的手机号是否存在
        email=request.POST['email']
        user=User.objects.filter(email=email)
        if user:
            #该手机号已经注册,给出提示，回到注册页面
            Msg='邮箱号已经注册'
            return render(request,'register.html',locals())
        else:
            email=request.POST['email']
            upwd=request.POST['upwd'] 
            obj=User(email=email,upwd=upwd)
            obj.save()
            
            Msg='注册成功'
            return render(request,'register.html',locals())





l=[]
def system_views(request):
    
    uemail=request.POST['email']
    uupwd=request.POST['upwd']
    user=User.objects.filter(email=uemail,upwd=uupwd) or ''
    #print(user.email,user.upwd)
    if user:
        l.append(request)
        url="/qa/"
        return render(request,'welcome2.html',locals())
        
    
    else:
        Msg='没有此用户'
        return render(request,'login.html',locals())

dic={}
def aq_views(request):
                
    question=request.POST.get('qname')
    answer=request.POST.get('qanswer')
    dic[question]=answer
    Msg='你已经出过题,休息一会儿'
    return render(request,'question.html',locals())
                
                
def dati_views(request):
    while True:
        time.sleep(1)
        try:
            for x in dic:
                if dic[x]:
                    question=x
                    answer=dic[x]
                    return render(request,'room.html',locals())
        except:
            continue
    



                





al=['答题','出题']
ul=[]
def qa_views(request):
    Msg=choice(al)
    if Msg==al[1] and len(ul)==0:
        print(Msg)
        ul.append(Msg)
        return render(request,'question.html',locals())
    else:
        Msg='你是答题玩家,再次点击答题将进入等待队列'
        url='/dati/'
        return render(request,'welcome2.html',locals())
    

sl=[]
d={}
         
def paihan_views(request):
    name=request.POST['pname']
    score=request.POST['score']
    score=int(score)
    d['name']=name
    d['score']=score
    sl.append(d)
    
    sorted(sl,key=lambda x:x['score'])
    print(sl)
    while True:



        if len(sl)==len(l)-1:
            return render(request,'paihan.html',locals())
            
       