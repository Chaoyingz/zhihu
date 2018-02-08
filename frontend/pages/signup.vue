<template lang="html">
  <main>
    <div id="signup">
      <div id="signup-container">

        <!-- FORM HEADER BEGIN -->
        <div class="signup-header">
          <img src="~assets/images/logo.svg" alt="知乎">
          <div v-show="isLoginPage">
            登陆知乎，发现更大的世界
          </div>
          <div v-show="!isLoginPage">
            注册知乎，发现更大的世界
          </div>
        </div>
        <!-- FORM HEADER END -->

        <!-- LOGIN CONTAINER BEGIN -->
        <div class="login-content" v-show="isLoginPage">
          <form @submit.prevent="login">
            <div class="input-container">
              <input type="text" v-model="loginInfo.username" placeholder="手机号或邮箱">
            </div>
            <div class="input-container">
              <input type="password" v-model="loginInfo.password" placeholder="密码">
            </div>
            <div class="form-options">
              <button type="button">手机验证码登陆</button>
              <button type="button">忘记密码？</button>
            </div>
            <button type="submit">登陆</button>
          </form>
        </div>
        <!-- LOGIN CONTAINER END -->

        <!-- REGISTER CONTAINER BEGIN -->
        <div class="register-content" v-show="!isLoginPage">
          <form @submit.prevent="register">

            <div class="input-container register-mobile">
              <button type="button">
                中国 +86
                <icon name="sort" scale="0.9"></icon>
              </button>
              <span class="vertical">&nbsp;</span>
              <div class="register-mobile-input">
                <input type="text" v-model="registerInfo.mobile"
                placeholder="手机号" v-show="!registerMask.mobile"
                v-focus="focus.mobile" @blur="focus.mobile=false">
                <div class="error-mask mobile" v-show="registerMask.mobile || regError.mobile"
                @click="toggleMask('mobile')">
                  <span class="error" v-show="regError.mobile">{{ regError.mobile }}</span>
                  <span v-show="registerMask.mobile">请输入手机号</span>
                </div>
              </div>
            </div>

            <div class="input-container register-code">
              <div class="register-code-input" v-show="!registerMask.code">
                <input type="code" v-model="registerInfo.code"
                placeholder="验证码" v-focus="focus.code"
                @blur="focus.code=false">
              </div>
              <div class="error-mask" v-show="registerMask.code"
              @click="toggleMask('code')">
                <span>请输入短信验证码</span>
              </div>
              <button class="show" type="button" @click="fetchSms" v-show="codeBtn">
                获取短信验证码
              </button>
              <button type="button" v-show="!codeBtn" class="hide">
                {{ timeInterval }}秒后可重发
              </button>
            </div>
            <div class="form-options">
              <button type="button">接收语音验证码</button>
            </div>
            <button type="submit">注册</button>
          </form>
        </div>
        <!-- REGISTER CONTAINER END -->

        <!-- SWITCH CONTAINER BEGIN -->
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
        <!-- SWITCH CONTAINER END -->

      </div>
    </div>
  </main>
</template>

<script>
import {mapActions} from 'vuex'

import {fetchLogin, fetchSmsCode} from '../api/api'
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
        registerMask: {
          mobile: true,
          code: true
        },
        isLoginPage: true,
        timeInterval: 60,
        codeBtn: true,
        regError: {
          mobile: '',
          code: '',
        },
        focus: {
          mobile: false,
          code: false,
        },
    }
  },
  methods: {
    ...mapActions(['userLogin']),
    login () {
      let self = this
      fetchLogin (this.loginInfo)
      .then (res => {
        localStorage.setItem('username', res.data.username)
        localStorage.setItem('token', res.data.token)
        this.$store.dispatch('userLogin')
        self.$router.push('/')
      })
      .catch (err => {

      })
    },
    pageSwitch () {
      this.isLoginPage = !this.isLoginPage
    },
    toggleMask (div) {
      if (div === 'mobile') {
        this.registerMask.mobile = false
        this.focus.mobile = true
        this.regError.mobile = ''
      } else if (div === 'code') {
        this.registerMask.code = false
        this.focus.code = true
        this.regError.code = ''
      }
    },
    fetchSms () {
      let params = {
        mobile: this.registerInfo.mobile
      }
      fetchSmsCode (params)
      .then(res => {
        let that = this
        that.codeBtn = false
        let interval = window.setInterval( function() {
          that.timeInterval = that.timeInterval - 1
          if (that.timeInterval <= 0) {
            that.timeInterval = 60;
            that.codeBtn = true;
            window.clearInterval(interval);
          }
        }, 1000);
      })
      .catch(err => {
        this.regError.mobile = err.response.data.mobile[0]
      })
    },
  },
  directives: {
    focus: {
      update: (el, {value}) => {
        if (value) {
          el.focus()
        }
      }
    }
  },
}
</script>

<style lang="scss" scoped>
@import '../assets/css/signup.scss';
</style>
