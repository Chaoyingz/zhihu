<template>
  <div id="main-container" class="inner">
    <DashBoard></DashBoard>

    <!-- RECOMMEND LIST BEGIN -->
    <main>

      <!-- RECOMMEND ANSWER BEGIN -->
      <div v-for="(answer, index) of recommendList" class="recommend" :key="index"
           v-if="(recommendList && recommendList.length)">

        <div class="feed-title">
          <span>
            热门内容, 来自:
            <span>{{ answer.topic }}</span>
          </span>
        </div>

        <div class="author-info">
          <span>{{ answer.author }}</span>
          <span>{{ answer.author_desc }}</span>
        </div>

        <div class="question-title">
          <h2>
            <router-link :to="`questions/${answer.question_id}`" target="_blank">
              {{ answer.question }}
            </router-link>
          </h2>
        </div>

        <div class="answer-content" v-if="!contentStatus[index]"
        @click="toggleContent(index)">
          <span>{{ cutContent(answer.text) }}</span>
          <button type="button">
            阅读全文
            <icon name="angle-down" scale="1.1"></icon>
          </button>
        </div>

        <!-- TOGGLE CONTENT -->
        <div class="answer-content" v-if="contentStatus[index]">
          <span>{{ answer.text }}</span>
        </div>

        <AnswerAction :vote="answer.vote" :answerId="answer.id" :answerIndex="index"
        :voteStatus="voteStatus">
        </AnswerAction>

      </div>
      <!-- RECOMMEND ANSWER END -->

      <div class="recommend" v-if="!(recommendList && recommendList.length)">
        <span>还没有相关的提问...</span>
      </div>

    </main>
    <!-- RECOMMEND LIST END -->

    <!-- SIDE CONTAINER BEGIN -->
    <section id="side-container">
      <ul class="nav-list">
        <li>
          <a href="#">
            <icon name="star" scale="1"></icon>
            <span>我的收藏</span>
          </a>
        </li>
        <li>
          <a href="#">
            <icon name="question-circle" scale="1"></icon>
            <span>我关注的问题</span>
          </a>
        </li>
        <li>
          <a href="#">
            <icon name="user-plus" scale="1"></icon>
            <span>我的邀请</span>
          </a>
        </li>
      </ul>
    </section>
    <!-- SIDE CONTAINER END -->

  </div>
</template>

<script>
import {fetchAnswers, fetchUserVote} from '../api/api'
import AnswerAction from '../components/Home/AnswerAction'
import DashBoard from '../components/Home/DashBoard'
export default {
  layout: 'home',
  head: {
    title: "首页 - 知乎"
  },
  components: {
    DashBoard,
    AnswerAction,
  },
  data () {
    return {
      recommendList: [],
      contentStatus: [],
      voteStatus: [],
    }
  },
  methods: {
    // 获取回答JSON & 获取回答VOTE状态
    fetchData () {
      fetchUserVote('')
      .then (res => {
        this.voteStatus = res.data
      })
      fetchAnswers()
      .then (res => {
        this.recommendList = res.data.results
      })
    },
    // 问题文本截取
    cutContent (text) {
      if (text.length > 80) {
        return text.slice(0, 80) + '...';
      } else {
        return text;
      }
    },
    // 开关READ MORE
    toggleContent (index) {
      this.$set(this.contentStatus, index, !this.contentStatus[index])
    }
  },
  created () {
    this.fetchData ()
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</style>
