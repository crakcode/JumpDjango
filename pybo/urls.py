from django.urls import path
from . import views

"""
<int:question_id>/ 이 주소가 변경될수있으니
detail이라는 별칭을 사용하기 

네임스페이스 app_name
- 분리하는 경우 html에서 pybo:별칭 써서 부러줘야됨 

"""

app_name='pybo'



urlpatterns=[
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    path('hellos/',views.sayHello),
    path('show/',views.showTable)
]