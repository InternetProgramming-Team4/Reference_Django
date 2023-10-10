from django.db import models

# Create your models here.

class Post(models.Model):
    # DB col을 생성, model -> title
    title = models.CharField(max_length=30)

    # DB col을 생성, model -> content
    content = models.TextField()

    # DB col을 생성, model -> 시간
    # 현재 시간을 새로 작성할 때 바로 넣기
    create_at = models.DateTimeField(auto_now_add=True)

    # 수정 시간을 업데이트 했을 때, 수정 현재 시각으로 교체
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'


    def get_absolute_url(self):
        return f'/blog/{self.pk}/'