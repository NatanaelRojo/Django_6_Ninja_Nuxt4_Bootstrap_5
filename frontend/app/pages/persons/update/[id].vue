<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Update Person</h1>

    <form v-if="!pendingFetch" @submit.prevent="updatePerson">
      <div class="mb-3">
        <label class="form-label">Name</label>
        <input v-model="form.name" type="text" class="form-control" required>
      </div>

      <div class="mb-3">
        <label class="form-label">Email Address</label>
        <input v-model="form.email" type="email" class="form-control" required>
      </div>

      <div class="mb-3">
        <label class="form-label">Age</label>
        <input v-model.number="form.age" type="number" class="form-control" required>
      </div>

      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/persons" class="btn btn-secondary">Cancel</NuxtLink>
        <button type="submit" class="btn btn-warning text-white">
          Update Changes
        </button>
      </div>
    </form>
    
    <div v-else class="text-center">
      <p>Cargando datos del usuario...</p>
    </div>
  </div>
</template>

<script setup>
// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()
// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase
// Llamamos al estado global del loader para mostrar el spinner durante la petición
const loader = useState('loader')
// Capturamos el ID de la persona desde la URL
const route = useRoute()
// Extraemos el ID del usuario de los parámetros de la ruta
const personId = route.params.id

// Configuramos el título de la página
useHead({
  title: 'Update Person',
})

// Objeto reactivo para el formulario
const form = ref({
  name: '',
  email: '',
  age: null
})

// Obtenemos los datos de la persona al cargar la página
// Usamos useFetch para traer los datos apenas carga la página
const { data: person, pending: pendingFetch } = await useFetch(`${apiBase}/person/${personId}`, {
  key: `person-${personId}`
})

// Sincronizamos los datos recibidos con el formulario
watch(person, (newVal) => {
  if (newVal) {
    form.value.name = newVal.name
    form.value.email = newVal.email
    form.value.age = newVal.age
  }
}, { immediate: true })

// Método para actualizar la persona
const updatePerson = async () => {
  loader.value = true
  try {
    await $fetch(`${apiBase}/person/${personId}`, {
      method: 'PUT', // PUT reemplaza todo el objeto
      body: form.value
    })

    // Redirigimos de vuelta a la lista de usuarios después de actualizar
    navigateTo('/persons')
  } catch (err) {
    console.error('Update error:', err)
    alert('Error updating. Check if the ID exists.')
  } finally {
    loader.value = false
  }
}
</script>
