<template>
  <div id="app">

    <Header/>

    <div class="body">
      <Aside/>
      <router-view/>
    </div>

  </div>
</template>

<script>
import Header from './components/Header.vue'
import Aside from './components/Aside.vue'

export default {
  name: 'App',
  components: {
    Header,
    Aside
  }
}
</script>

<style scoped>
.body {
  display: flex;
  /* min-height: calc(100vh - 50px); */
}
.body router-view {
  flex: 1;
}
</style>
