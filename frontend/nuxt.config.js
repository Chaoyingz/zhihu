module.exports = {
  /*
  ** Global CSS
  */
  css: [
    '@assets/css/normalize.css',
    '@assets/css/common.css',
  ],
  /*
  **  Global plugin
  */
  plugins: [
    { src: '~plugins/awesome-icon'},
    { src: '~plugins/vue-toasted', ssr: false},
    { src: '~plugins/vue-clipboard2', ssr: false},
  ],
  /*
  ** Headers of the page
  */
  head: {
    title: '知乎',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'frontend' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  mode: 'spa',
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    },
    vendor: ['vue-awesome', 'axios', 'vue-toasted', 'vue-clipboard2']
  }
}
