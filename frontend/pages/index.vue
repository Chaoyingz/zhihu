<template>
  <div id="main-container">
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
          <h2>{{ answer.question }}</h2>
        </div>

        <div class="answer-content">
          <span>{{ answer.text }}</span>
          <button type="button">阅读全文</button>
        </div>

        <div class="answer-actions">

          <span class="answer-vote">
            <button type="button">
              <icon name="sort-up" scale="1.2"></icon>
              {{ answer.vote }}
            </button>
            <button type="button">
              <icon name="sort-down" scale="1.2"></icon>
            </button>
          </span>

          <button type="button" class="answer-comment">
            <icon name="comment" scale="1"></icon>
            <span> 1 条评论</span>
          </button>

          <div class="answer-share">
            <icon name="send" scale="0.9"></icon>
            分享
          </div>

          <button type="button" class="answer-collection">
            <icon name="star" scale="1"></icon>
            收藏
          </button>

          <button type="button" class="answer-thank">
            <icon name="heart" scale="0.9"></icon>
            感谢
          </button>

          <button type="button" class="answer-more">
            <icon name="ellipsis-h" scale="0.9"></icon>
          </button>

        </div>

      </div>
      <!-- RECOMMEND ANSWER END -->

      <div class="recommend" v-if="!(recommendList && recommendList.length)">
        <span>还没有相关的提问...</span>
      </div>

    </main>
    <!-- RECOMMEND LIST END -->

  </div>
</template>

<script>
import {getAnswers} from '../api/api'
import DashBoard from '../components/DashBoard'
export default {
  layout: 'home',
  head: {
    title: "首页 - 知乎"
  },
  components: {
    DashBoard,
  },
  data () {
    return {
      recommendList: []
    }
  },
  methods: {
    // 获取回答JSON
    fetchData () {
      getAnswers()
      .then (res => {
        this.recommendList = res.data.results
      })
      .catch (err => {

      })
    },

  },
  created () {
    this.fetchData ()
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</style>
