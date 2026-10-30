---
name: de-ai-ui
description: Use when building, reviewing, or polishing any web or app UI, landing page, dashboard, or component with an AI coding agent, or when the user says a UI looks AI-generated, cheap, generic, slop, 有 AI 味, 廉价, 没质感, or asks to make it more refined, 精致, 有质感, or 高级.
---

# UI 设计去 AI 味 / De-AI-ify UI

AI 生成的界面露馅，通常不是因为缺功能，而是细节失控：圆角不对心、颜色乱抢、字号乱飞、文案乱加。本 Skill 把 @bruc3van 汇总推荐的 8 位中文设计师在 X 上公开分享的方法，转述整理为**可执行、可检查**的规则、自查清单、工作流和自查脚本。每条规则都标注了来源作者，原帖链接与摘要见 `references/sources.md`。

> 说明：本 Skill 是对公开帖子的**转述与归纳**，不是原文转载；带长 Prompt 的原帖只做要点提炼，完整 Prompt 请到原帖查看。标注 `[本 Skill 补充]` 的内容是为串联规则而加的通用实践，不代表来源作者观点。

## 何时使用 / When to use

- 用 AI 新建或修改界面：落地页、后台、仪表盘、设置页、组件、设计 token。
- 用户反馈「像 AI 做的 / 廉价 / 没质感 / 有 AI 味 / slop / 太 generic」。
- UI 交付前的 review pass（自查）。

## 核心原则 / Core principles

1. **先减后加。** AI 最常见的失败是加太多：多余的说明文字、分割线、图标、标签、阴影、颜色、动效。每个元素先问「能不能不要」。[ZaynHao][dingyi][yanliudreamer]
2. **界面退后，内容出彩。** 界面骨架（按钮、卡片、输入框）默认黑白灰，颜色留给照片、数据和内容本身。[ianneo_ai]
3. **一致性靠系统，不靠手感。** 颜色用成套 token、间距圆角走网格、字号收敛到少数几档、组件复用现有库。[ZaynHao][Kubai087][yanliudreamer]
4. **细节要几何正确。** 嵌套圆角同心、光学对齐、边框粗细全站统一。[Kubai087][ZaynHao][dingyi]
5. **先定义，再动手；先全貌，再逐块改。** 先说清给谁用、解决什么问题、要什么感觉；出完整一版后列问题、排优先级、每轮只改一处。[Xian0063]
6. **不同外观模式单独设计，不做自动转换。** 深色、透明 / Clear 等模式直接套用默认素材会显脏，要单独处理素材与图层。[remixdesigner][ianneo_ai]

## 硬规则速览 / Checkable rules

完整版分篇在 `references/`，此处只列可直接打勾的结论：

### 圆角与边框 → `references/radius-and-borders.md`
- [ ] 嵌套圆角满足 **r = R − p**（内圆角 = 外圆角 − 间距），内外同心；从外往里逐层推。
- [ ] 同层级元素共用同一圆角；计算结果不低于 4px；pill / 圆形保持全圆。
- [ ] padding、gap、radius 落在 4px 网格；有 radius token 时改 token，不硬编码。
- [ ] 连续圆角（超椭圆）只作渐进增强：保留 `border-radius`，再 `@supports` 加 `corner-shape`，不支持的浏览器自动回退。
- [ ] 细线与边框优先 0.5px 且全站统一粗细（低分屏 / 老设备需评估回退，见参考篇）。
- [ ] 圆角、阴影不滥用；禁止卡片左边缘彩色竖线。

### 颜色 → `references/color.md`
- [ ] 界面 chrome 默认黑白灰；品牌色克制使用，颜色优先服务内容。
- [ ] 颜色全部纳入成套色阶 token（如 Radix Colors 的 12 级用途定义），不随手写 hex。
- [ ] 为产品定 3–5 个有辨识度的基础色定调，其余从色阶系统派生。
- [ ] 不用紫 / 紫蓝渐变、渐变按钮、彩色图标雨、一卡一色。

### 字体与中文排版 → `references/typography-cjk.md`
- [ ] 全站字号 ≤ 4 档（最好 3 档），最小 12px；层级不足用字重、颜色、间距补。
- [ ] 避开被用烂的字体与排版套路：见参考篇的 slop 字体名单、全大写小标题、眉标、超大 hero 字。
- [ ] 中文字体栈：先西后中、英文名、带空格加引号、`sans-serif` 兜底（现成写法在参考篇）。
- [ ] 不默认全居中排版；等宽字体只给代码。

### 文案 → `references/copy-and-content.md`
- [ ] 不用中点「·」作分隔符；删冗余解释文字；正文不塞 emoji、标题不顶 emoji 图标。
- [ ] 文案贴合目标人群：易懂、不过度口语化、不随意造词、长度匹配功能场景。
- [ ] 不编造数据与社会证明；图表不过度堆细节；标签 / badge 不泛滥。

### 动效与交互 → `references/motion-and-interaction.md`
- [ ] 动效能少则少；必须加时以 ease-out、约 250ms 为基线，收敛不生硬。
- [ ] 下拉 / 级联菜单要有安全三角区与开关延时；下拉按钮的小箭头要专门检查（样式、尺寸、光学居中、间距）。
- [ ] 拖拽排序要有插入线与由近及远的让位节奏；按钮要有可感知的按下反馈。
- [ ] 减少需要用户停下来判断的交互；必须出现时放在用户本来就要做选择的位置。

### 图标与模式素材 → `references/icons-and-modes.md`
- [ ] 全套图标同一风格体系：线宽、圆角、比例、视觉重量一致。
- [ ] AI 生成图标要「去体积感」：减高光阴影与内发光，阴影用同色相深色而非掺黑。
- [ ] 深色 / Clear 等模式素材单独做，不靠滤镜硬转。

## 工作流 / Workflow

**动手前**
1. 写清：给谁用、解决什么问题、要什么感觉。说不清先提问，这一步不出设计。[Xian0063]
2. 盘点项目已有组件库与 token（颜色 / 圆角 / 间距 / 字号）；没有就先建最小 token 集（`examples/tokens.css`）。
3. 定视觉规则：基础色 + 灰阶系统、≤4 档字号、4px 网格、圆角层级、边框粗细、中文字体栈。

**编码中**
1. 每加一个元素先做减法审查；先出完整页面全貌，不做局部拼补。[Xian0063][yanliudreamer]
2. 方向不确定时一次出 3–4 个方案对比，避免在单一方案上沉没成本式打磨。[yanliudreamer]
3. 反馈用「目标」表达：在截图上标问题、说想要的效果，具体数值让 AI 计算。[Xian0063]

**交付前自查（Review pass）**
1. 逐条过 `references/slop-checklist.md`，按严重程度排序汇报命中项。
2. 可先跑机器初筛：`python3 scripts/audit.py <项目目录>`（查渐变、slop 字体、字号档数、分隔符等可机械检测项）。
3. 每轮只改一处，确认后再改下一处；改圆角时输出 `element: old -> new` 清单。[Xian0063][Kubai087]
4. 至少在 3 种宽度下看截图，并检查深色模式。`[本 Skill 补充，思路转述自 Xian0063 介绍的 Taste Skill]`

## 最小起手 Prompt / Starter prompt

完整版（中 / 英）见 `references/prompts.md`。一句话版（源自 [ianneo_ai]）：

```
界面只用黑白灰，颜色留给照片和内容。
```

## 参考文件 / References

| 文件 | 内容 |
|---|---|
| `references/sources.md` | 主帖 + 15 条来源帖链接、作者与要点摘要 |
| `references/slop-checklist.md` | AI slop 自查清单（交付前逐项打勾） |
| `references/radius-and-borders.md` | 圆角公式、超椭圆、0.5px 与回退 |
| `references/color.md` | 黑白灰 chrome、成套色阶、3–5 基础色 |
| `references/typography-cjk.md` | 字号层级、slop 字体、中文 font-family |
| `references/copy-and-content.md` | 文案与内容规则 |
| `references/motion-and-interaction.md` | 动效基线、级联菜单、拖拽、按钮手感、下拉箭头 |
| `references/icons-and-modes.md` | 图标一致性与去体积感、多模式素材 |
| `references/workflow-and-resources.md` | 8 条审美原则、10 个资源、5 个同类 Skill 的选用 |
| `references/prompts.md` | 本 Skill 自撰的可复制 Prompt（中 / 英） |
| `examples/tokens.css` | 最小 token 集（颜色 / 圆角 / 字号 / 字体栈） |
| `examples/before-after.css` | 典型 slop 写法 → 修正写法对照 |
| `scripts/audit.py` | 可机械检测项的初筛脚本（stdlib，无依赖） |
