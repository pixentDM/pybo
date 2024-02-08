# 질문 관리
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from pybo.forms import QuestionForm
from pybo.models import Question


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def question_create(request):                               # 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():                         # form이 유효한지 검사
            question = form.save(commit=False)      # form으로 Question 모델 데이터를 저장하기 위한 코드
            question.author = request.user          # 추가한 속성 author 적용
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')

    else:                                           # request.method 가 get인 경우
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html',context)



@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def question_modify(request,question_id):                   # 질문 수정
    question = get_object_or_404(Question, pk=question_id)  #test
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()           # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question_id)

    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)



@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def question_delete(request, question_id):                  # 질문 삭제
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

