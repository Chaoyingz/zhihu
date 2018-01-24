<template lang="html">
  <div id="head-container">
    <header>
      <div class="inner">

        <!-- LOGO BEGIN -->
        <a href="/" id="logo">
          <img src="~assets/images/logo.svg" alt="知乎">
        </a>
        <!-- LOGO END -->

        <!-- NAV BAR BEGIN -->
        <nav>
          <a href="/">首页</a>
          <a href="#">发现</a>
          <a href="#">话题</a>
        </nav>
        <!-- NAV BAR END -->

        <!-- SEARCH BAR BEGIN -->
        <div id="searchbar">
          <form>
            <input type="text" placeholder="搜索你感兴趣的内容...">
            <div>
              <icon name="search" scale="0.9"></icon>
            </div>
          </form>
          <button type="submit">提问</button>
        </div>
        <!-- SEARCH BAR END -->

        <!-- ACCOUNT BAR BEGIN -->
        <div id="accountbar">
          <div class="accountbar-icon">
            <button type="button">
              <icon name="bell" scale="1.3"></icon>
            </button>
          </div>
          <div class="accountbar-icon">
            <button type="button">
              <icon name="commenting" scale="1.3"></icon>
            </button>
          </div>
          <div class="accountbar-icon">
            <button type="button">
              <icon name="user" scale="1.3"></icon>
            </button>
          </div>
        </div>
        <!-- ACCOUNT BAR END -->

      </div>
    </header>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
@import '../assets/css/header.scss';
</style>
