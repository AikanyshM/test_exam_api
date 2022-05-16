from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Question, Questionnaire, Answer, Final, User

# для администратора системы

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all().prefetch_related('answer_set')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class QuestionnaireViewSet(ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

# для пользователей системы

class ActiveQuestionnaireListAPIView(ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    
class FinalListCreateAPIView(ListCreateAPIView):
    queryset = Final.objects.all()
    serializer_class = FinalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self, pk):
    #     user_id = self.request.user.id
    #     return Final.objects.filter(pk=user_id)

