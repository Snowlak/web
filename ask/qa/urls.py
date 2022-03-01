from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_all, name='home'),
    url(r'^login/', views.login_view),
    url(r'^signup/', views.signup),
    url(r'^ask/', views.ask, name='ask'),
    url(r'new', views.post_all_new_question, name='new'),
    url(r'^popular/', views.post_all_popular_question),
    url(r'^question/(?P<id>[0-9]+)', views.one_post, name='question'),
    url(r'^answer/(?P<question_id>[0-9]+)', views.add_answer, name='answer')
]
