from django.db import models

# Create your models here.

'''
subject : 질문의 제목 
CharField 를 이용하여 글자의 수를 지정할수있음 

content : 질문의 내용 
- TextField : 글의 숫자가 안주어져있음 

create_date : 질문이 만들어진 날짜 \
- DateTimeField 날짜 와 시간을 이용할때 쓴다. 

question : 답변은 질문에 대한 키를 가지고있어야 한다.
- 따라서  Forigin key 매핑을 해주고, on_delete 속성을 이용해 질문이 삭제되면 같이 삭제되도록 
'''

class Question(models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()

