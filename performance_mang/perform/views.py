from rest_framework import viewsets
from .models import Goals, Staff, Managers, KRA, TagKra, Job, Feedback_Cateog, Feedback_setting, Feedback, Skill, Tag_skill
from .serializers import GoalsSerializer, StaffSerializer, ManagersSerializer, KRASerializer, TagKraSerializer,JobSerializer, Feedback_CateogSerializer, Feedback_settingSerializer, FeedbackSerializer, SkillSerializer, Tag_skillSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser


class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']
    permission_classes = [IsAdminUser]



class ManagersViewset(viewsets.ModelViewSet):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']
    permission_classes = [IsAdminUser]


class KRAViewset(viewsets.ModelViewSet):
    queryset = KRA.objects.all()
    serializer_class = KRASerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'desciption']
    permission_classes = [IsAdminUser]


class TagKraViewset(viewsets.ModelViewSet):
    queryset = TagKra.objects.all()
    serializer_class = TagKraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kra_name', 'weightage']
    permission_classes = [IsAdminUser]



class GoalsViewset(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['goal_name', 'start_date', 'due_date', 'assigned_by', 'assigned_to', 'status']
    permission_classes = [IsAdminUser]


class Feedback_CateogViewset(viewsets.ModelViewSet):
    queryset = Feedback_Cateog.objects.all()
    serializer_class = Feedback_CateogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories']
    permission_classes = [IsAdminUser]


class Feedback_settingViewset(viewsets.ModelViewSet):
    queryset = Feedback_setting.objects.all()
    serializer_class = Feedback_settingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['feed_type', 'categories']
    permission_classes = [IsAdminUser]



class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['staff_name']
    permission_classes = [IsAdminUser]


class SkillViewset(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['add_skill']
    permission_classes = [IsAdminUser]


class Tag_skillViewset(viewsets.ModelViewSet):
    queryset = Tag_skill.objects.all()
    serializer_class = Tag_skillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['domain', 'select_skill']
    permission_classes = [IsAdminUser]


class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'start_date']
    permission_classes = [IsAdminUser]
