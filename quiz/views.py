from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

# 점수 총합에 해당하는 전역 변수
total_score = 0

# 질문 전체를 가져와서 render로 띄워주기.
def index(request):
    questions = Question.objects.all() # 모델 전체를 가져옴.
    global total_score # 점수 총합
    
   
    return render(request, 'index.html', {"questions":questions, "total_score":total_score})


# 점수 알고리즘.
def addScore(request, score): # 선택지에 해당하는 점수 == score,  html 선택지 링크에서 전달받음.
    global total_score 
    total_score += score
    
    return redirect('index')


#결과페이지
def result(request):
    global total_score
    # 점수에 따라서 해당하는 이미지를 보여줘야 함. 
    return render(request,'result.html', {"total_score":total_score})


# 테스트 다시하기
def reset(request):
    global total_score
    total_score = 0 # 점수 0으로 초기화시키기.
    return redirect('index') # redirect하는 페이지의 url name을 넣어주기.

