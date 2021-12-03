from rest_framework import serializers 
from tutorial.models import Tutorials
 
 
class TutorialsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorials
        fields = ('id',
                  'title',
                  'description',
                  'published')