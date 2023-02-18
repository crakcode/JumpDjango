from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

from pybo.models import Question,Answer

def index(request):
    """
    Pybo 목록 출력
    order_by를 이용해서 정렬 create_date의 경우 그냥 정순 -붙이면 역순
    """
    question_list=Question.objects.order_by('-create_date')
    context={'question_list':question_list}
    return render(request,'pybo/question_list.html',context)



def sayHello(request):
    return HttpResponse("hellsss oworlsdadasdsss")


def showTable(request):
    s=""
    for name in Question.objects.all():
        s+=str(name)
        s+=", "
    return HttpResponse(s)


def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={"question":question}
    return render(request,"pybo/question_detail.html",context)

def answer_create(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    return redirect('pybo:detail',question_id)
