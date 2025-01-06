from django.contrib import admin
from .models import Eventdatapaper
from .models import Eventdataproject
from .models import Eventdatatechnical

# Register your models here.
admin.site.register(Eventdatapaper)
admin.site.register(Eventdataproject)
admin.site.register(Eventdatatechnical)
