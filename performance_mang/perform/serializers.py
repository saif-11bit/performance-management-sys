from rest_framework import serializers
from .models import Goals, Skillset, Feedback, Staff, Managers, KRA


class ManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class KRASerializer(serializers.ModelSerializer):
    class Meta:
        model = KRA
        fields = '__all__'


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class SkillsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skillset
        fields = '__all__'