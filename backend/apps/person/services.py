from apps.person.schemas import PersonCreateSchema
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from .models import Person


def list_people() -> QuerySet[Person]:
    return Person.objects.all()


def get_person(person_id: int) -> Person:
    return get_object_or_404(Person, id=person_id)


def create_person(data: PersonCreateSchema) -> Person:
    return Person.objects.create(**data.dict())


def update_person(person_id: int, data: PersonCreateSchema) -> Person:
    person = get_object_or_404(Person, id=person_id)
    for attr, value in data.dict().items():
        setattr(person, attr, value)
    person.save()
    return person


def delete_person(person_id: int) -> None:
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return None
