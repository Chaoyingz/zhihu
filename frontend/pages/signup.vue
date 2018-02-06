<template lang="html">
  <main>
    <div id="signup">
      <div id="signup-container">

        <div class="signup-header">
          <img src="~assets/images/logo.svg" alt="知乎">
          <div v-show="isLoginPage">
            登陆知乎，发现更大的世界
          </div>
          <div v-show="!isLoginPage">
            注册知乎，发现更大的世界
          </div>
        </div>

        <div class="login-content" v-show="isLoginPage">
          <form @submit.prevent="login">
            <input type="text" v-model="loginInfo.username" placeholder="手机号或邮箱">
            <input type="password" v-model="loginInfo.password" placeholder="密码">
            <div class="login-options">
              <button type="button">手机验证码登陆</button>
              <button type="button">忘记密码</button>
            </div>
            <button type="submit">登陆</button>
          </form>
        </div>

        <div class="register-content" v-show="!isLoginPage">
          <form @submit.prevent="register">
            <div class="register-mobile">
              <button type="button">
                中国 +86
                <icon name="sort" scale="0.9"></icon>
              </button>
              <span class="SignFlow-accountSeperator">&nbsp;</span>
              <input type="text" v-model="registerInfo.mobile" placeholder="手机号">
            </div>
            <input type="code" v-model="registerInfo.code" placeholder="验证码">
            <div class="login-options">
              <button type="button">接收语音验证码</button>
            </div>
            <button type="submit">注册</button>
          </form>
        </div>

        <div class="signup-switch">
          <div v-show="isLoginPage" @click="pageSwitch">
            没有账号?
            <span> 注册</span>
          </div>

          <div v-show="!isLoginPage" @click="pageSwitch">
            已有帐号?
            <span> 登陆</span>
          </div>
        </div>

      </div>
    </div>
  </main>
</template>

<script>
import { mapActions } from 'vuex'

import {fetchLogin} from '../api/api'
export default {
  data () {
    return {
        loginInfo: {
          username: '',
          password: ''
        },
        registerInfo: {
          mobile: '',
          code: ''
        },
        isLoginPage: true,
    }
  },
  methods: {
    ...mapActions(['userLogin']),
    login () {
      let self = this
      fetchLogin (this.loginInfo)
      .then (res => {
        localStorage.setItem('username', this.user.username)
        localStorage.setItem('token', res.data.token)
        this.$store.dispatch('userLogin')
        self.$router.push('/')
      })
      .catch (err => {

      })
    },
    pageSwitch () {
      this.isLoginPage = !this.isLoginPage
    }
  },
}
</script>

<style lang="scss" scoped>
@import '../assets/css/signup.scss';
</style>
