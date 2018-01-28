<template lang="html">
  <div class="answer-actions">

    <span class="answer-vote">
      <button type="button">
        <icon name="sort-up" scale="1.2"></icon>
        {{ vote }}
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
</template>

<script>
export default {
  props: ['vote'],
}
</script>

<style lang="scss" scoped>
@import '../../assets/css/answeraction.scss';
</style>
