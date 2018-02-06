import Vuex from 'vuex'

import mutations from './mutations'
import actions from './actions'


const state = {
    userInfo: {
      userName: null,
      token: null,
    },
    isLogin: false,
}

const createStore = () => {
  return new Vuex.Store({
    state,
    mutations,
    actions
  })
}

export default createStore
