from rest_framework import serializers
from api.models.Project import Project


class ProjectListSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Project
        fields = ["name", 'code', 'description', 'status', 'creator']
