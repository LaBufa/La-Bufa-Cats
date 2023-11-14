from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('catalogo/', views.CatalogoView.as_view(), name='catalogo'),
    path('<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
    path('<int:pk>/adocao', views.AdocaoView.as_view(), name='adocao'),
    path('index/', views.PrincipalView.as_view(), name='index'),
    path('rifas/', views.RifasView.as_view(), name='rifas'),
    path('doacao/', views.DoacaoView.as_view(), name='doacao'),
    path('<path:path>/', views.NotFoundView.as_view(), name='page_not_found'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)