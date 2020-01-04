from rest_framework import serializers
from .models import Goals, Staff, Managers, KRA, TagKra, Job, Feedback_Cateog, Feedback_setting, Feedback, Skill, Tag_skill


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


class TagKraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagKra
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class Feedback_CateogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback_Cateog
        fields = '__all__'

class Feedback_settingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback_setting
        fields = '__all__'



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class Tag_skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag_skill
        fields = '__all__'