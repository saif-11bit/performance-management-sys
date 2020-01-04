from rest_framework import routers
from perform.views import StaffViewset, ManagersViewset, GoalsViewset, KRAViewset, TagKraViewset, Feedback_CateogViewset, Feedback_settingViewset, FeedbackViewset, SkillViewset, Tag_skillViewset
from django.contrib import admin
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'staff', StaffViewset,'staff')
router.register(r'manager', ManagersViewset, 'manager')
router.register(r'goal', GoalsViewset, 'goal')
router.register(r'kra', KRAViewset, 'kra')
router.register(r'tag_kra', TagKraViewset, 'tag_kra')
router.register(r'feedback_cate', Feedback_CateogViewset, 'feedback_cate')
router.register(r'feedback_setting', Feedback_settingViewset, 'feedback_setting')
router.register(r'feedback', FeedbackViewset, 'feedback')
router.register(r'skill', StaffViewset, 'skill')
router.register(r'tag_skill', Tag_skillViewset, 'tag_skill')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
]
