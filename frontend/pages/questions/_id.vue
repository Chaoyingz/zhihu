<template>
  <div id="main-container">

    <!-- QUESTION BEGIN -->
    <div id="question-header">
      <div class="inner">

        <div class="question-content">
          <div class="question-content-main">
            <div class="question-tag">
              <span>{{ question.topic }}</span>
            </div>
            <h1 class="question-title">
              {{ question.title }}
            </h1>
            <div class="question-body">
              {{ question.body }}
            </div>
          </div>
          <div class="question-content-side">
            <div class="question-fllowstatus">
              <button type="button">
                <div>关注者</div>
                <strong>311</strong>
              </button>
              <div class="">
                <div>被浏览</div>
                <strong>{{ question.views }}</strong>
              </div>
            </div>
          </div>
        </div>

        <div class="question-footer">
          <div class="question-button">
            <button type="button">关注问题</button>
            <button type="button">
              <icon name="pencil" scale="0.9"></icon>
              写回答
            </button>
          </div>
        </div>

      </div>
    </div>
    <!-- QUESTION END -->

    <!-- ANSWER BEGIN -->
    <main>
      <div class="inner list">

        <div class="answer-list">
          <div class="answer-header">
            <h4>
              <span>{{ question.answers_count }} 个回答</span>
            </h4>
            <button type="button">
              <span>默认排序　</span>
              <span><icon name="sort" scale="0.9"></icon></span>
            </button>
          </div>

          <div class="answer" v-for="(answer, index) of question.answers"
          :key="index">

          <div class="author-info">
            <div>{{ answer.author }}</div>
            <div>{{ answer.author_desc }}</div>
          </div>

          <div class="answer-vote">
            {{ answer.vote }} 人赞同了该回答
          </div>

          <div class="answer-content">
            <div class="answer-body">
              <span>{{ answer.text }}</span>
            </div>
            <div class="answer-publish">
              <span>发布于 {{ pubTime(answer.publish) }}</span>
            </div>
            <AnswerAction :vote="answer.vote"></AnswerAction>
          </div>

          </div>
        </div>

      </div>
    </main>
    <!-- ANSWER END -->

  </div>
</template>

<script>
import '../../filter/moment.js'
import {getQuestionDetail} from '../../api/api'
import AnswerAction from '../../components/Home/AnswerAction'
export default {
  layout: 'home',
  components: {
    AnswerAction,
  },
  head () {
    const title = this.title
    return {
      title: `${title} - 知乎`
    }
  },
  data () {
    return {
      title: '加载中... ',
      question: [],
    }
  },
  methods: {
    fetchData () {
      getQuestionDetail(this.$route.params.id)
      .then (res => {
        this.question = res.data
        this.title = res.data.title
      })
    },
    pubTime (time) {
      return time.slice(0,10)
    }
  },
  created () {
    this.fetchData ()
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/question-detail.scss';
</style>
