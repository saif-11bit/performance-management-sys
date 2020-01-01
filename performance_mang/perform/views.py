from rest_framework import viewsets
from .models import Goals, Feedback, Skillset, KRA, Staff, Managers
from .serializers import GoalsSerializer, FeedbackSerializer, SkillsetSerializer, StaffSerializer, ManagersSerializer, KRASerializer
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
    filterset_fields = ['tag_to', 'to_achieve']
    permission_classes = [IsAdminUser]


class GoalsViewset(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['goal_name', 'start_date', 'due_date', 'assigned_by', 'assigned_to', 'status']
    permission_classes = [IsAdminUser]


class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['staff_name',]
    permission_classes = [IsAdminUser]


class SkillsetViewset(viewsets.ModelViewSet):
    queryset = Skillset.objects.all()
    serializer_class = SkillsetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['domain',]
    permission_classes = [IsAdminUser]
