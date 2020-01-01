from rest_framework import routers
from perform.views import GoalsViewset, FeedbackViewset, SkillsetViewset, StaffViewset, ManagersViewset, KRAViewset
from django.contrib import admin
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'goals', GoalsViewset, 'goals')
router.register(r'feedback', FeedbackViewset, 'feedback')
router.register(r'skillset', SkillsetViewset, 'skillset')
router.register(r'staff', StaffViewset, 'staff')
router.register(r'manager', ManagersViewset, 'manager')
router.register(r'kra', KRAViewset, 'kra')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
]
