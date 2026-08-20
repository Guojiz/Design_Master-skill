# Design Master

[English](README.md) | [简体中文](README.zh-CN.md)

<p align="center">
  <a href="https://guojiz.github.io/"><img alt="官网" src="https://img.shields.io/badge/官网-guojiz.github.io-111111?style=flat-square"></a>
  <a href="https://github.com/Guojiz/Sponsors"><img alt="赞助" src="https://img.shields.io/badge/赞助-支持-111111?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://guojiz.github.io/"><strong>作者官网</strong></a>
  · <a href="https://x.com/guojizh">X</a>
  · <a href="https://space.bilibili.com/3493114115263006">哔哩哔哩</a>
  · <a href="https://youtube.com/@guojizh">YouTube</a>
  · <a href="https://github.com/Guojiz/Sponsors">赞助</a>
</p>


Design Master 是一个资源优先的 AI 设计师插件。它先研究参考案例并提炼可执行设计系统，再生成响应式页面、网页演示、数据看板、动效或按需三维体验，最后统一执行审美、用户体验、无障碍、响应式和性能检查。

使用者只需提供目标、内容、图片和数据。Design Master 会自动选择参考来源、提炼设计规范、判断是否调用图表、动效或三维引擎、生成作品并完成质量检查，不需要使用者逐步下达这些命令。

当前版本是 `0.1.0` 基础架构，不是一个把动画和三维效果强塞进所有页面的模板生成器。

## 已完成

- 六个指定开源技能的源码、版本、依赖和许可证审计
- Claude Design、Open Design 与四个前端引擎的接入边界
- 国内外设计网站的可查询资源索引
- 可供直接浏览和收藏的设计资源导览
- 参考研究 → 设计规律 → 页面生成 → 技能封装 → 编辑器的提示词流程
- 响应式网页、演示文稿、数据看板、动效和三维体验的统一路由
- ECharts、GSAP、Spline、Three.js 条件调用模板
- 审美、用户体验、无障碍、响应式和性能质量门
- 可执行的引擎选择器与数据格式规范

## 目录

```text
.codex-plugin/plugin.json       Codex 插件清单
skills/design-master/           主技能、参考资料、数据规范与脚本
docs/RESOURCE_RESEARCH.md       资源研究报告
docs/UPSTREAMS.lock.json        固定的上游版本与许可证
THIRD_PARTY.md                  第三方接入与再发布边界
```

## 使用

安装为 Codex 插件后，可以直接提出：

- “为我的人工智能产品制作一个落地页。”
- “把这份内容做成 12 页发布会演示，数据页使用真实图表。”
- “参考这个网址和截图，重新设计页面。”
- “检查并优化这个现有网站。”

需要时，参考研究、设计规范提炼、引擎选择和质量检查都会自动完成。

运行确定性引擎选择器：

```bash
python3 skills/design-master/scripts/plan_artifact.py request.json --pretty
```

完整调查结论见 [资源研究报告](docs/RESOURCE_RESEARCH.md)。

## 设计资源导览

资源库也可以脱离生成流程，直接作为分类清晰的设计网站收藏夹和导览使用：

- [设计资源导览](docs/DESIGN_RESOURCES.zh-CN.md)
- [Design Resource Guide](docs/DESIGN_RESOURCES.md)

## 原则

- 不从零重复造轮子，但也不把许可证不兼容的代码换名复制。
- 不先做页面再补理由；先把参考规律固化成设计系统。
- 不逢页面必加动画、图表或 3D。
- 不用假数据制造“高级感”。
- 编辑模式和播放模式隔离，导出物保持干净。

## 官网与其它推广

这个仓库可以没有独立产品站。对外入口是作者官网、本 GitHub 仓库，以及下面这些项目。

| | |
| --- | --- |
| **项目页** | https://guojiz.github.io/design-master/ |
| **作者官网** | https://guojiz.github.io/ |
| **X** | https://x.com/guojizh |
| **哔哩哔哩** | https://space.bilibili.com/3493114115263006 |
| **YouTube** | https://youtube.com/@guojizh |
| **赞助** | https://github.com/Guojiz/Sponsors |

### 其它开源项目

- [GitLearnOS](https://guojiz.github.io/gitlearnos/) — 学习者拥有的 Git 记忆
- [Word Snap](https://guojiz.github.io/word-snap/) — 双语单词匹配
- [AI Subtitle Extractor](https://github.com/Guojiz/ai-subtitle-extractor)
- [Design Master](https://github.com/Guojiz/design-master)
- [AI Video Studio](https://github.com/Guojiz/comfyui-minimax-h3-studio)
- [llm-provider-compat](https://github.com/Guojiz/llm-provider-compat)
- [Claude Desktop Tweak Models](https://github.com/Guojiz/claude-desktop-tweak-models)
- 全部项目：[github.com/Guojiz](https://github.com/Guojiz)

## 许可证

本仓库原创内容采用 MIT。第三方项目和运行时保留各自许可证，详见 [THIRD_PARTY.zh-CN.md](THIRD_PARTY.zh-CN.md)。
