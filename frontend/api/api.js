import axios from 'axios'

const baseUrl = 'http://localhost:8000/api/v1/'

const token = process.browser ? JSON.parse(localStorage.getItem('vuex')).userInfo.token : null

console.log(token)

const config = {
  headers: {'Authorization': 'JWT ' + token}
}

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
  return axios.get(`${baseUrl}votes/?search=${params}`, config)
}

// 赞同 / 反对回答
export const fetchAddUserVote = params => {
  return axios.post(`${baseUrl}votes/`, params, config)
}

// 取消赞同反对
export const fetchDelUserVote = params => {
  return axios.delete(`${baseUrl}votes/${params}/`, config)
}
