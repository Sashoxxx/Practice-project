from django.urls import path

from todo.views import (
    index,
    TaskCreateView,
    toggle_task_status,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView
)
urlpatterns = [
    path("", index, name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("toggle/<int:pk>", toggle_task_status, name="toggle-task"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete")

]

app_name = "todo"
