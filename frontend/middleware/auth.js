import axios from 'axios'

export default function ({ store, redirect, error }) {
  if (!store.state.isLogin) {
    return redirect('/signup');
  }
}
