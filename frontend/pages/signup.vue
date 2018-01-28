<template lang="html">
  <main>
    <div id="signup">
      <div id="signup-container">

        <div class="signup-header">
          <img src="~assets/images/logo.svg" alt="知乎">
          <div>
            登陆知乎，发现更大的世界
          </div>
        </div>

        <div class="login-content">
          <form>
            <input type="text" placeholder="手机号或邮箱">
            <input type="text" placeholder="密码">
            <div class="login-options">
              <button type="button">手机验证码登陆</button>
              <button type="button">忘记密码</button>
            </div>
            <button type="submit">登陆</button>
          </form>
        </div>

        <div class="signup-switch">
          <div>
            没有账号?
            <span> 注册</span>
          </div>
        </div>

      </div>
    </div>
  </main>
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
@import '../assets/css/signup.scss';
</style>
