# 답변 관리
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone

from pybo.forms import AnswerForm
from pybo.models import Question, Answer


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def answer_create(request, question_id):                    # 질문 답변
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user                    # 추가된 author 속성 적용, request.user = 현재 로그인한 계정의 User모델 객체
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id))
    else:
        form = AnswerForm()  # POST가 아닐 때 빈 폼을 생성

    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)



@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def answer_modify(request, answer_id):                      # 답변 수정
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)



@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def answer_delete(request, answer_id):                      # 답변 삭제
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)