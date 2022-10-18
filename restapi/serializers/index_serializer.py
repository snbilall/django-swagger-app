from rest_framework import serializers


class SnippetSerializer(serializers.Serializer):
    id = serializers.DateField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField()
    linenos = serializers.IntegerField(required=False)
    language = serializers.CharField(default='python')
    style = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return validated_data