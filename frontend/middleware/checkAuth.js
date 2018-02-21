
export default function ({ isServer, store, redirect}) {

  if (isServer && !req) return

  if (!store.state.isLogin) {
    return redirect('/signup');
  }
  
}
