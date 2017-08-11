from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views
urlpatterns=[
    url(r'^login/$',login,{'template_name':'login.html'}),
    url(r'^home_page/$',views.home_page,name='home_page'),
    url(r'^logout/$',logout,{'template_name':'logout.html'}),
    url(r'^create_user/$',views.create_user,name='create_user'),
    url(r'^player_list/$',views.player_list,name='player_list'),
    url(r'^change_pass/$',views.changePassword,name='change_pass'),
    url(r'^receipt/$',views.receipt,name='receipt'),
    url(r'^add_receipt/$',views.add_receipt,name='add_receipt'),
    url(r'^redirect_edit_receipt/$',views.redirect_edit_receipt,name='redirect_edit_receipt'),
    url(r'^update_receipt/$',views.update_receipt,name='update_receipt'),
    url(r'^delete_receipt/$',views.delete_receipt,name='delete_receipt'),
    url(r'^delete_selected_receipt/$',views.delete_selected_receipt,name='delete_selected_receipt'),
    url(r'^search_receipt/$',views.search_receipt_follow_month_year,name='search_receipt'),
    url(r'^test_dict/$',views.test_dict,name='test_dict'),
]

