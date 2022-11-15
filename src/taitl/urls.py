from django.urls import path
from .views import DetailProgram, Index
app_name = 'taitl'
urlpatterns = [
    path('', Index.as_view(), name="index"),
    path("detail/<str:slug>", DetailProgram.as_view(), name="program_detail"),
]