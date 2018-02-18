<template lang="html">
  <div id="dashboard-wrapper">
    <section id="dashboard">

      <!-- DASHBOARD NAV BEGIN -->
      <div id="dashboard-nav">
        <button type="button" @click="questionShow">
          <icon name="edit" scale="1"></icon>
          提问
        </button>
        <router-link :to="`question`" target="_blank">
          <icon name="file-text-o" scale="1"></icon>
          回答
        </router-link>
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
            <form @submit.prevent="questionSubmit">
              <div class="input-container" :class="{'is-focus':focus==='title'}">
                <textarea aria-expanded="false" placeholder="问题标题" v-model="questionForm.title"
                v-focus='focus==="title"' @click="toggleFocus('title')">
                </textarea>
              </div>
              <div class="input-container input-topic" :class="{'is-focus':focus==='topic'}">
                <input type="text" placeholder="添加话题" v-model="topicText"
                v-focus='focus==="topic"' @click="toggleFocus('topic'), selectTopic()">
                <icon name="search" scale="1" class="topic">
                </icon>
                <div class="topic-select" v-if="focus==='topic' && topics">
                  <div v-for="(topic, index) of topics" :key="index"
                  @click="questionForm.topic=topic.id, topicText=topic.name">
                    {{ topic.name }}
                  </div>
                </div>
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
import { directive as onClickaway } from 'vue-clickaway'

import { fetchTopic, fetchQuestionPost } from '../../api/api'

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
      topicText: '',
      focus: '',
      topics: [],
    }
  },
  methods: {
    questionShow () {
      this.showQuestion = true
      this.focus = 'title'
    },
    questionHide () {
      this.showQuestion = false
    },
    toggleFocus (div) {
      this.focus = div
    },
    selectTopic () {
      if (this.topics == false) {
        fetchTopic()
        .then (res => {
          this.topics = res.data.results
        })
      }
    },
    // 提交问题
    questionSubmit () {
      fetchQuestionPost (this.questionForm)
      .then (res => {
        this.showQuestion = false
        this.$toasted.show(`发布问题成功!`, { duration: 3000, position: "bottom-right", })
      })
      .catch (err => {
        this.$toasted.show(`问题发布失败!`, { duration: 3000, position: "bottom-right", })
      })
    }
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
