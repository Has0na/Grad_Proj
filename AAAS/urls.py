"""AAAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.signIn, name="$"),
    url(r'^postsign/', views.postsign),
    url(r'^regester/', views.register_Details, name="regester"),
    url(r'^postsignup/', views.postsignup, name='postsignup'),
    url(r'^mainstu/', views.mainstu, name='mainstu'),
    url(r'^json_test/', views.code_test, name='json_test'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^about_us/', views.aboutus, name='about_us'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^Log_Out/', views.logout, name='Log_Out'),
    url(r'^about_st/', views.aboutst, name='about_st'),
    url(r'^report/', views.report, name='report'),
    url(r'^submit_course/', views.course_submit, name='submit_course'),
    url(r'^stReport/', views.student_report, name='stReport'),
    url(r'^courseregistration/', views.course_registration, name='courseregistration'),

    url(r'^regsignin/', views.reglogin, name="regsignin"),
    url(r'^registrerMain/', views.reg_main, name="registrerMain"),
    url(r'^registrer/', views.regmain, name='registrer'),
    url(r'^registrerrole/', views.registrer_role, name='registrerrole'),

    # url(r'^getid/', views.get_id, name='getid'),
    #
    url(r'^res/', views.reset_pass, name='res'),
    #
    # url(r'^regester/', views.register, name="regester"),
    url(r'^post_add/', views.post_add, name='post_add'),
    url(r'^add_s/', views.add_s, name='add_s'),
    #
    url(r'^fill_failed/', views.fill_info2, name='fill_failed'),
    #
    url(r'^fill/', views.fill_info, name='fill'),
    # url(r'^printfill/', views.print_info, name='printfill'),
    #
    url(r'^logout/', views.logout, name='logout'),

]
