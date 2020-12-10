from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer) :
    class Meta:
        # Quiz 모델에 있는 데이터를 fields 형식의 json 데이터로 출력해줌
        model = Quiz
        fields = ('title', 'body', 'answer')