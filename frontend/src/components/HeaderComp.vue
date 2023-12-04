<script>
import { RouterLink } from 'vue-router'


</script>
<template>
<div class="bg-gray-100">
  <nav class="container px-6 py-8 mx-auto md:flex md:justify-between md:items-center">
<div class="flex items-center justify-between">
  <Router-link class="text-x1 font-bold text-gray-800 md:text-2x1 hover:text-blue-400" :to="{ name: 'mainView' } ">
    Logo
  </Router-link>
</div>
  <div class="items-center justify-between text-base text-gray-700">
    <Router-link class="text-gray-700 hover:text-blue-400" :to="{ name: 'aboutView' }">
      Sobre
    </Router-link>
  </div>
  <div>
    <Router-link class="text-gray-700 hover:text-blue-400" :to="{ name: 'brasilView' }">
      Brasil Movies
    </Router-link>
  </div>
  <div>
    <Router-link class="text-gray-700 hover:text-blue-400" :to="{ name: 'moviesView' }">
      Movies
    </Router-link>
  </div>
  </nav>

</div>
</template>
  <style scoped> 

</style>