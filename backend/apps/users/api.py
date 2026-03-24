from ninja import Router, ModelSchema, Schema
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from typing import List
from .models import User

router = Router()

# --- SCHEMAS ---

class UserSchema(ModelSchema):
    """Schema para devolver datos del usuario (Output)"""
    class Meta:
        model = User
        # Listamos los campos definidos en tus formularios
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

class UserCreateSchema(Schema):
    """Schema para crear un usuario (Input)"""
    username: str
    email: str
    password: str
    first_name: str = None
    last_name: str = None
    role: str = "user" # Valor por defecto si no se envía

class UserUpdateSchema(Schema):
    """Schema para actualizar un usuario (campos opcionales)"""
    email: str = None
    first_name: str = None
    last_name: str = None
    role: str = None

# --- ENDPOINTS (CRUD) ---

@router.get("/", response=List[UserSchema])
def list_users(request):
    """Lista todos los usuarios del sistema"""
    return User.objects.all()

@router.get("/{user_id}", response=UserSchema)
def get_user(request, user_id: int):
    """Obtiene un usuario específico por su ID"""
    user = get_object_or_404(User, id=user_id)
    return user

@router.post("/", response=UserSchema)
def create_user(request, data: UserCreateSchema):
    """Crea un nuevo usuario con contraseña encriptada"""
    user_data = data.model_dump()
    # Importante: Encriptar la contraseña antes de guardar
    user_data['password'] = make_password(user_data['password'])
    
    user = User.objects.create(**user_data)
    return user

@router.put("/{user_id}", response=UserSchema)
def update_user(request, user_id: int, data: UserUpdateSchema):
    """Actualiza los datos de un usuario existente"""
    user = get_object_or_404(User, id=user_id)
    
    # Filtramos solo los campos que no son None para actualizar
    for attr, value in data.model_dump(exclude_none=True).items():
        setattr(user, attr, value)
    
    user.save()
    return user

@router.delete("/{user_id}")
def delete_user(request, user_id: int):
    """Elimina un usuario"""
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True, "message": f"User {user_id} deleted successfully"}
