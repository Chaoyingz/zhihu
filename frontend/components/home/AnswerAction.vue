<template lang="html">
  <div class="answer-actions">

    <span class="answer-vote">
      <button type="button" @click="optVote('up', answerId)"
      :class="{'active': selfVoteStatus == 'up'}">
        <icon name="sort-up" scale="1.2"></icon>
        {{ numOfVote }}
      </button>
      <button type="button" @click="optVote('down', answerId)"
      :class="{'active': selfVoteStatus == 'down'}">
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
  props: {vote: Number, answerId: Number, answerIndex: Number,
          voteStatus: {
            type: String,
            default: ''
          },
  },
  data () {
    return {
      numOfVote: JSON.parse(this.vote),
      selfVoteStatus: this.voteStatus
    }
  },
  methods: {
    // 赞同 & 反对问题
    optVote (type, id) {

      if (this.selfVoteStatus) {
        if (this.selfVoteStatus == type) {
          fetchDelUserVote (id)
          .then (res => {
            this.selfVoteStatus = ''
            type == 'up' ? this.numOfVote -= 1 : this.numOfVote += 1
          })
        } else {
          fetchDelUserVote (id)
          .then (res => {
            type == 'up' ? this.numOfVote += 1 : this.numOfVote -= 1
            this.AddUserVote(type, id)
          })
        }
      } else {
        this.AddUserVote(type, id)
      }

    },

    AddUserVote (type, id) {
      let params = {
        "answer": id,
        "vote_type": type
      }
      fetchAddUserVote (params)
      .then (res => {
        this.selfVoteStatus = type
        type == 'up' ? this.numOfVote += 1 : this.numOfVote -= 1
      })
    },

  },
  created () {
    console.log(this.selfVoteStatus)
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/answeraction.scss';
</style>
