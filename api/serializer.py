from rest_framework import serializers
from rest_framework.serializers import Field
import numpy as np

class MyField(Field):
    def to_representation(self, value):
        if isinstance(value, np.integer):
            return value
        elif isinstance(value, str):
            return value

class RankSerializer(serializers.Serializer):
    cols = serializers.IntegerField()
    rows = serializers.IntegerField()
    args = serializers.CharField()
    result = MyField()