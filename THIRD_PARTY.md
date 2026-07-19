# Third-party resources

Design Master 的原创代码采用 MIT。下列项目只按本文件所述方式接入；它们的名称、商标和源码仍归各自权利人所有。

| 资源 | 许可证 | 本仓库的接入方式 |
|---|---|---|
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | MIT | 工作流与运行时思想的适配；复制实质代码时必须保留原版权与许可证 |
| [huashu-design](https://github.com/alchaincyf/huashu-design) | MIT | 模块化适配设计路由、方向选择与导出思想 |
| [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | AGPL-3.0 | 不复制当前源码；仅外部调用或清洁复现通用设计概念 |
| [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | MIT | 适配 HTML deck 与 presenter 思想；复制实质代码时保留归属 |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT | 适配审美检查与可调设计旋钮 |
| [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | 优先通过其 CLI / 本地查询接口使用，不在首版复制完整数据库 |
| [Open Design](https://github.com/nexu-io/open-design) | Apache-2.0，捆绑资源有例外 | 可选 CLI / MCP 后端；不 vendor monorepo |
| [Apache ECharts](https://github.com/apache/echarts) | Apache-2.0 | 可选 npm 依赖 |
| [GSAP](https://github.com/greensock/GSAP) | GreenSock 自定义许可 | 可选 npm 依赖；不作为 MIT 源码再发布 |
| [Spline](https://spline.design/) | runtime / viewer npm 元数据未声明 | 只使用用户导出的场景、URL 或安装的运行时，不 vendor |
| [Three.js](https://github.com/mrdoob/three.js) | MIT | 可选 npm 依赖 |

机器可读的审计快照位于 [`docs/UPSTREAMS.lock.json`](docs/UPSTREAMS.lock.json)。升级任何第三方资源前，先检查许可证变化，再更新锁文件和集成测试。

设计灵感网站中的图片、视频、文案和页面源码不随本插件再发布。插件只保存来源 URL、作者等必要元数据以及原创分析，并要求使用者遵守原站条款与作品版权。
