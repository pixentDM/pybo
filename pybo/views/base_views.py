# 기본관리
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from pybo.models import Question


def index(request):                         # 질문 목록(리스트)
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')     # 페이지
    kw = request.GET.get('kw', '')          # 검색어
    so = request.GET.get('so', 'recent')    # 정렬 기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:   # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    # question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            #  filter함수에서 모델 필드에 접근하려면 __를 이용해야함!
            Q(subject__icontains=kw) |                  # 제목 검색, subject__icontains : 제목에 kw 문자열이 포함되었는지를 의미함.
            Q(content__icontains=kw) |                  # 내용 검색
            # icontains 를 사용하면 대소문자를 가리지 않고 찾아줌.
            # contains 를 사용하면 대소문자를 구별함.
            Q(author__username__icontains=kw) |         # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이 검색, answer__author__username__icontains : 답변을 작성한 사람의 이름에 포함되는지를 의미함.
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10)                        # 페이지 당 10개씩 보여줌
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}           # page, kw, so 추가됨
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):           # 질문 상세조회
    """
    pybo 내용출력
    """
    question = get_object_or_404(Question, pk=question_id)                      # 모델의 기본키를 이용하여 404페이지 반환
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)