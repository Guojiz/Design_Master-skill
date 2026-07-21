# Third-party resources

[English](THIRD_PARTY.md) | [简体中文](THIRD_PARTY.zh-CN.md)

Original code in Design Master is licensed under MIT. The projects below are integrated only in the ways described in this file; their names, trademarks, and source code remain the property of their respective owners.

| Resource | License | How this repository integrates it |
|---|---|---|
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | MIT | Adaptation of workflow and runtime ideas; any copied substantial code must retain the original copyright and license |
| [huashu-design](https://github.com/alchaincyf/huashu-design) | MIT | Modular adaptation of design routing, direction selection, and export ideas |
| [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | AGPL-3.0 | No current source code is copied; external invocation or clean-room reimplementation of general design concepts only |
| [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | MIT | Adaptation of HTML deck and presenter ideas; attribution is preserved when substantial code is copied |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT | Adaptation of taste checks and adjustable design dials |
| [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | Prefer its CLI / local query interfaces; the full database is not copied in the first version |
| [Open Design](https://github.com/nexu-io/open-design) | Apache-2.0, with exceptions for bundled resources | Optional CLI / MCP backend; the monorepo is not vendored |
| [Apache ECharts](https://github.com/apache/echarts) | Apache-2.0 | Optional npm dependency |
| [GSAP](https://github.com/greensock/GSAP) | GreenSock custom license | Optional npm dependency; not redistributed as MIT source |
| [Spline](https://spline.design/) | runtime / viewer npm metadata declares no license | Only user-exported scenes, URLs, or user-installed runtimes are used; nothing is vendored |
| [Three.js](https://github.com/mrdoob/three.js) | MIT | Optional npm dependency |

The machine-readable audit snapshot lives in [`docs/UPSTREAMS.lock.json`](docs/UPSTREAMS.lock.json). Before upgrading any third-party resource, check for license changes first, then update the lock file and the integration tests.

Images, videos, copy, and page source from design inspiration websites are not redistributed with this plugin. The plugin stores only source URLs, necessary metadata such as authors, and original analysis, and requires users to follow the original sites' terms and the creators' copyrights.
