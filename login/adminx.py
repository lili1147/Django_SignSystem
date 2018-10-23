__author__ = 'lili'
__date__ = '2018/10/18 17:56'

from .models import Event,Guest

import xadmin

class EventAdmin(object):
    list_display = ['name','limit','status','address','start_time','create_time']
    search_fields = ['name','limit','status','address']
    list_filter = ['name','limit','status','address']

class GuestAdmin(object):
    list_display = ['event','realname','phone','email','sign','create_time']
    search_fields = ['event','realname','phone','email','sign']
    list_filter = ['event','realname','phone','email','sign']


xadmin.site.register(Event,EventAdmin)
xadmin.site.register(Guest,GuestAdmin)
