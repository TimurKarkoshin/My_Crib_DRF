import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Smartphone, Category


class SmartphoneModel:
    def __init__(self, name, descritpion):
        self.name = name
        self.description = descritpion


class SmartphoneSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Smartphone
        fields = "__all__"


class SmartphoneSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    description = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=False
    )

    def create(self, validated_data):
        return Smartphone.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.time_create = validated_data.get("description", instance.time_create)
        instance.time_update = validated_data.get("description", instance.time_update)
        instance.save()
        return instance

def encode():
    model = SmartphoneModel("IPohui", "Ты только делаешь глаток, и в это же мгновение... ТЕБЯ УНОСЯТ ПАРУСА!")
    model_sr = SmartphoneSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"name":"IPohui", "description":"WONDERDUL WONDERFUL DREAM! FUCK THIS FUCK OFF!"}')
    data = JSONParser().parse(stream)
    serializer = SmartphoneSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
