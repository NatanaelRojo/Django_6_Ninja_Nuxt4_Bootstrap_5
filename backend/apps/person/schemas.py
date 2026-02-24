from apps.person.models import Person
from ninja import ModelSchema, Schema


class PersonSchema(ModelSchema):
    """Schema basado en el modelo para devolver datos (Output)"""

    class Meta:
        model = Person
        fields = ["id", "name", "email", "age", "created_at", "updated_at"]


class PersonCreateSchema(Schema):
    """Schema para recibir datos al crear o actualizar (Input)"""

    name: str
    email: str
    age: int
