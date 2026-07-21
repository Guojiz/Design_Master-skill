# Four-stage prompt pipeline

## Contents

- [State model](#state-model)
- [Phase 1: analyze references](#phase-1-analyze-references)
- [Phase 2: generate the artifact](#phase-2-generate-the-artifact)
- [Phase 3: package the design system](#phase-3-package-the-design-system)
- [Phase 4: add lightweight editing](#phase-4-add-lightweight-editing)
- [Direction gate](#direction-gate)
- [Failure handling](#failure-handling)

## State model

Use four explicit states so later work cannot silently ignore earlier decisions:

```text
REFERENCES → DESIGN_SYSTEM → ARTIFACT → EDITABLE_ARTIFACT
```

Persist the outputs of each completed state. Never jump from references to final code without a written design system unless the user explicitly provides a complete one.

Use these variables in the templates:

- `{{input_materials}}`: URLs, screenshots, images, HTML, copy, data and brand assets.
- `{{project_type}}`: page, deck, dashboard, motion or 3d.
- `{{audience}}`: intended audience and context.
- `{{delivery_target}}`: HTML, project source, PPTX, PDF or other requested format.
- `{{constraints}}`: stack, dimensions, brand rules, browser support, deadline and performance budget.
- `{{design_system}}`: the accepted Phase 1 output.

## Phase 1: analyze references

Use this prompt after collecting supplied and researched references:

```markdown
你是一名专业的前端网站与产品视觉设计师。

请分析以下网站、截图、图片或 HTML：
{{input_materials}}

项目类型：{{project_type}}
目标受众：{{audience}}
约束：{{constraints}}

请区分“可以直接观察到的事实”和“基于事实的推断”，并拆解：

1. 配色：角色、色值、对比、使用比例与状态色
2. 字体：字体家族、字号、字重、行高、字距、行长和层级
3. 布局：容器、网格、列数、间距、对齐、留白与响应式断点
4. 图像：内容类型、比例、裁切、材质、色调和艺术指导
5. 组件：导航、卡片、按钮、表单、标签、表格、图表和反馈状态
6. 表面：圆角、边框、阴影、模糊、纹理与层级
7. 节奏：首屏、章节顺序、信息密度、重复与变化
8. 动效：触发条件、持续时间、缓动、编排、交互目的与降级方式
9. 可访问性：对比度、键盘、焦点、语义、文本替代和 reduced motion
10. 反例：哪些元素只适合原案例，不应复制到当前项目

不要只做抽象评价。请输出：

- 参考来源与观察证据
- 共同规律、差异与取舍
- 可直接执行的 Markdown 设计规范
- 一组工具中立的 design tokens
- 组件规则、图表规则、动画原则和响应式规则
- 需要用户确认的唯一关键分歧；没有关键分歧则明确写“无需确认”
```

Phase 1 completion gate:

- Every rule must be measurable, selectable or directly implementable.
- Cite each external reference URL.
- Do not claim an exact font, framework or animation library unless evidence supports it.
- Do not copy source code, protected imagery or marketing copy from the references.

## Phase 2: generate the artifact

Use the accepted design system verbatim as the source of truth:

```markdown
你是一名负责交付的资深前端设计工程师。

请根据以下内容制作完整、可交互且符合交付目标的 {{project_type}}：
{{input_materials}}

严格遵守这套设计规范：
{{design_system}}

交付目标：{{delivery_target}}
工程与性能约束：{{constraints}}

要求：

1. 先列出内容结构与所用组件，再实现。
2. 只在内容确有需要时调用 ECharts、GSAP、Spline 或 Three.js。
3. 不得添加与内容无关的动画、3D、装饰性图表或虚构数据。
4. 页面必须响应式；演示必须使用固定逻辑舞台等比缩放，两者不得混用。
5. 动效和 3D 必须提供 reduced-motion / 静态降级。
6. 保留语义 HTML、键盘访问、可见焦点、足够对比和合理点击区域。
7. 使用真实内容和用户素材；缺失素材使用明确占位并记录，不伪造事实。
8. 完成后按设计规范逐项自检，修复阻塞问题再交付。
```

Phase 2 completion gate:

- Render or run the result, not just inspect source.
- Verify at representative desktop and mobile sizes; add deck viewport checks for presentations.
- Verify console output, missing assets, keyboard path and reduced-motion behavior.
- Keep a dependency inventory with reason and version for every optional engine.

## Phase 3: package the design system

Use this only after the Phase 2 artifact has been rendered and accepted:

```markdown
请把这套已经验证过的 HTML 设计系统封装为可复用 Skill。

输入：
- 已验证的设计规范与 tokens
- 已验证的页面 / 演示源码
- 组件、图表、动效与响应式测试结论

Skill 必须保存：

1. 整体视觉风格与适用 / 不适用场景
2. 工具中立 design tokens
3. 配色、字体、留白、网格与组件规则
4. 图表选型、数据诚信和无障碍规范
5. 动画触发、持续时间、缓动、强度与降级原则
6. 封面页、数据页、功能页、案例页、总结页等常用模板契约
7. 输入主题、内容、图片和数据时的生成流程
8. 质量门、测试方法、许可证与来源约束

保持 SKILL.md 简洁，把详细规则放入 references，把可复制模板放入 assets，把确定性操作放入 scripts。不得保存用户机密、一次性内容或未经授权的第三方资产。
```

Packaging gate:

- Use only `name` and `description` in SKILL.md frontmatter.
- Keep the main Skill under 500 lines and use progressive disclosure.
- Include only reusable artifacts proven by Phase 2.
- Validate the Skill and every bundled script.

## Phase 4: add lightweight editing

Use this after the base artifact and animation work correctly:

```markdown
请为现有 HTML 增加轻量可视化编辑功能，同时保持播放与导出结果不变。

必须支持：

- 点击文字修改内容
- 替换图片并保持裁切规则
- 在允许自由布局的画布中拖拽元素
- 通过侧边栏修改字体、颜色、字号、间距和动画 token
- 页面复制、组件删除、撤销 / 恢复和导出 HTML

架构要求：

1. 编辑控件只存在于独立 editor overlay；播放模式自动隐藏。
2. 响应式网页不允许默认任意坐标拖拽；拖拽必须转换成网格顺序、对齐或受约束尺寸。
3. deck / 自由画布可使用绝对定位，但必须吸附网格并保留键盘微调。
4. 编辑操作写入可序列化 command history，支持 undo / redo。
5. 导出前移除 editor 状态、临时属性、选择框和调试代码。
6. 不包裹或重写动画目标 DOM，避免破坏原 GSAP / CSS 时间轴。
7. 所有控件可通过键盘操作，并有可见焦点和文本标签。
```

Editor completion gate:

- Toggle edit/play repeatedly without layout drift.
- Undo and redo text, image, token, duplicate and delete operations.
- Export, reopen the exported HTML, and verify no editor UI remains.
- Verify existing animation timelines and responsive rules still work.

## Direction gate

For open-ended greenfield work, produce three actual previews with the same content and structure so the visual variable is isolated. Each direction must differ materially in typography, grid, image treatment, surface and motion—not just accent color.

Skip the direction gate when any of these is true:

- The user supplied a complete design system and asked for faithful implementation.
- The task is image-to-code or exact reference reproduction.
- The task is a narrow repair or audit.
- The user explicitly asked to proceed with one named direction.

Record the reason when skipping.

## Failure handling

- If a URL cannot be accessed, continue with supplied screenshots or HTML and label the limitation.
- If brand assets are missing, use neutral placeholders and request only the single asset that blocks fidelity.
- If data is missing, design the structure with explicit schema placeholders; do not invent figures.
- If an engine cannot load, preserve content and interaction through the documented fallback.
- If a license is incompatible or missing, use an external adapter or reimplement the general behavior without copying source.
