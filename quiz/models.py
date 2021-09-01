from django.db import models

# Create your models here.

# 테스트용으로 4지선다 질문 하나만 만듦.
# 확인해보려면 superuser 만들어서 admin 계정으로 질문, 선택지, 점수 넣어줘야 함.
class Question(models.Model):
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    # foreignkey 쓰는 거 귀찮아서 그냥 score1,2,3,4 만들어서 admin page에서 점수 넣어줌.
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    score3 = models.IntegerField(default=0)
    score4 = models.IntegerField(default=0)
    
    
    def __str__(self):
        # return self.question
        return str(self.id)+"번 문제"


