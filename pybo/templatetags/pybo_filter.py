import markdown
from django import template
from django.utils.safestring import mark_safe

# 템플릿 필터 (페이지 넘어갈때 번호가 계속 1번인 문제를 해결하기 위함)
register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter()  # 마크다운 필터 등록
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    # nl2br : 줄바꿈 문자를 <br>태그로 바꿔줌 ( Enter를 한 번만 눌러도 줄바꿈으로 인식함)
    # fenced_code : 마크다운의 소스코드 표현을 위해 적용
    return mark_safe(markdown.markdown(value, extensions=extensions))