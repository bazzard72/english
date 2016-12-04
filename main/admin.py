from django.contrib import admin
from models import Grade
from models import Subfield
from models import Stage
from models import Papersheet, Counter

# Register your models here.

admin.site.register(Grade)
admin.site.register(Subfield)
admin.site.register(Papersheet)
admin.site.register(Stage)
admin.site.register(Counter)