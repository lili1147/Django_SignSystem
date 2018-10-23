from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from login.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404


# Create your views here.

def login_action(request):
    if request.method =='POST':
        username = request.POST.get('username','null')
        pwd = request.POST.get('password','null')
        user = authenticate(username=username,password=pwd)
        if user is not None:
            login(request,user)
            request.session['user'] = username
            return redirect('/Message_event')
        else:
            return render(request,'login.html',{'err_msg':'用户名或密码错误'})
    else:
        return render(request,'login.html')

@login_required
def message_event(request):
    even_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'Message_event.html',{'user':username,'events':even_list})

@login_required
def Search_name(request):
    username = request.session.get('user','')
    serchname = request.GET.get('name','')
    #搜索数据库中名字包含想要搜索的内容，模糊搜索 注意这里是双下划线
    event_list = Event.objects.filter(name__contains=serchname)
    return render(request,'Message_event.html',{'user':username,'events':event_list})

@login_required
def Guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
        print(contacts)
    except PageNotAnInteger:
        #if page is not an integer,deliver first page
        contacts = paginator.page(1)
    except EmptyPage:
        #if page is out of range(9999),deliver last page of results
        contacts = paginator.page(paginator.num_pages)
    return render(request,'Guset_manage.html',{'user':username,'guests':contacts})


@login_required
def sign_index(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    return render(request,'sign_index.html',{'event':event})


@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    phone =request.POST.get('phone','')

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hit':'phone error'})

    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        render(request,'sign_index.html',{'event':event,'hit':'event_id or phone error'})

    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hit':'user has sign in'})

    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hit':'sign in success','guest':result})

