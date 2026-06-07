from rest_framework import serializers


class GenerateTextSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True, help_text="Input text prompt")
    temperature = serializers.FloatField(
        required=False, default=0.7, min_value=0.0, max_value=1.0,
        help_text="Controls randomness (0=deterministic, 1=creative)"
    )
    max_tokens = serializers.IntegerField(
        required=False, default=2048, min_value=1, max_value=8192,
        help_text="Maximum length of response"
    )


class ChatSerializer(serializers.Serializer):
    messages = serializers.ListField(
        child=serializers.DictField(),
        required=True,
        help_text="List of message objects with 'role' and 'parts'"
    )
    temperature = serializers.FloatField(
        required=False, default=0.7, min_value=0.0, max_value=1.0
    )