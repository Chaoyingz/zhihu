<template lang="html">
  <div id="dashboard-wrapper">
    <section id="dashboard">

      <!-- DASHBOARD NAV BEGIN -->
      <div id="dashboard-nav">
        <button type="button" @click="questionShow">
          <icon name="edit" scale="1"></icon>
          提问
        </button>
        <a href="#">
          <icon name="file-text-o" scale="1"></icon>
          回答
        </a>
      </div>
      <!-- DASHBOARD NAV END -->

      <a href="#">
        草稿
      </a>

    </section>

    <!-- QUESTION BEGIN -->
    <span v-if="showQuestion">
      <div class="question-wrapper">
        <div class="question-bk" @click="questionHide"></div>

        <div class="question-container">
          <transition
            name="custom-classes-transition"
            enter-active-class="animated fadeIn"
            leave-active-class="animated fadeOut"
          >
          <div class="question-inner">
            <h3>写下你的问题</h3>
            <div class="question-sub">
              描述精确的问题更易得到解答
            </div>
            <form>
              <div class="input-container" :class="{'is-focus':focus==='title'}">
                <textarea aria-expanded="false" placeholder="问题标题" v-model="questionForm.title"
                v-focus='focus==="title"' @click="toggleFocus('title')">
                </textarea>
              </div>
              <div class="input-container" :class="{'is-focus':focus==='topic'}">
                <input type="text" placeholder="添加话题" v-model="questionForm.topic"
                v-focus='focus==="topic"' @click="toggleFocus('topic')">
                <icon name="search" scale="1" class="topic"></icon>
              </div>
              <span>问题描述（可选）：</span>
              <div class="input-container" :class="{'is-focus':focus==='body'}" v-focus='focus==="body"'>
                <textarea aria-expanded="false" placeholder="问题背景、条件、等详细信息"
                v-model="questionForm.body" @click="toggleFocus('body')">
                </textarea>
              </div>
              <div class="anonymous">
                <label for="anonymous-checkbox">
                  <input type="checkbox" id="anonymous-checkbox"
                  v-model="questionForm.anonymous" @click="toggleFocus('')">
                  匿名提问
                </label>
              </div>
              <div class="button-container">
                <button type="submit">提交问题</button>
              </div>

            </form>

            <button type="button" @click="questionHide">
              <icon name="close" scale="1.8"></icon>
            </button>

          </div>
          </transition>
        </div>

      </div>
    </span>
    <!-- QUESTION END -->

  </div>
</template>

<script>
import { directive as onClickaway } from 'vue-clickaway';
export default {
  data () {
    return {
      showQuestion: false,
      questionForm: {
        title: '',
        body: '',
        anonymous: false,
        topic: '',
      },
      focus: '',
    }
  },
  methods: {
    questionShow () {
      this.showQuestion = true
      this.focus = 'title'
      console.log(this.focus)
    },
    questionHide () {
      this.showQuestion = false
    },
    toggleFocus (div) {
      this.focus = div
    },
  },
  directives: {
    onClickaway: onClickaway,
    focus: {
      inserted: function (el, {value}) {
        if (value) {
          el.focus()
        }
      }
    },
  },
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/animate.css';
@import '../../assets/css/dashboard.scss';
</style>
