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

    <button class="answer-share" @click="shareStatus=!shareStatus">
      <icon name="send" scale="0.9"></icon>
      分享
    </button>

    <div class="answer-share-clip" v-if="shareStatus" v-on-clickaway="hideShare">
      <button type="button" v-clipboard:copy="shareMessage"
      v-clipboard:success="copyLink">
        <icon name="link" scale="0.9"></icon>
        复制链接
      </button>
    </div>

    <button type="button" class="answer-collection" v-if="!isFav" @click="addFav">
      <icon name="star" scale="1"></icon>
      收藏
    </button>

    <button type="button" class="answer-collection" v-if="isFav" @click="delFav">
      <icon name="star" scale="1"></icon>
      已收藏
    </button>

    <button type="button" class="answer-thank" v-show="!thank" @click="thank=true">
      <icon name="heart" scale="0.9"></icon>
      <span>感谢</span>
    </button>

    <button type="button" class="answer-thank"  v-show="thank" @click="thank=false">
      <icon name="heart" scale="0.9"></icon>
      <span>已感谢</span>
    </button>

  </div>
</template>

<script>
import {fetchAddUserVote, fetchDelUserVote, fetchfavpost, fetchfavdel} from '../../api/api'
import { directive as onClickaway } from 'vue-clickaway'

export default {
  props: ['vote', 'answerId', 'answerIndex', 'voteStatus', 'link', 'favStatus'],
  data () {
    return {
      numOfVote: JSON.parse(this.vote),
      upVoteStatus: false,
      downVoteStatus: false,
      shareStatus: false,
      shareMessage: `http://localhost:3000/questions/${this.link}`,
      thank: false,
      isFav: false
    }
  },
  methods: {
    // 获取赞同 / 反对初始状态
    fetchData () {

      for (let i=0; i<this.voteStatus.length; i++) {
        if (this.answerId == this.voteStatus[i]["answer"]) {
          if (this.voteStatus[i]["vote_type"] == 'up') {
            this.upVoteStatus = true
          } else {
            this.downVoteStatus = true
          }
        }
      }

      for (let i=0; i<this.favStatus.length; i++) {
        if (this.answerId == this.favStatus[i]["answer"]) {
          this.isFav = true
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
      if (type == 'up') {
        this.numOfVote += 1
        this.upVoteStatus = true
      } else {
        this.numOfVote -= 1
        this.downVoteStatus = true
      }
      fetchAddUserVote(params)
      .then (res => {
      })
    },

    copyLink () {
      this.shareStatus = !this.shareStatus
      this.$toasted.show(`复制链接成功!`, { duration: 3000, position: "bottom-right", })
    },

    hideShare() {
      this.shareStatus = !this.shareStatus
    },

    addFav () {
      const params = {
        answer: this.answerId
      }
      fetchfavpost(params)
      .then(res => {
        this.isFav = true
        this.$toasted.show(`添加收藏成功!`, { duration: 3000, position: "bottom-right", })
      })
      .catch(err => {
        this.$toasted.show(`添加收藏失败!`, { duration: 3000, position: "bottom-right", })
      })
    },

    delFav () {
      fetchfavdel(this.answerId)
      .then(res => {
        this.isFav = false
        this.$toasted.show(`取消收藏成功!`, { duration: 3000, position: "bottom-right", })
      })
      .catch(err => {
        this.$toasted.show(`取消收藏失败!`, { duration: 3000, position: "bottom-right", })
      })
    },
  },
  created () {
    this.fetchData()
  },
  directives: {
    onClickaway: onClickaway,
  },
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/answeraction.scss';
</style>
