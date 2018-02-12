<template lang="html">
  <div class="answer-actions">

    <span class="answer-vote">
      <button type="button" @click="optVote('up', answerId)">
        <icon name="sort-up" scale="1.2"></icon>
        {{ vote }}
      </button>
      <button type="button" @click="optVote('down', answerId)">
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
</template>

<script>
import {fetchUserVote} from '../../api/api'

export default {
  props: ['vote', 'answerId'],
  methods: {
    // 赞同 & 反对问题
    optVote (type, id) {
      if (type == 'up') {
        let params = {
          answer: `${id}`,
          vote_type: 'up'
        }
        fetchUserVote(params)
        .then (res => {

        })
      } else if (type == 'down') {
        let params = {
          answer: `${id}`,
          vote_type: 'down'
        }
        fetchUserVote(params)
        .then (res => {

        })
      }
    },
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/answeraction.scss';
</style>
