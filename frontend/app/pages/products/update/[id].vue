<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Update Product</h1>

    <form v-if="!pendingFetch" @submit.prevent="updateProduct">
      <div class="mb-3">
        <label for="nameInput" class="form-label">Name</label>
        <input 
          id="nameInput" 
          v-model="form.name" 
          type="text" 
          class="form-control" 
          required
        >
      </div>

      <div class="mb-3">
        <label for="priceInput" class="form-label">Price</label>
        <input 
          id="priceInput" 
          v-model="form.price" 
          type="text" 
          class="form-control" 
          required
        >
      </div>

      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/products" class="btn btn-secondary">Cancel</NuxtLink>
        <button type="submit" class="btn btn-warning text-white">
          Update Changes
        </button>
      </div>
    </form>
    
    <div v-else class="text-center" aria-live="polite">
      <p>Cargando datos del producto...</p>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['auth'],
})

const config = useRuntimeConfig()
const apiBase = config.public.apiBase
const loader = useState('loader')
const route = useRoute()
const productId = route.params.id

// 1. Fetch the data securely using our custom courier and useAsyncData
const { data: product, pending: pendingFetch } = await useAsyncData(`product-update-${productId}`, () => 
  useApiFetch(`${apiBase}/products/${productId}/`)
)

// 2. Clean Code: Directly initialize the form with the fetched data
// The '?.' (optional chaining) safely handles cases where product might be null
const form = ref({
  name: product.value?.name || '',
  price: product.value?.price || '',
})

const updateProduct = async () => {
  loader.value = true
  try {
    // 3. Send the PUT request securely with our custom courier
    await useApiFetch(`${apiBase}/products/${productId}/`, {
      method: 'PUT',
      body: form.value
    })
    
    await navigateTo('/products')
  } catch (err) {
    console.error('Error:', err)
    // Optional: Add an alert here so NVDA announces if the update fails
    alert('No se pudo actualizar el producto.')
  } finally {
    loader.value = false
  }
}
</script>