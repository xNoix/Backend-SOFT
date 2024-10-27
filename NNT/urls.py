"""
URL configuration for NNT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from robot.host.rest.robot_controller import get_robot_connection_info, move_robot_joints, move_robot_pose
from robot.host.rest.secuencias_controller import crear_secuencia, get_all_secuencias, delete_secuencia, get_secuencia


urlpatterns = [
    path("admin/", admin.site.urls),
    path('robot/connection/', get_robot_connection_info, name='get_robot_connection_info'),
    path('robot/move_joints/', move_robot_joints, name='move_robot_joints'),
    path('robot/move_pose/', move_robot_pose, name='move_robot_pose'),
    path('robot/crear_secuencia/', crear_secuencia, name='crear_secuencia'),
    path('robot/get_all_secuencias/', get_all_secuencias, name='get_all_secuencias'),
    path('robot/delete_secuencia/', delete_secuencia, name='delete_secuencia'),
    path('robot/get_secuencia/', get_secuencia, name='get_secuencia'),
]
