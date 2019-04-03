from django import forms
from django.forms import ModelForm
from .models import Openstack, Fullstack

CHOICES = (
    ('beta', 'Beta'),
    ('techfossguru', 'Techfossguru',)
)

TABLE_CHOICES = (
            ('id', 'ID'),
            ('contents', 'Contents'),
            ('end_time', 'End Time'),
            ('fd', 'File Discriptor'),
            ('host_name', 'Host Name'),
            ('pipe_val', 'Pipe Value'),
            ('proc_id','Process ID'),
            ('proc_name','Process Name'),
            ('return_byte','Return Byte'),
            ('sock_type','Socket Type'),
            ('start_time','Start Time' ),
            ('sys_call','System Call'),
            ('thread_id','Thread ID'),
            ('turnaround_time', 'Turnaround Time'),
            ('valid', 'Valid '),
)


class KeyspaceForm(forms.Form):
    keyspace = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices = CHOICES,
    )
class TableForm(forms.Form):
    table_columns = forms.ChoiceField(
        required = False,
        widget=forms.Select,
        choices = TABLE_CHOICES,
    )

class InsertQueryForm(forms.ModelForm):
    class Meta:
        model = Openstack   
        fields = ['id', 'end_time', 'fd', 'host_name', 'pipe_val',
        'proc_id', 'proc_name', 'return_byte', 'sock_type', 'start_time',
        'sys_call', 'thread_id' , 'turnaround_time', 'valid'
        ]


#Doesn't work cuz there is no objects in Fullstack


#class TableForm(ModelForm):
#    class Meta:
#        model = Fullstack
 #       fields = [
#            'id',
#            'contents',
 #           'end_time', 
  #          'fd',
   #         'host_name',
    #        'pipe_val',
     #       'proc_id',
      #      'proc_name',
       #     'return_byte',
        #    'sock_type',
         #   'start_time', 
          #  'sys_call',
           # 'thread_id',
            #'turnaround_time', 
            #'valid', 
       # ]