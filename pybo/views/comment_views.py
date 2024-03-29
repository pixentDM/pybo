# 댓글 관리
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone

from pybo.forms import CommentForm, AnswerForm
from pybo.models import Question, Comment, Answer


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def comment_create_question(request, question_id):          # 질문 댓글 등록
    """
    pybo 질문댓글등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def comment_modify_question(request, comment_id):           # 질문 댓글 수정
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('pybo:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def comment_delete_question(request, comment_id):           # 질문 댓글 삭제
    """
    pybo 질문 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('pybo:detail', question_id=comment.question.id)


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def comment_create_answer(request, answer_id):              # 답변 댓글 등록
    """
    pybo 답글댓글등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)



@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def comment_modify_answer(request, comment_id):             # 답변 댓글 수정
    """
    pybo 답글댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('pybo:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)


@login_required(login_url='common:login')                   # @login_required = 애너테이션을 통해 로그인이 되었는지 검사, login_url='common:login' = 로그아웃 상태면 로그인 화면으로 이동
def comment_delete_answer(request, comment_id):             # 답변 삭제
    """
    pybo 답변 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('pybo:detail', question_id=comment.answer.question.id)