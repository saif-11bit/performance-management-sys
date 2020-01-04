from django.contrib import admin
from .models import Staff, Managers, KRA, TagKra, Job, Goals, Feedback_Cateog, Feedback_setting, Feedback, Skill, Tag_skill

# # Register your models here.
admin.site.register(Staff)
admin.site.register(Managers)
admin.site.register(KRA)
admin.site.register(TagKra)
admin.site.register(Job)
admin.site.register(Goals)
admin.site.register(Feedback_Cateog)
admin.site.register(Feedback_setting)
admin.site.register(Feedback)
admin.site.register(Skill)
admin.site.register(Tag_skill)