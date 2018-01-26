import axios from 'axios'

const baseUrl = 'http://localhost:8000/api/v1/'

// 获取问题列表
export const getQuestions = () => { return axios.get(`${baseUrl}questions/`) }

// 获取回答列表
export const getAnswers = () => { return axios.get(`${baseUrl}answers/`) }
