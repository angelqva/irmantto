from rest_framework.routers import SimpleRouter
from .views import UserView, LogoutView

user_router = SimpleRouter()
user_router.register('users', UserView, basename='users')

logout_router = SimpleRouter()
logout_router.register('logout', LogoutView, basename='logout')
