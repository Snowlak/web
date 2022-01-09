from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_all_new_question, name='home'),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^popular/', views.post_all_popular_question),
    url(r'^new/', views.test),
    url(r'^question/(?P<id>[0-9]+)', views.one_post, name='question'),
    url(r'^answer/$', views.answer, name='answer')
]
