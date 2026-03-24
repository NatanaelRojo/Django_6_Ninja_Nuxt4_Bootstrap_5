<template>
  <div>
    <h1>
      <img
        src="/images/star.png"
        alt="star"
        class="img-fluid mb-3"
        width="50px"
      >
      Django 6 + Django Ninja + Nuxt 4 + Bootstrap 5
    </h1>
  </div>
</template>

<script setup>
useHead({
  title: 'Home'
})

const loader = useState('loader')

onMounted(() => {
  console.log("Activo el loader")
  loader.value = true

  setTimeout(() => {
    loader.value = false
    console.log("Ha pasado 1 segundo y quité el loader")
  }, 1000)
})
</script>
