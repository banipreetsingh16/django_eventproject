from rest_framework.serializers import ModelSerializer
from .models import Events, Participants


class EventSerializer(ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'
