from typing import List

from apps.person.schemas import PersonCreateSchema, PersonSchema
from django.http import HttpRequest
from ninja import Router

from . import services

router = Router()


# 1. Listar personas (GET)
@router.get("/", response=List[PersonSchema])
def list_people(request: HttpRequest):
    return services.list_people()


# 2. Obtener una persona (GET por ID)
@router.get("/{person_id}", response=PersonSchema)
def get_person(request: HttpRequest, person_id: int):
    return services.get_person(person_id)


# 3. Crear una persona (POST)
@router.post("/", response=PersonSchema)
def create_person(request: HttpRequest, data: PersonCreateSchema):
    return services.create_person(data)


# 4. Actualizar una persona (PUT)
@router.put("/{person_id}", response=PersonSchema)
def update_person(request: HttpRequest, person_id: int, data: PersonCreateSchema):
    return services.update_person(person_id, data)


# 5. Eliminar una persona
@router.delete("/{person_id}")
def delete_person(request: HttpRequest, person_id: int) -> dict[str, str | bool]:
    services.delete_person(person_id)
    return {"success": True, "message": f"Person {person_id} deleted successfully"}
