<template lang="html">
  <div class="answer-actions">

    <span class="answer-vote">
      <button type="button" @click="optVote('up', answerId)"
      :class="{'active': upVoteStatus}">
        <icon name="sort-up" scale="1.2"></icon>
        {{ numOfVote }}
      </button>
      <button type="button" @click="optVote('down', answerId)"
      :class="{'active': downVoteStatus}">
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
import {fetchAddUserVote, fetchDelUserVote} from '../../api/api'

export default {
  props: ['vote', 'answerId', 'answerIndex', 'voteStatus'],
  data () {
    return {
      numOfVote: JSON.parse(this.vote),
      upVoteStatus: false,
      downVoteStatus: false,
    }
  },
  methods: {
    // 获取赞同 / 反对初始状态
    fetchData () {

      for (let i=0; i < this.voteStatus.length; i++) {
        if (this.answerId == this.voteStatus[i]["answer"]) {
          if (this.voteStatus[i]["vote_type"] == 'up') {
            this.upVoteStatus = true
          } else {
            this.downVoteStatus = true
          }
        }
      }

    },
    // 赞同 & 反对问题
    optVote (type) {
      // 赞同
      if (type == 'up') {
        if (this.upVoteStatus) {
          this.upVoteStatus = false
          this.numOfVote -= 1
          fetchDelUserVote(this.answerId)
        } else if (this.downVoteStatus) {
          this.downVoteStatus = false
          this.numOfVote += 1
          fetchDelUserVote(this.answerId)
          .then (res => {
            this.addVote(type)
          })
        } else {
          this.addVote(type)
        }
      // 反对
      } else {
        if (this.downVoteStatus) {
          this.downVoteStatus = false
          this.numOfVote += 1
          fetchDelUserVote(this.answerId)
        } else if (this.upVoteStatus) {
          this.upVoteStatus = false
          this.numOfVote -= 1
          fetchDelUserVote(this.answerId)
          .then (res => {
            this.addVote(type)
          })
        } else {
          this.addVote(type)
        }
      }

    },

    //
    addVote (type) {
      const params = {
        vote_type: type,
        answer: this.answerId
      }
      fetchAddUserVote(params)
      .then (res => {
        if (type == 'up') {
          this.numOfVote += 1
          this.upVoteStatus = true
        } else {
          this.numOfVote -= 1
          this.downVoteStatus = true
        }
      })
    }

  },
  created () {
    this.fetchData()
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/answeraction.scss';
</style>
