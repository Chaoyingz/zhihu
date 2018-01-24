<template>
  <div id="main-container">
    <DashBoard></DashBoard>
  </div>
</template>

<script>
import DashBoard from "../components/DashBoard"
export default {
  layout: 'home',
  head: {
    title: '首页 - 知乎'
  },
  components: {
    DashBoard,
  },
}
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</style>
