<template>
  <div id="main-container">

    <!-- QUESTION BEGIN -->
    <div id="question-header">
      <div class="inner">

        <div class="question-content">
          <div class="question-content-main">
            <div class="question-tag">
              <span>{{ question.topic_name }}</span>
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
                <strong>{{ question.flows }}</strong>
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
            <button type="button" v-show="!isFlow" @click="flowQuestion">关注问题</button>
            <button type="button" v-show="isFlow" @click="flowQuestion">已关注</button>
            <button type="button" @click="isWrite=true">
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

        <span v-if="isWrite">
          <div id="edit">
            <div class="edit-header">
              <div class="username">
                <span>{{ username }}</span>
              </div>
              <button type="button" v-if="!answer.anonymous" @click="answer.anonymous=true">
                使用匿名身份回答
              </button>
              <button type="button" v-if="answer.anonymous" @click="answer.anonymous=false">
                使用实名身份回答
              </button>
            </div>
            <form @submit.prevent="publishAnswer">
              <textarea placeholder="写回答..." v-model="answer.text"></textarea>
              <div class="submit">
                <button type="submit">提交回答</button>
              </div>
            </form>
          </div>
        </span>

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

          <div class="author-info" v-if="!answer.anonymous">
            <div>{{ answer.author_name }}</div>
            <div>{{ answer.author_desc }}</div>
          </div>
          <div class="author-info" v-if="answer.anonymous">
            <div>匿名用户</div>
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
            <AnswerAction :vote="answer.vote" :answerId="answer.id" :answerIndex="index"
            :voteStatus="voteStatus">
            </AnswerAction>
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
import {fetchQuestionDetail, fetchUserVote, fetchFlowQuestion, fetchAnswerPost,
        fetchFlowQuestionPost, fetchFlowQuestionDelete, } from '../../api/api'
import AnswerAction from '../../components/Home/AnswerAction'
export default {
  layout: 'home',
  components: {
    AnswerAction,
  },
  computed: {
    username () {
      return this.$store.state.userInfo.username
    }
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
      voteStatus: [],
      isFlow: false,
      isWrite: false,
      answer: {
        text: '',
        status: 'published',
        anonymous: false,
        question: this.$route.params.id,
      }
    }
  },
  methods: {
    fetchData () {
      fetchUserVote(this.$route.params.id)
      .then (res => {
        this.voteStatus = res.data
      })
      fetchFlowQuestion(this.$route.params.id)
      .then(res => {
        this.isFlow = true
      })
      .catch(err => {
        this.isFlow = false
      })
      fetchQuestionDetail(this.$route.params.id)
      .then (res => {
        this.question = res.data
        this.title = res.data.title
      })
    },
    pubTime (time) {
      return time.slice(0,10)
    },
    flowQuestion() {
      if (this.isFlow) {
        fetchFlowQuestionDelete(this.$route.params.id)
        this.isFlow = false
        this.question.flows -= 1
      } else {
        const params = {
          question: this.$route.params.id
        }
        fetchFlowQuestionPost(params)
        this.isFlow = true
        this.question.flows += 1
      }
    },
    publishAnswer () {
      fetchAnswerPost(this.answer)
      .then(res => {
        this.isWrite = false
        this.$toasted.show(`回答问题成功!`, { duration: 3000, position: "bottom-right", })
      })
      .catch(err => {
        this.$toasted.show(`回答发布失败!`, { duration: 3000, position: "bottom-right", })
      })
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
