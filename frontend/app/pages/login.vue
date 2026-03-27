<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1 class="mb-4">Log In</h1>

                <div 
          v-if="errorMessage" 
          class="alert alert-danger" 
          role="alert"
        >
          {{ errorMessage }}
        </div>
        
        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="usernameInput" class="form-label">Username</label>
            <input 
              type="text" 
              class="form-control" 
              id="usernameInput" 
              v-model="username" 
              required 
            />
          </div>

          <div class="mb-3">
            <label for="passwordInput" class="form-label">Password</label>
            <input 
              type="password" 
              class="form-control" 
              id="passwordInput" 
              v-model="password" 
              required 
            />
          </div>

          <button type="submit" class="btn btn-primary w-100">Sign In</button>
        </form>
        
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const errorMessage = ref('') // New reactive variable for the error UI
const router = useRouter()

const handleLogin = async () => {
  // 1. Clear any previous errors before a new attempt
  errorMessage.value = '' 

  try {
    const response = await $fetch('http://127.0.0.1:8000/api/users/token/pair', {
      method: 'POST',
      body: {
        username: username.value,
        password: password.value
      }
    })

    const accessToken = useCookie('access_token')
    const refreshToken = useCookie('refresh_token')

    accessToken.value = response.access
    refreshToken.value = response.refresh

    await router.push('/')
  } catch (error) {
    console.log(error.status);
    // 2. Catch the error and display a user-friendly message
    if (error.status === 401) {
      errorMessage.value = "Invalid username or password. Please try again."
    } else {
      errorMessage.value = "A network error occurred. Please verify your connection."
    }
    console.error("Login failed:", error)
  }
}
</script>