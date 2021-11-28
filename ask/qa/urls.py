from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.post_all_new_question),
    url(r'^login/.*$', include('')),
    url(r'^signup/.*', include('')),
    url(r'^ask/.*', include('')),
    url(r'^popular/.*', views.post_all_popular_question),
    url(r'^new/.*', include('')),
    url(r'^admin/', admin.site.urls),
    url(r'^question/(?P<id>[0-9]+)/$', views.one_post)
]
