let publicPathUrl = ''
let publicApiPathUrl = ''
if (process.env.NODE_ENV !== 'production') {
    publicPathUrl = process.env.VUE_APP_API_BASE_URL + ':' + process.env.PORT
    publicApiPathUrl = process.env.VUE_APP_API_BASE_URL + ':' + process.env.VUE_APP_API_PORT
} else {
    publicPathUrl = process.env.VUE_APP_API_BASE_URL
    publicApiPathUrl = process.env.VUE_APP_API_BASE_URL
}

module.exports = {
  publicPath: publicPathUrl,
  devServer: {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
    },
    historyApiFallback: true,
    proxy: {
        '/api': {
            ws: true,
            changeOrigin: true,
            target: publicApiPathUrl,
        },
    },
  },

  transpileDependencies: ['vuetify'],

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false,
    },
  },
}
