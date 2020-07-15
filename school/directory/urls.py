from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.DirectoryListView.as_view(), name='root'),
    path('directory/', views.DirectoryListView.as_view(), name='directory-list'),
    path('info/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('addTeacher/', views.AddTeacherView.as_view(), name='add-teacher'),
    path('addTeacher/bulk/', views.AddTeacherBulkView.as_view(), name='add-teacher-bulk'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
