from django.urls import path
from .views import index_view, photo_detail_view, photo_upload_view, photo_edit_view, photo_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('photo/<int:pk>/', photo_detail_view, name='photo_detail'),
    path('photo/upload/', photo_upload_view, name='photo_upload'),
    path('photo/<int:pk>/edit/', photo_edit_view, name='photo_edit'),
    path('photo/<int:pk>/delete/', photo_delete_view, name='photo_delete'),
]
