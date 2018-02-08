import axios from 'axios'

const baseUrl = 'http://localhost:8000/api/v1/'

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
