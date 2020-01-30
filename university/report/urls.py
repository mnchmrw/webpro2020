from django.urls import include, path
from report import views


urlpatterns = [
    path('dashboard/', views.dashboard),
    path('search/<int:id>', views.search)
]
