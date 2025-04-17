"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from tasks.views import (TaskListView,
                         TaskCreateView,
                         TaskUpdateView,
                         TaskDeleteView,
                         TaskToggleStatusView,
                         TagListView,
                         TagCreateView,
                         TagUpdateView,
                         TagDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/add/", TaskCreateView.as_view(), name="add_task"),
    path("task/edit/<int:pk>", TaskUpdateView.as_view(), name="edit_task"),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name="delete_task"),
    path("task/toggle/<int:pk>", TaskToggleStatusView.as_view(), name="toggle_task"),

    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tag/add/", TagCreateView.as_view(), name="add_tag"),
    path("tag/edit/<int:pk>", TagUpdateView.as_view(), name="edit_tag"),
    path("tag/delete/<int:pk>", TagDeleteView.as_view(), name="delete_tag"),
]
