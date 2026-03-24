<template>
  <div>
    <GoBack />
    <div v-if="pending">Loading details...</div>
    
    <div v-else-if="error">
      <p>Error: Products with ID: was not found {{ productId }}</p>
    </div>

    <div v-else>
      <h1>Details</h1>
      <div >
        <p><strong>Name:</strong> {{ product.name }}</p>
        <p><strong>Price:</strong> {{ product.price }}</p>
        <p><strong>Created at:</strong> {{ new Date(product.created_at).toLocaleString() }}</p>
        <p><strong>Updated at:</strong> {{ new Date(product.updated_at).toLocaleString() }}</p>
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
const productId = route.params.id

// Pedimos solo los datos de ese usuario específico
const { data: product, pending, error } = await useFetch(`${apiBase}/products/${productId}`)
</script>

<style scoped>
</style>
