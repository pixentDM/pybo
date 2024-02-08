from django import forms

from pybo.models import Question, Answer, Comment


# 장고 폼
# forms.Form을 상속 받으면 '폼' 이라고 부름
# forms.ModelForm을 상속 받으면 '모델 폼' 이라고 부름
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # }
        labels = {              # 위에 작성된 항목을 한글로 변경
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
