<template>
  <div>
    <GoBack /> |
    <NuxtLink to="/products/create">
      <button>Create product</button>
    </NuxtLink>

    <h1>Product List</h1>

    <div v-if="error" class="alert alert-danger">
      Error al cargar productos. Inténtalo de nuevo.
    </div>

    <table v-else>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.price }}</td>
          <td>
            <NuxtLink :to="`/products/${product.id}`">Detail</NuxtLink> |
            <NuxtLink :to="`/products/update/${product.id}`">Update</NuxtLink> |
            <button @click="deleteProduct(product.id, product.name)">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()

// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase

// 1. Estado global para controlar el loader
const loader = useState('loader')

// 2. Configuramos el título de la página
useHead({
  title: 'Product List',
})

// Simularemos una llamada a la API de Backend usando una API de prueba real
// 'pending' es un booleano reactivo que cambia automáticamente
const { data: response, pending, error, refresh} = await useFetch(`${apiBase}/products/`, {
  lazy: true
})

// 3. Mapeamos los resultados (JSONPlaceholder devuelve un Array directo)
const products = computed(() => response.value || [])

// Función para eliminar un producto
const deleteProduct = async (id, name) => {
  // 1. Confirmación de seguridad
  if (!confirm(`¿Estás seguro de que deseas eliminar a ${name}?`)) return

  try {
    loader.value = true // Activamos el spinner
    // 2. Petición DELETE a Django
    await $fetch(`${apiBase}/products/${id}`, {
      method: 'DELETE'
    })

    // 3. Refrescar la lista automáticamente sin recargar la página
    await refresh()

  } catch (err) {
    console.error('Error al eliminar:', err)
    alert('No se pudo eliminar el producto')
    loader.value = false // Apagamos el spinner
  } finally {
    loader.value = false // Apagamos el spinner
  }
}

// 4. Observamos 'pending' y asignamos su valor directamente al loader
watch(pending, (newVal) => {
  loader.value = newVal
}, { immediate: true }) // immediate asegura que si empieza cargando, el loader se active de una vez
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse; /* Crucial para que las líneas se unan */
}

table, th, td {
  border: 1px solid black; /* Define el grosor, estilo y color de la rejilla */
}

th, td {
  padding: 8px; /* Espaciado interno para que el texto no toque las líneas */
  text-align: left; /* Alineación del texto */
}

th {
  background-color: #f2f2f2; /* Color de fondo opcional para el encabezado */
}
</style>
