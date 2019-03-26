from rest_framework import serializers

from postings.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BlogPost # similar data from model
        fields = ['url',
                  'pk',
                  'user',
                  'title',
                  'content',
                  'timestamp',
                  ] # model field

        read_only_fields = ['pk','user']

    def get_url(self, obj):
        #request
        request = self.context.get("request")
        return obj.get_api_url(request=request  )

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('The title provided already exists')
        return value
