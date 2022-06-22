from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('text/<int:text_id>/<slug:text_slug>', views.DetailView.as_view(), name='detail'),
    path('text/delete/<int:text_id>', views.DeleteTextView.as_view(), name='text_delete'),
    path('text/update/<int:text_id>', views.UpdateTextView.as_view(), name='text_update'),
]