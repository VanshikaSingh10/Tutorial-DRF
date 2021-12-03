
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from tutorial import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tutorial',views.TutorialViewSet,basename='tutorial')

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Tutorial API",
#         default_version='v1',
#         description="Welcome to the world of Tutorial",
#         terms_of_service="https://www.tutorial.org",
#         contact=openapi.Contact(email="vanshika@tutorial.org"),
#         license=openapi.License(name="Awesome IP"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
   path('admin/', admin.site.urls),
   #url(r'^', include('tutorial.urls')),
#     path('', schema_view.with_ui('swagger',
#                                  cache_timeout=0), name='schema-swagger-ui'),

# #     path('api/api.json/', schema_view.without_ui(cache_timeout=0),
# #          name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc',
                                   #   cache_timeout=0), name='schema-redoc'),
    path('',include(router.urls)),
]
