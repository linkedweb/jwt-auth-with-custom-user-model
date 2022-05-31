from django.urls import path
from .views import CreateUserAccount, RetrieveUserAccount


urlpatterns = [
  path('create', CreateUserAccount.as_view()),
  path('user', RetrieveUserAccount.as_view()),
]
