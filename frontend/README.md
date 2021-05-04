# distributed-platform

## Project setup


- install [node.js](https://nodejs.org/en/), latest stable will be fine
- `cd frontend`
- `npm install --registry=https://registry.npm.taobao.org` to install dependencies
- Compiles and hot-reloads for development `npm run serve`
- Compiles and minifies for production `npm run build`
- [Vue.js DevTools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd) Chrome Extension may facilitate developing
  > 可以在 Chrome 中直接查看网页上 Vue 组件的层次关系，观察变量状态，非常实用


## Note on Development

推荐使用VS Code作为编辑器，并安装以下插件
- ESLint 语法规范器
  > 本项目配置了较为严格的语法检查，该插件可以在代码中检测不规范的语法并高亮提示，只有修改后才能通过编译
- Vetur vue插件

主要文件：
- `src/views/distributed` 是我们实际开发项目的各个组件
- `routers.js` 给需要单独地址的组件注册 url
- `src/views/dashboard` 内是原本模板提供的组件，可以参考
- 其中 `Index.vue` 是整个项目的顶层组件，其中导入的除了侧边栏等组件外，`dashboard/components/core/View`是主页面，可以根据 url 在`<router-view />`中渲染我们已经注册的各类组件

参考文档：
- vuetify UI库：https://vuetifyjs.com/zh-Hans/




