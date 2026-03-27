export default defineNuxtRouteMiddleware((to, from) => {
  // Read the cookie securely
  const token = useCookie('access_token')

  // If there is no token, redirect to the login page
  if (!token.value) {
    return navigateTo('/login')
  }
})