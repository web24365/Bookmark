from django.db import models

# Create your models here.

class Bookmark(models.Model):
    # field 정의(column)
    # field 이름 = field 종류
    # field 종류의 목적
    # 1. database에 어떤식으로 저장할 것인가
    # 2. 사용자의 입력을 받을 때 어떤 form tag를 보여줄 것인가
    # 2.1. 입력폼의 제한 사항, 유효성 검사(ex: http://xxx.xxx.xxx.xxx)
    site_name = models.CharField(max_length=100)
    # 'Site URL' 입력 form 이름, 없으면 변수명
    url = models.URLField('Site URL')

    # 모델을 다룰 때의 옵션값들 설정
    class Meta:
        # 오름 차순 정렬, -site_name 내림 차순 정렬
        ordering = ['site_name']

    # 개체를 출력할 때 어떤 내용을 출력할지 결정
    def __str__(self):
        return '사이트 이름: ' + self.site_name

    # ex: 글을 쓰고 완료한 후 어느 주소로 이동할 것인지를 결정하기 위해
    def get_absolute_url(self):
        pass

