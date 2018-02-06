import * as types from './mutation-types'

const actions ={

  userLogin({commit}){
    commit(types.LOGIN_IN);
  },

  userLoginOut({commit}){
    commit(types.LOGIN_OUT)
  }

}

export default actions
