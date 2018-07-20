from django.urls import path
from .views import DRFAuthenticatedGraphQLView

import rest_framework.authtoken.views

urlpatterns = [
    path('auth/token/', rest_framework.authtoken.views.obtain_auth_token),
    path('', DRFAuthenticatedGraphQLView.as_view(graphiql=True)),
]
