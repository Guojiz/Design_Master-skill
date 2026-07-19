# Design Master

[English](README.md) | [简体中文](README.zh-CN.md)

Design Master 是一个资源优先的 AI 设计编排插件。它先研究参考案例并提炼可执行设计系统，再生成响应式页面、HTML 演示、数据看板、动效或按需 3D，最后统一执行审美、UX、无障碍、响应式和性能检查。

当前版本是 `0.1.0` 基础架构，不是一个把动画和 3D 强塞进所有页面的模板生成器。

## 已完成

- 六个指定开源 Skill 的源码、版本、依赖和许可证审计
- Claude Design、Open Design 与四个前端引擎的接入边界
- 国内外设计网站的可查询资源索引
- 参考研究 → 设计 DNA → 页面生成 → Skill 封装 → 编辑器的提示词流程
- page / deck / dashboard / motion / 3D 统一路由
- ECharts、GSAP、Spline、Three.js 条件调用模板
- taste + UI/UX + accessibility + responsive + performance 质量门
- 可执行的引擎选择器与 JSON Schema

## 目录

```text
.codex-plugin/plugin.json       Codex 插件清单
skills/design-master/           主 Skill、参考资料、schema 与脚本
docs/RESOURCE_RESEARCH.md       资源研究报告
docs/UPSTREAMS.lock.json        固定的上游版本与许可证
THIRD_PARTY.md                  第三方接入与再发布边界
```

## 使用

安装为 Codex 插件后，可以直接提出：

- “先研究三个高相关参考，再为我的 AI 产品做落地页。”
- “把这份内容做成 12 页 HTML 发布会演示，数据页用真实图表。”
- “分析这个 URL 和截图，输出设计规范，再按规范重做页面。”
- “审查现有 HTML 的模板感、层级、响应式、无障碍和动效。”

运行确定性引擎选择器：

```bash
python3 skills/design-master/scripts/plan_artifact.py request.json --pretty
```

完整调查结论见 [资源研究报告](docs/RESOURCE_RESEARCH.md)。

## 原则

- 不从零重复造轮子，但也不把许可证不兼容的代码换名复制。
- 不先做页面再补理由；先把参考规律固化成设计系统。
- 不逢页面必加动画、图表或 3D。
- 不用假数据制造“高级感”。
- 编辑模式和播放模式隔离，导出物保持干净。

## 许可证

本仓库原创内容采用 MIT。第三方项目和运行时保留各自许可证，详见 [THIRD_PARTY.md](THIRD_PARTY.md)。
