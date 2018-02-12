import axios from 'axios'

const baseUrl = 'http://localhost:8000/api/v1/'

// const token = localStorage.getItem('token') ? localStorage.getItem('token') : null
// axios.defaults.headers.common['Authorization'] = `JWT ${token}`


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

// 赞同 / 反对回答
export const fetchUserVote = params => {
  return axios.post(`${baseUrl}votes/`, params)
}
