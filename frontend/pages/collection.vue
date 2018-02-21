<template lang="html">
  <div>
    <div class="inner">
      <section id="collection">
        <div v-if="!favs">
          还没有任何收藏
        </div>
        <div v-for="(fav, index) of favs" :key="index" id="fav">
          <h2><router-link :to="`questions/${fav.id}`" target="_blank">
            {{ fav.question_title }}
          </router-link></h2>
          <div class="author">
            <span class="vote">{{ fav.answer_vote }}</span>
            <span class="useranme">{{ fav.author_name }}</span>
          </div>
          <div class="text">
            <span>{{ fav.answer_text }}</span>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { fetchfav } from '../api/api'
export default {
  layout: 'home',
  data () {
    return {
      favs: []
    }
  },
  methods: {
    fetchData() {
      fetchfav()
      .then(res => {
        this.favs = res.data
      })
    },
  },
  created () {
    this.fetchData()
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/css/collection.scss';
</style>
