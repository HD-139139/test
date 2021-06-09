from django.db import models    #우리가 실제로 구상할 아이(클래스임)

#질문을 받아줄 클래스 입력, 얘가 부모 클래스인 격
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

#답변(Question함수를 참조해서 답변을 하겠다는 의미, 질문이 있어야 답변이 생기니까)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.question
# Create your models here.
