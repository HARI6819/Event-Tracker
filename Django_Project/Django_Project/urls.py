"""
URL configuration for Django_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from My_Application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    # path('',views.home,name="home"),  
    # path('index1/sign/',views.sign),  
    # path('index1/sign/index/',views.homepage),
    path('' ,views.page), 
    path('admin1',views.admin1),
    path('adminpaper',views.adminpaper),
    path('logout',views.logout_view),
    path('accounts/', include('allauth.urls')), 
    path('/', include('My_Application.urls')),
    path('loginpage' ,views.login),
    path('paper1', views.index,name='paper1'),
    path('project1', views.project,name='project1'),
    path('technical', views.technical, name='technical'),
    path('home1', views.index),
    path('createnew', views.index),
    path('createnewproject',views.project),
    path('createnewtechnical',views.technical),
    path('upload<int:id>', views.upload, name='paper1'),
    path('uploadproject<int:id>', views.uploadproject, name='project1'),
    path('uploadtechnical<int:id>', views.uploadtechnical, name='technical'),
    path('camera.html<int:id>', views.camera),
    path('cameraproject.html<int:id>', views.cameraproject),
    path('cameratechnical.html<int:id>', views.cameratechnical),
    path('update<int:id>',views.update),
    path('updateproject<int:id>',views.updateproject),
    path('updatetechnical<int:id>',views.updatetechnical),
    path('delete<int:id>',views.delete),
    path('deleteproject<int:id>',views.deleteproject),
    path('deletetechnical<int:id>',views.deletetechnical),
    path('addData',views.index,name="register"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)