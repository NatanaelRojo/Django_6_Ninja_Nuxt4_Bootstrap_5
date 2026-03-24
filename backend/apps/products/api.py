from ninja import Router, ModelSchema, Schema
from django.shortcuts import get_object_or_404
from typing import List
from .models import Product

router = Router()

# --- SCHEMAS ---

class ProductSchema(ModelSchema):
    """Schema basado en el modelo para devolver datos (Output)"""
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'created_at', 'updated_at']

class ProductCreateSchema(Schema):
    """Schema para recibir datos al crear o actualizar (Input)"""
    name: str
    price: int

# --- ENDPOINTS (CRUD) ---

@router.get("/", response=List[ProductSchema])
def list_people(request):
    return Product.objects.all()

@router.get("/{product_id}", response=ProductSchema)
def get_person(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product

@router.post("/", response=ProductSchema)
def create_person(request, data: ProductCreateSchema):
    # .dict() convierte el esquema de Pydantic en un diccionario de Python
    product = Product.objects.create(**data.dict())
    return product

@router.put("/{product_id}", response=ProductSchema)
def update_person(request, product_id: int, data: ProductCreateSchema):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in data.dict().items():
        setattr(product, attr, value)
    product.save()
    return product

@router.delete("/{product_id}")
def delete_person(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True, "message": f"Product {product_id} deleted successfully"}
