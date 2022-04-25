from django.urls import path
from .views import TestedList, TestedDetail

app_name = 'tested'

urlpatterns = [
    path('', TestedList.as_view(), name='list'),
    path('<int:pk>', TestedDetail.as_view(), name='detail')
]