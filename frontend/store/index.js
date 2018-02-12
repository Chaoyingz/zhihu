import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

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
    actions,

  })
}

export default createStore
