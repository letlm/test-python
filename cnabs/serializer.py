from rest_framework import serializers

from .models import InfosTable


class CnabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfosTable
        fields = "__all__"
