import * as types from './mutation-types'

const actions ={

  nuxtServerInit({ commit }, { req }) {
    if (!process.server) {
      commit(types.LOGIN_IN)
    }
  },

  userLogin({commit}){
    commit(types.LOGIN_IN);
  },

  userLoginOut({commit}){
    commit(types.LOGIN_OUT)
  }

}

export default actions
