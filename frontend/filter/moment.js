import Vue from 'vue'
/** TIME FORMAT BEGIN **/
Vue.filter('moment', function(value) {

  // 计算时间差
  var pubTime = new Date(value);
  var currentTime = new Date();
  var diffTime = currentTime.getTime() - pubTime.getTime();

  // 定义一天、一小时、一分钟
  var aDay = 24*3600*1000;
  var anHours = 3600*1000;
  var aMinutes = 60*1000;

  // 计算差值
  var days = Math.floor(diffTime / aDay);

  var leftHours = diffTime % aDay;
  var hours = Math.floor(leftHours / anHours);

  var leftMinutes = leftHours % anHours;
  var minutes = Math.floor(leftMinutes / aMinutes);

  var leftSeconds = leftMinutes % aMinutes;
  var seconds = Math.round(leftSeconds / 1000);

  if (days >= 30) {
    return pubTime.toISOString().slice(0,10);
  } else if (days >= 7) {
    return parseInt(days / 7) + "周前";
  } else if (days >= 1) {
    return days + "天前";
  } else if (hours >= 1) {
    return hours + "小时前";
  } else if (minutes >= 1) {
    return minutes + "分钟前";
  } else if (seconds >= 1) {
    return seconds + "秒前";
  } else {
    return "来自异次元";
  };

});
/** TIME FORMAT END **/
