from django.db import models

# Create your models here.
class Blog(models.Model):
    # 모델 클래스의 속성을 상속받음
    title = models.CharField(max_length=200) # 제한이 있는 문자형
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField() 
    body = models.TextField()
    # 제목이 보이도록 만들기
    # def __str__(self):
    #     return self.title
    # 글이 전부 보이지 않도록 만들기
    def summary(self):
        return self.body[:100]
