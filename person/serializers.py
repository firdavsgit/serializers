from rest_framework import serializers



class Sportserializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
