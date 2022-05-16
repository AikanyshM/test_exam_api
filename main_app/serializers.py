from rest_framework import serializers
from .models import Questionnaire, Question, Answer, Final
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

    def validate(self, data):
        if data['linked_question']:
            question = data['linked_question']
            if question.type == 'Текст':
                raise serializers.ValidationError("Error")
        return data


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, source = "answer_set", read_only = True)
    class Meta:
        model = Question
        fields = ['questionnaire', 'text', 'type', 'answer']
        read_only_fields = ['answer', ]

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"


class FinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Final
        # fields = ['question', 'answer']
        fields = "__all__"

    def validate(self, data):
        if data['question']:
            question = data['question']
            answer = data['answer']
            if question.type == 'Выбор':
                if not Answer.objects.filter(question=question, text=answer).exists():
                    raise serializers.ValidationError("У данного вопроса тип Текст")
        return data





