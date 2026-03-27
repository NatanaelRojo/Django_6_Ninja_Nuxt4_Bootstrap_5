<template>
  <div>
    <h1>
      <img
        src="/images/star.png"
        alt="star"
        class="img-fluid mb-3"
        width="50"
      >
      Django 6 + Django Ninja + Nuxt 4 + Bootstrap 5
    </h1>

    <button 
      @click="handleLogout" 
      class="btn btn-danger mt-4"
      :disabled="isLoggingOut"
      aria-live="polite"
    >
      <span v-if="isLoggingOut">Logging out...</span>
      <span v-else>Log out</span>
    </button>

    <div v-if="logoutError" class="alert alert-warning mt-3" role="alert">
      {{ logoutError }}
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

useHead({
  title: 'Home'
})

// Initialize runtime config to access the API Base URL
const config = useRuntimeConfig()
const apiBase = config.public.apiBase

const loader = useState('loader')

// Reactive variables for the logout state
const isLoggingOut = ref(false)
const logoutError = ref('')

// Access the cookies
const accessToken = useCookie('access_token')
const refreshToken = useCookie('refresh_token')

onMounted(() => {
  console.log("Activo el loader")
  loader.value = true

  setTimeout(() => {
    loader.value = false
    console.log("Ha pasado 1 segundo y quité el loader")
  }, 1000)
})

// 3. The Logout Logic
const handleLogout = async () => {
  isLoggingOut.value = true
  logoutError.value = ''

  try {
    // Send the POST request to your nested users router
    if (refreshToken.value) {
      // Note: We use the native $fetch here instead of useApiFetch because 
      // the logout endpoint expects the refresh token in the BODY, not the HEADER.
      await $fetch(`${apiBase}/users/logout`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        },
        body: {
          refresh: refreshToken.value
        }
      })
    }
  } catch (error) {
    console.error("Logout failed on the backend:", error)
    logoutError.value = "No se pudo conectar con el servidor, pero tu sesión local ha sido cerrada."
  } finally {
    // 4. Destroy the local cookies securely
    accessToken.value = null
    refreshToken.value = null

    // 5. Redirect the user back to the login screen
    isLoggingOut.value = false
    await navigateTo('/login')
  }
}
</script>