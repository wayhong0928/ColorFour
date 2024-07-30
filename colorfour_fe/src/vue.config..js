const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      }
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        'vue': 'vue/dist/vue.esm-bundler.js'
      }
    },
    define: {
      '__VUE_OPTIONS_API__': true,
      '__VUE_PROD_DEVTOOLS__': false,
      '__VUE_PROD_HYDRATION_MISMATCH_DETAILS__': false
    }
  }
});
