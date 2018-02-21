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
          <a href="/" @click="active = 'home'" :class="{'active': active == 'home'}">首页</a>
          <router-link :to="`question`" @click="active = 'discover'" :class="{'active': active == 'discover'}">发现</router-link>
        </nav>
        <!-- NAV BAR END -->

        <!-- SEARCH BAR BEGIN -->
        <div id="searchbar">
          <form :class="{'active': searchActive}" @click="searchActive=true" v-on-clickaway="hideSearch">
            <input type="text" placeholder="搜索你感兴趣的内容..." v-model="searchText">
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
            <button type="button" @click="show('message')"  title="未开发">
              <icon name="bell" scale="1.3"></icon>
            </button>
          </div>
          <div class="accountbar-icon">
            <button type="button" @click="show('letter')"  title="未开发">
              <icon name="commenting" scale="1.3"></icon>
            </button>
          </div>
          <div class="accountbar-icon" @click="show('account')"  title="未开发 可退出">
            <button type="button">
              <icon name="user" scale="1.3"></icon>
            </button>
          </div>
        </div>
        <!-- ACCOUNT BAR END -->

      </div>
    </header>

    <span id="info-container">

        <!-- MESSAGE BEGIN -->
        <transition
          name="custom-classes-transition"
          enter-active-class="animated fadeIn"
          leave-active-class="animated fadeOut"
        >
        <div class="message" v-if="showMessage" v-on-clickaway="hideMessage">
          <div class="message-content">
            <div class="message-empty">
              <icon name="bell-o" scale="4"></icon>
              <div class="">
                还没有消息
              </div>
            </div>
          </div>
          <div class="message-footer">
            <a href="">
              <icon name="cog" scale="1.2"></icon>
              设置
            </a>
            <a href="">查看全部提醒</a>
          </div>
        </div>
        </transition>
        <!-- MESSAGE END -->

        <!-- LETTER BEGIN -->
        <transition
          name="custom-classes-transition"
          enter-active-class="animated fadeIn"
          leave-active-class="animated fadeOut"
        >
        <div class="letter" v-if="showLetter" v-on-clickaway="hideLetter">
          <div class="letter-content">
            <div class="letter-empty">
              <icon name="commenting-o" scale="4"></icon>
              <div class="">
                还没有私信
              </div>
            </div>
          </div>
          <div class="letter-footer">
            <a href="">
              <icon name="pencil" scale="1.1"></icon>
              设置
            </a>
            <a href="">查看全部私信</a>
          </div>
        </div>
        </transition>
        <!-- LETTER END -->

        <!-- ACCOUNT BEGIN -->
        <transition
          name="custom-classes-transition"
          enter-active-class="animated fadeIn"
          leave-active-class="animated fadeOut"
        >
        <div class="account" v-if="showAccount" v-on-clickaway="hideAccount">
          <a href="#">
            <icon name="user" scale="1"></icon>
            我的主页
          </a>
          <a href="#">
            <icon name="cog" scale="1"></icon>
            设置
          </a>
          <a href="#" @click="loginOut">
            <icon name="power-off" scale="1"></icon>
            退出
          </a>
        </div>
        </transition>
        <!-- ACCOUNT END -->

    </span>

  </div>
</template>

<script>
import {mapActions} from 'vuex'
import { directive as onClickaway } from 'vue-clickaway'

import {fetchSearch} from '../../api/api'
export default {
  data () {
    return {
      showMessage: false,
      showLetter: false,
      showAccount: false,
      active: 'home',
      searchText: '',
      searchActive: false,
    }
  },
  methods: {
    ...mapActions(['userLogout']),
    show (div) {
      if (div == 'message') {
        this.showMessage = true
      } else if (div == 'letter') {
        this.showLetter = true
      } else {
        this.showAccount = true
      }
    },
    hideMessage() {
      this.showMessage = false
    },
    hideLetter() {
      this.showLetter = false
    },
    hideAccount() {
      this.showAccount = false
    },
    loginOut () {
      this.$store.dispatch('userLogout')
      this.$router.push('/signup')
      this.$toasted.show(`用户退出成功!`, { duration: 3000, position: "bottom-right", })
    },
    hideSearch () {
      this.searchActive = false
    }
  },
  directives: {
    onClickaway: onClickaway,
  },
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/animate.css';
@import '../../assets/css/header.scss';
</style>
