export const useApiFetch = (request, options = {}) => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const accessToken = useCookie('access_token')
  const refreshToken = useCookie('refresh_token')

  // We create a customized version of $fetch
  const customFetch = $fetch.create({
    // 1. Automatically attach the access token BEFORE sending
    onRequest({ options }) {
      if (accessToken.value) {
        options.headers = {
          ...options.headers,
          Authorization: `Bearer ${accessToken.value}`
        }
      }
    },

    // 2. Intercept errors AFTER receiving a response
    async onResponseError({ request: originalRequest, response, options }) {
      // If the error is 401 and we have a refresh token
      if (response.status === 401 && refreshToken.value) {
        try {
          // Ask Django for a new access token
          // Note: ensure this URL matches your Django Ninja refresh endpoint
          const refreshRes = await $fetch(`${apiBase}/users/token/refresh/`, {
            method: 'POST',
            body: { refresh: refreshToken.value }
          })

          // Save the new access token securely in the cookie
          accessToken.value = refreshRes.access

          // Update the header of the original request with the new token
          options.headers.Authorization = `Bearer ${refreshRes.access}`
          
          // Retry the original request seamlessly
          return $fetch(originalRequest, options)

        } catch (error) {
          console.error('Refresh token failed:', error)
          // If the refresh token is ALSO expired, the user must log in again
          accessToken.value = null
          refreshToken.value = null
          return navigateTo('/login')
        }
      }
    }
  })

  // Execute the request
  return customFetch(request, options)
}