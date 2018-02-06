import * as types from './mutation-types'

export const mutations = {

  [types.LOGIN_IN] (state) {
    let uname = localStorage.getItem('username')
    let utoken = localStorage.getItem('token')
    state.userInfo = {
      userName: uname,
      token: utoken
    }
    state.isLogin = true
  },

  [types.LOGIN_OUT] (state) {
    state.userInfo = {
      userName: null,
      token: null
    }
    state.isLogin = false
  }

}

export default mutations
