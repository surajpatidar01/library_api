

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Token URLs
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),

    # Your app URLs
    path('api/', include('library.urls')),

    # DRF Browsable API login/logout
    path('api-auth/', include('rest_framework.urls')),
]




















#
#
# from django.contrib import admin
# from django.urls import path,include
# from rest_framework.authtoken.views import obtain_auth_token
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/',include('library.urls')),
#
#     path('api-auth/', include('rest_framework.urls')),
#     path('api-token-auth/', obtain_auth_token),
# ]
#
#
