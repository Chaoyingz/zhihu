import * as types from './mutation-types'

const actions ={

  nuxtServerInit({ commit }, { req }) {
    if (!process.server) {
      commit(types.LOGIN_IN)
    }
  },

  userLogin({commit}, user){
    commit(types.LOGIN_IN, user)
  },

  userLogout({commit}){
    commit(types.LOGIN_OUT)
  }

}

export default actions
