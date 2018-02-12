<template lang="html">
  <div class="answer-actions">

    <span class="answer-vote">
      <button type="button" @click="optVote('up', answerId)"
      :class="{'active': upVoteStatus[answerIndex]}">
        <icon name="sort-up" scale="1.2"></icon>
        {{ vote }}
      </button>
      <button type="button" @click="optVote('down', answerId)"
      :class="{'active': downVoteStatus[answerIndex]}">
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
import {fetchUserVote, fetchAddUserVote, fetchDelUserVote} from '../../api/api'

export default {
  props: ['vote', 'answerId', 'answerIndex'],
  data () {
    return {
      upVoteStatus: [],
      downVoteStatus: [],
    }
  },
  methods: {
    // 赞同 & 反对问题
    optVote (type, id) {
      if (type == 'up') {
        let params = {
          answer: `${id}`,
          vote_type: 'up'
        }
        fetchAddUserVote(params)
        .then (res => {
          this.$set(this.upVoteStatus, this.answerIndex, true)
          this.vote += 1
        })
      } else if (type == 'down') {
        let params = {
          answer: `${id}`,
          vote_type: 'down'
        }
        fetchAddUserVote(params)
        .then (res => {
          this.$set(this.downVoteStatus, this.answerIndex, true)
          this.vote -= 1
        })
      }
    },
    // 获取当前用户 赞同 & 反对问题 列表
    fetchData () {
      fetchUserVote ()
      .then (res => {

        for (let i=0; i < res.data.length; i++) {
          if (this.answerId == res.data[i]["answer"]) {
            if (res.data[i]["vote_type"] == 'up') {
              this.$set(this.upVoteStatus, this.answerIndex, true)
            } else if (res.data[i]["vote_type"] == 'down') {
              this.$set(this.downVoteStatus, this.answerIndex, true)
            }
          }
        }

      })
    },
  },
  created () {
    this.fetchData()
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/answeraction.scss';
</style>
