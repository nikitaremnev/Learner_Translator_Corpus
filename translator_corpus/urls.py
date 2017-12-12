"""translator_corpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from annotator.admin import learner_admin
from translator_corpus.views import start
from Corpus.views import Search, download_file

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', learner_admin.urls),
    url(r'^$', start, name='start_page'),
    url(r'^document-annotations/', include('annotator.urls', namespace='annotations')),
    url(r'^search/$', Search.as_view(), name='main.search'),
    url(r'^download_file/(?P<doc_id>[\w\-]+)/(?P<doc_type>ann|tokens|text)$', download_file, name='download_file'),
]
