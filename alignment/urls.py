# coding=utf-8
u"""Управление возможными url с префиксом /translator_corpus/document-alignment"""

from django.conf.urls import url

from alignment.views import Root, Index, Annot, Search, EditorView2, mark, get_correction, handle_upload, star


urlpatterns = [
                       # storage API
                       url(r'^$', Root.as_view(), name='align.root'),

                       url(r'^search$', Search.as_view(), name='align.search'),

                       # update corrections
                       url(r'^get_correction_by_id/(?P<doc_id>[\w\-]*)', get_correction, name="get.correction"),

                       # mark text as (not) annotated/checked/aligned
                       url(r'^document/(?P<doc_id>[\w\-]+)/mark$', mark),

                       url(r'^star/(?P<sent_id>[\w\-]+)/(?P<todo>add|remove)$', star, name="star"),

                       # public pages
                       url(r'^document/(?P<doc_id>[\w\-]+)/edit$', EditorView2.as_view(), name='align.editor'),
                       ]