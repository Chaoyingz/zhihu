import axios from 'axios'

const baseUrl = 'http://localhost:8000/api/v1/'

const token = process.browser ? JSON.parse(localStorage.getItem('vuex')).userInfo.token : null

// const config = {
//   headers: {'Authorization': 'JWT ' + token}
// }

axios.defaults.headers.common['Authorization'] = `JWT ${token}`

// 获取问题列表
export const fetchQuestions = () => { return axios.get(`${baseUrl}questions/`) }

// 获取回答列表
export const fetchAnswers = () => { return axios.get(`${baseUrl}answers/`) }

// 获取问题详情
export const fetchQuestionDetail = params => {
  return axios.get(`${baseUrl}questions/${params}/`)
}

// 用户登陆
export const fetchLogin = params => {
  return axios.post(`${baseUrl}login/`, params)
}

// 获取验证码
export const fetchSmsCode = params => {
  return axios.post(`${baseUrl}codes/`, params)
}

// 注册
export const fetchRegister = params => {
  return axios.post(`${baseUrl}register/`, params)
}

// 获取当前用户赞同 / 反对问题状态列表
export const fetchUserVote = params => {
  return axios.get(`${baseUrl}votes/?search=${params}`)
}

// 赞同 / 反对回答
export const fetchAddUserVote = params => {
  return axios.post(`${baseUrl}votes/`, params)
}

// 取消赞同反对
export const fetchDelUserVote = params => {
  return axios.delete(`${baseUrl}votes/${params}/`)
}

// 提交问题
export const fetchQuestionPost = params => {
  return axios.post(`${baseUrl}questions/`, params)
}

// 获取话题
export const fetchTopic = () => {
  return axios.get(`${baseUrl}topics/`)
}

// 关注问题列表
export const fetchFlowQuestion = params => {
  return axios.get(`${baseUrl}flow_questions/${params}/`)
}

// 关注问题
export const fetchFlowQuestionPost = params => {
  return axios.post(`${baseUrl}flow_questions/`, params)
}

// 取消关注问题
export const fetchFlowQuestionDelete = params => {
  return axios.delete(`${baseUrl}flow_questions/${params}/`)
}

// 提交回答
export const fetchAnswerPost = params => {
  return axios.post(`${baseUrl}answers/`, params)
}

// 收藏列表
export const fetchfav = () => {
  return axios.get(`${baseUrl}favs/`)
}

// 添加收藏
export const fetchfavpost = params => {
  return axios.post(`${baseUrl}favs/`, params)
}

// 取消收藏
export const fetchfavdel = params => {
  return axios.delete(`${baseUrl}favs/${params}/`)
}

// 获取用户资料
export const fetchUserProfile = () => {
  return axios.get(`${baseUrl}users/`)
}

// 搜索
export const fetchSearch = params => {
  return axios.get(`${baseUrl}questions/?search=${params}`)
}
