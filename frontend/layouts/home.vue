<template>
  <div id="wrapper">
    <HomeHead></HomeHead>
    <div class="inner">
      <nuxt/>
    </div>
  </div>
</template>

<script>
import HomeHead from "../components/HomeHead"
export default {
  components: {
    HomeHead,
  },
}
</script>

<style>
</style>
