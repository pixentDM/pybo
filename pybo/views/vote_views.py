from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from pybo.models import Question, Answer


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def vote_question(request, question_id):                    # 질문 등록
    """
    pybo 질문 추천 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:                     # 본인 게시물에 본인이 추천하는 것을 방지하기 위한 오류
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def vote_answer(request, answer_id):                        # 답변 추천 기능
    """
    pybo 답글 추천 등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)