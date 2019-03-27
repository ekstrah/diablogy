from django import forms
from .models import *

class InsertQuery(forms.ModelForm):
    class Meta:
        model = Teststack
        fields = ['id', 'contents', 'end_time', 'fd', 'host_name', 'pipe_val',
        'proc_id', 'proc_name', 'return_byte', 'sock_type', 'start_time',
        'sys_call', 'thread_id' , 'turnaround_time', 'valid'
        ]
