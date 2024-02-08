from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):                                           # 질문 테이블
    author = models.ForeignKey(User, on_delete=models.CASCADE,          # 글쓴이, on_delete=models.CASCADE = 계정이 삭제되면 계정과 연결된 모든 데이터를 모두 삭제하라
                               related_name='author_question')          # related_name= : 밑에 추천인 필드와 동일하게 "user"을 참조하고 있어 데이터에 적급할때 어떤 필드를 기준으로 할지 알 수 없기 때문에 직접 정함
    subject = models.CharField(max_length=200)                          # 제목
    content = models.TextField()                                        # 내용
    create_date = models.DateTimeField()                                # 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)           # 수정일시
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인
    # related_name= : 위에 글쓴이 필드와 동일하게 "user"을 참조하고 있어 데이터에 적급할때 어떤 필드를 기준으로 할지 알 수 없기 때문에 직접 정함
    # ManyToManyField : 같은 사용자가 하나의 질문을 여러 번 추천해도 추천 수가 증가하지 않음. 이 함수는 중복을 허락하지 않음, 다대다 관계를 지원함

    def __str__(self):                                                  # Question 모델 데이터 조회 결과에 속성값 보여주기
        return self.subject


class Answer(models.Model):                                             # 답변 테이블
    author = models.ForeignKey(User, on_delete=models.CASCADE,          # 글쓴이, on_delete=models.CASCADE = 계정이 삭제되면 계정과 연결된 모든 데이터를 모두 삭제하라
                               related_name='author_answer')            # related_name : Question 테이블과 동일한 이유로 작성됨
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 외래키
    content = models.TextField()                                        # 내용
    create_date = models.DateTimeField()                                # 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)           # 수정일시
    voter = models.ManyToManyField(User, related_name='voter_answer')   # 추천인
    # related_name : Question 테이블과 동일한 이유로 작성됨
    # ManyToManyField : 같은 사용자가 하나의 질문을 여러 번 추천해도 추천 수가 증가하지 않음. 이 함수는 중복을 허락하지 않음, 다대다 관계를 지원함



class Comment(models.Model):                                                                    # 댓글 테이블
    author = models.ForeignKey(User, on_delete=models.CASCADE)                                  # 댓글 글쓴이
    content = models.TextField()                                                                # 댓글 내용
    create_date = models.DateTimeField()                                                        # 댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)                                   # 댓글 수정일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)     # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)         # 이 댓글이 달린 답변
