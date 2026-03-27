from typing import List

from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Router, Schema
from ninja_jwt.authentication import JWTAuth

from .models import Product

# Protegemos todas las rutas con JWTAuth
router = Router(auth=JWTAuth())

# --- SCHEMAS ---


class ProductSchema(ModelSchema):
    """Schema basado en el modelo para devolver datos (Output)"""

    class Meta:
        model = Product
        fields = ["id", "name", "price", "created_at", "updated_at"]


class ProductCreateSchema(Schema):
    """Schema para recibir datos al crear o actualizar (Input)"""

    name: str
    price: int


# --- ENDPOINTS (CRUD) ---


@router.get("/", response=List[ProductSchema])
def list_products(request):
    """Lista todos los productos de la base de datos"""
    return Product.objects.all()


@router.get("/{product_id}", response=ProductSchema)
def get_product(request, product_id: int):
    """Obtiene un producto específico por su ID"""
    product = get_object_or_404(Product, id=product_id)
    return product


@router.post("/", response=ProductSchema)
def create_product(request, data: ProductCreateSchema):
    """Crea un nuevo producto"""
    # .model_dump() es el reemplazo moderno de .dict() en Pydantic v2
    product = Product.objects.create(**data.model_dump())
    return product


@router.put("/{product_id}", response=ProductSchema)
def update_product(request, product_id: int, data: ProductCreateSchema):
    """Actualiza un producto existente"""
    product = get_object_or_404(Product, id=product_id)
    for attr, value in data.model_dump().items():
        setattr(product, attr, value)
    product.save()
    return product


@router.delete("/{product_id}")
def delete_product(request, product_id: int):
    """Elimina un producto de la base de datos"""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True, "message": f"Product {product_id} deleted successfully"}
