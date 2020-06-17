from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.HomePage.as_view(), name="home"),
    path('case/',views.case_form,name='case_insert'),
    path('list/',views.case_list,name='case_list'),
    path('<int:id>case/',views.case_form,name='case_update'),
    #path('test/', views.TestPage.as_view(), name="test"),
    #path('thanks/', views.ThanksPage.as_view(), name="thanks"),

  #  path('delete/<int:id>/',views.case_delete,name='case_delete'),
]