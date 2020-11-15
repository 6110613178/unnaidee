from django.contrib import admin
from .models import *
'UserUn,Favarite,Cpu,Gpu,Display,Ram,Rom,NoteBook'
admin.site.register(UserUn)
admin.site.register(Gpu)
admin.site.register(Cpu)
admin.site.register(Display)
admin.site.register(Ram)
admin.site.register(Rom)
admin.site.register(NotebookData)
admin.site.register(NoteBook)
admin.site.register(Compare)



