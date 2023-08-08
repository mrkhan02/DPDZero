from django.urls import path
from .views import CustomUserCreate, Logout
from .views import ItemListCreateView, ItemRetrieveUpdateDeleteView
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='user-register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('logout/', Logout.as_view(), name='logout'),
    path('data/', ItemListCreateView.as_view(), name='item-list-create'),
    path('data/<str:key>/', ItemRetrieveUpdateDeleteView.as_view(), name='item-retrieve-update-delete'),
]
