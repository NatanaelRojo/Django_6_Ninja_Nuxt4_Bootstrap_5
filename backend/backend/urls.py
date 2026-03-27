from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from ninja import NinjaAPI

# Importamos el router de la app producs
from apps.products.api import router as products_router

# Importamos el router de la app users
from apps.users.api import router as users_router

# Instancia del API
api = NinjaAPI(title="Mi Proyecto CRUD API")

# Routers de la app Productos
api.add_router("/products/", products_router)
# Routers de la app Users
api.add_router("/users/", users_router)

urlpatterns = [
    # Ruta para el admin
    path("admin/", admin.site.urls),
    # Redirigir la raíz al login de users
    path("", lambda request: redirect("users:login"), name="root"),
    # Tus rutas de las apps
    path("products/", include("apps.products.urls")),
    path("users/", include("apps.users.urls")),
    # Ruta para el API
    path("api/", api.urls),
]
