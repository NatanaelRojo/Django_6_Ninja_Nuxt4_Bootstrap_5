<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Register Product</h1>

    <form @submit.prevent="saveProduct">
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
        <label class="form-label">Price</label>
        <input
          v-model="form.price"
          type="text"
          class="form-control"
          required
        >
      </div>

      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/products" class="btn btn-secondary">Cancel</NuxtLink>
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
  title: 'Register Product',
})

// Objeto reactivo para el formulario
const form = ref({
  name: '',
  price: ''
})

// Función para guardar el producto
const saveProduct = async () => {
  loader.value = true // Activamos el spinner

  // Validación simple para asegurarnos de que los campos no estén vacíos
  try {
    // Usamos $fetch para peticiones manuales (POST, PUT, DELETE)
    await $fetch(`${apiBase}/products/`, {
      method: 'POST',
      body: form.value
    })

    // Si todo sale bien, redirigimos a la lista
    navigateTo('/products')

  } catch (err) {
    console.error('Error saving data:', err)
    alert('Failed to save product. Check Django logs.')
  } finally {
    loader.value = false // Apagamos el spinner
  }
}
</script>
