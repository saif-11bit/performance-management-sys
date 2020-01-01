from django.contrib import admin
from .models import Staff, Managers, KRA, Goals, Feedback, Skillset

# Register your models here.
admin.site.register(Staff)
admin.site.register(Managers)
admin.site.register(KRA)
admin.site.register(Goals)
admin.site.register(Feedback)
admin.site.register(Skillset)