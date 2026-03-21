<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Register New Person</h1>

    <form @submit.prevent="savePerson">
      <div class="mb-3">
        <label class="form-label">Name</label>
        <input
          v-model="form.name"
          type="text"
          class="form-control"
          required
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Email Address</label>
        <input
          v-model="form.email"
          type="email"
          class="form-control"
          required
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Age</label>
        <input
          v-model.number="form.age"
          type="number"
          class="form-control"
          required
        >
      </div>

      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/persons" class="btn btn-secondary">Cancel</NuxtLink>
        <button type="submit" class="btn btn-primary">
          Save
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()
// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase

// Llamamos al estado global del loader para mostrar el spinner durante la petición
const loader = useState('loader')

// Configuramos el título de la página
useHead({
  title: 'Register Person',
})

// Objeto reactivo para el formulario
const form = ref({
  name: '',
  email: '',
  age: null
})

// Función para guardar la persona
const savePerson = async () => {
  loader.value = true // Activamos el spinner

  // Validación simple para asegurarnos de que los campos no estén vacíos
  try {
    // Usamos $fetch para peticiones manuales (POST, PUT, DELETE)
    await $fetch(`${apiBase}/person/`, {
      method: 'POST',
      body: form.value
    })

    // Si todo sale bien, redirigimos a la lista
    navigateTo('/persons')

  } catch (err) {
    console.error('Error saving data:', err)
    alert('Failed to save person. Check Django logs.')
  } finally {
    loader.value = false // Apagamos el spinner
  }
}
</script>
