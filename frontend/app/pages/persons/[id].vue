<template>
  <div>
    <GoBack />
    <div v-if="pending">Loading details...</div>
    
    <div v-else-if="error">
      <p>Error: Person with ID: was not found {{ personId }}</p>
    </div>

    <div v-else>
      <h1>Profile from: {{ person.name }}</h1>
      <div >
        <p><strong>Email:</strong> {{ person.email }}</p>
        <p><strong>Age:</strong> {{ person.age }}</p>
        <p><strong>Created at:</strong> {{ new Date(person.created_at).toLocaleString() }}</p>
        <p><strong>Updated at:</strong> {{ new Date(person.updated_at).toLocaleString() }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()
// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase

// Configuramos el título de la página
useHead({
  title: 'User detail',
})

// Obtenemos el ID desde la URL
const route = useRoute()
const personId = route.params.id

// Pedimos solo los datos de ese usuario específico
const { data: person, pending, error } = await useFetch(`${apiBase}/person/${personId}`)
</script>

<style scoped>
</style>
