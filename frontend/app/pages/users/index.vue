<template>
  <div>
    <GoBack /> |

    <h1>Users List</h1>

    <div v-if="error" class="alert alert-danger">
      Error al cargar usuarios. Inténtalo de nuevo.
    </div>

    <table v-else>
      <thead>
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>First name</th>
          <th>Last name</th>
          <th>Role</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.first_name }}</td>
          <td>{{ user.last_name }}</td>
          <td>{{ user.role }}</td>
          <td>
            XXXX
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

// Estado global para controlar el loader
const loader = useState('loader')

// Configuramos el título de la página
useHead({
  title: 'Users list',
})

// Llamada a la API de Backend usando una API de prueba real
const { data: response, pending, error} = await useFetch(`${apiBase}/users/`, {
  lazy: true
})

// Mapeamos los resultados (JSONPlaceholder devuelve un Array directo)
const users = computed(() => response.value || [])

// Observamos 'pending' y asignamos su valor directamente al loader
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
