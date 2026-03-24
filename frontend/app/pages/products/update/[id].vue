<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Update Product</h1>

    <form v-if="!pendingFetch" @submit.prevent="updateProduct">
      <div class="mb-3">
        <label class="form-label">Name</label>
        <input v-model="form.name" type="text" class="form-control" required>
      </div>

      <div class="mb-3">
        <label class="form-label">Price</label>
        <input v-model="form.price" type="text" class="form-control" required>
      </div>

      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/products" class="btn btn-secondary">Cancel</NuxtLink>
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
// Capturamos el ID del producto desde la URL
const route = useRoute()
// Extraemos el ID del usuario de los parámetros de la ruta
const productId = route.params.id

const form = ref({
  name: '',
  price: '',
})

// Usamos useAsyncData para un control más preciso
const { data: product, pending: pendingFetch } = await useFetch(`${apiBase}/products/${productId}`, {
  key: `product-detail-${productId}`,
  // Forzamos a que traiga los datos frescos
  pick: ['name', 'price'] 
})

// Sincronización inmediata
if (product.value) {
  form.value = { ...product.value }
}

// Watch por si los datos tardan en llegar (Hydration)
watch(product, (newVal) => {
  if (newVal) {
    form.value.name = newVal.name
    form.value.price = newVal.price
  }
})

const updateProduct = async () => {
  loader.value = true
  try {
    await $fetch(`${apiBase}/products/${productId}`, {
      method: 'PUT',
      body: form.value
    })
    await navigateTo('/products')
  } catch (err) {
    console.error('Error:', err)
  } finally {
    loader.value = false
  }
}
</script>
