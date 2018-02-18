<template>
  <main class="question-wrapper">
    <div class="inner">
      <div class="" v-if="!questions">
        还没有任何提问!
      </div>
      <section v-if="questions">
        <div v-for="(question, index) of questions" :key="index">
          <div class="topic">
            来自:
            <a href="#">{{question.topic_name}}</a>
          </div>
          <h2>
            <router-link :to="`questions/${question.id}`" target="_blank">
            {{ question.title }}
            </router-link>
          </h2>
          <div class="answer">
            <span v-if="question.answers_count == 0">还没有回答</span>
            <span v-if="question.answers_count != 0">
              {{ question.answers_count }}个回答
            </span>
            <span class="zg-bull">•</span>
            <span>
              {{ question.flows }}个关注
            </span>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<script>
import { fetchQuestions } from '../api/api'
export default {
  data () {
    return {
      questions: []
    }
  },
  layout: 'home',
  methods: {
    fetchData () {
      fetchQuestions ()
      .then(res => {
        this.questions = res.data.results
      })
    }
  },
  created () {
    this.fetchData()
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/css/question.scss';
</style>
