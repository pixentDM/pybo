from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

from pybo import views

app_name = 'pybo'                                                   # 앱이 관리하는 독립된 이름의 공간(네임스페이스)

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),                                                    # url 하드코딩을 해결하기 위해 name을 줘서 별칭을 만들어줌.
    path('<int:question_id>/', base_views.detail, name='detail'),                                # 질문 상세조회 매핑

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),                # 질문 등록
    path('question/modify/<int:question_id>/', question_views.question_modify,
         name='question_modify'),
    path('question/delete<int:question_id>/', question_views.question_delete,
         name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),  # 답변 등록 매핑
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),  # 질문 댓글 댓글추가
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),   # 질문 댓글 수정
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),   # 질문 댓글 삭제
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),          # 답변 댓글 추가
    path('comment/modify/answer/<int:answer_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),          # 답변 댓글 수정
    path('comment/delete/answer/<int:answer_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),          # 답변 댓글 삭제

    # vote_views.py
    path('vote/question/<int:question_id>/',                # 질문 추천
         vote_views.vote_question, name='vote_question'),
    # question_detail.html 파일의 코드 중 data-uri="{% url 'pybo:vote_question' question.id  %}"에 해당하는 매핑
    path('vote/answer/<int:answer_id>/',
         vote_views.vote_answer, name='vote_answer'),
]