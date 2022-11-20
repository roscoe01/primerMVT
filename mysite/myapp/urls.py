from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persona/<int:persona_id>', views.persona_por_id , name='persona_por_id')
]