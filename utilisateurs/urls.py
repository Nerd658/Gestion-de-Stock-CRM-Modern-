# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

urlpatterns = [
    # Redirige vers la vue de connexion Django par défaut
    path('accounts/login/', auth_views.LoginView.as_view(template_name='utilisateurs/connexion.html'), name='login'), 
    
    # URL pour la connexion personnalisée si vous avez une vue propre
    # path('login/', CustomLoginView.as_view(), name='login'),  # Si vous préférez utiliser la vue CustomLoginView
    
    path('', views.dashboard, name='dashboard'),
    
    path('logout/', views.custom_logout_view, name='logout'),
]
