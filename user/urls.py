from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.project, name="projects"),
    path("create-project", views.create_project, name="create-project"),
    path("update-project/<str:pk>", views.update_project, name="update-project"),
    path("delete-project/<str:pk>", views.delete_project, name="delete-project"),
    path("single-project/<str:pk>", views.single_project, name="single-project"),
    path("", views.profile, name="profiles"),
    path("single-profile/<str:pk>", views.single_profile, name="single-profile"),
    path("signup/", views.register_page, name="sign-up"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("account/", views.Account, name="account"),
    path("create-skill/", views.create_skill, name="create-skill"),
    path("update-skill/<str:pk>", views.update_skill, name="update-skill"),
    path("delete-skill/<str:pk>", views.delete_skill, name="delete-skill"),
    path("edit-account", views.edit_account, name="edit-account"),
    path("inbox", views.Inbox, name="inbox"),
    path("view-inbox/<str:pk>", views.single_message, name='single_inbox'),
    path("send-message/<str:pk>", views.send_message, name="send_message"),
    path("delete-message/<str:pk>", views.delete_message, name="delete-message"),
    path('comment/<str:pk>', views.Comments, name="comment"),
    path("delete-comment/<str:pk>", views.delete_comment, name="delete-comment"),
    path("delete-account/", views.delete_account, name="delete-account")

]
