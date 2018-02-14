import * as types from './mutation-types'

export const mutations = {

  [types.LOGIN_IN] (state, user) {
    state.userInfo = {
      username: user.username,
      token: user.token
    }
    state.isLogin = true
  },

  [types.LOGIN_OUT] (state) {
    state.userInfo = {
      username: null,
      token: null
    }
    state.isLogin = false
  }

}

export default mutations
