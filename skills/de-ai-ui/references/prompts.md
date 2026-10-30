# 可直接复制的 Prompt / Copy-paste prompts

以下 Prompt 是**本 Skill 依据各来源规则自撰**的合并版（不是任何原帖 Prompt 的转载）。带长 Prompt 的原帖（@Kubai087 的圆角 / 按钮 / 菜单 / 拖拽各篇、@ZaynHao 的 10 条）请到 `sources.md` 的链接里复制原文使用。

## 1. 合并版（中文，重做界面用）

```
请按下面的「去 AI 味」规则重做我指定的页面 / 组件。项目已有 design token 或组件库时，改 token、复用组件，不要硬编码、不要新造组件：

1. 颜色：界面骨架（按钮、卡片、输入框、导航）只用黑白灰，颜色留给照片和内容；其余颜色纳入成套色阶 token（如 Radix Colors）并按用途等级使用。不要紫 / 紫蓝渐变、渐变按钮、彩色图标、卡片左边缘彩色竖线。
2. 字号：最多 4 种、最好 3 种，最小 12px；层级不够用字重、颜色、间距解决。不要全大写小标题、标题上方眉标、超大 hero 字；避开 Instrument Serif、Space Grotesk、Bricolage Grotesque；等宽字体只给代码。
3. 圆角：嵌套满足 内圆角 = 外圆角 − 间距，同层同圆角，最小 4px，pill / 圆形保持全圆；padding、gap、radius 在 4px 网格上。连续圆角用 @supports (corner-shape: superellipse(1.25)) 做渐进增强，保留 border-radius 回退。
4. 边框：细线统一 0.5px；去掉多余分割线、多层阴影、半透明叠色、带边框容器和卡片套卡片。
5. 文案：删中点「·」分隔符和冗余解释文字；正文不用 emoji；文案贴合目标用户，不过度口语化、不造词；不编造数据与社会证明。
6. 动效：能少则少；必须加时 ease-out、约 250ms；下拉菜单的箭头要与图标风格一致、光学居中。
7. 中文字体栈：先西后中、英文名、带空格加引号、sans-serif 兜底。
8. 图标：全套同一风格体系；深色 / 透明模式的素材单独处理，不要滤镜硬转。

改完后输出：① 圆角变更清单 element: old -> new；② 本次消除的 slop 项（对照清单逐项说明）；③ 还没改的命中项及原因。
```

## 2. 只审查不改（中文）

```
用「去 AI 味」清单审查这个页面 / 组件，先不要改代码。逐项列出命中的 slop 特征：位置、现状、为什么显廉价、建议改法，按严重程度排序。重点检查：嵌套圆角是否同心、边框是否统一 0.5px、字号是否超过 4 种或小于 12px、是否有紫色渐变 / 渐变按钮 / 卡片左彩色竖线 / 中点分隔符 / 冗余解释文字 / 下拉箭头未修。
```

## 3. Merged prompt (English)

```
Redesign the screen or components I name using these de-AI rules. If the project has design tokens or a component library, change tokens and reuse components; do not hard-code values or invent new components:

1. Color: keep the UI chrome (buttons, cards, inputs, navigation) in black, white and grays; reserve color for photos and content. Put every other color into a scale-based token system (e.g. Radix Colors) and use each step for its defined purpose. No purple/blue-purple gradients, gradient buttons, rainbow icons, or colored accent bars on card edges.
2. Type: at most 4 font sizes (3 preferred), minimum 12px; create hierarchy with weight, color and spacing instead. No all-caps small headings, eyebrows, or oversized hero type; avoid Instrument Serif, Space Grotesk and Bricolage Grotesque; monospace is for code only.
3. Radius: nested corners must satisfy inner = outer − padding, same-level boxes share one radius, never below 4px, pills and circles stay fully round; keep padding, gap and radius on a 4px grid. Add continuous corners only as progressive enhancement via @supports (corner-shape: superellipse(1.25)), keeping border-radius as the fallback.
4. Borders: hairlines at a uniform 0.5px; remove redundant dividers, stacked shadows, translucent overlays, bordered containers and cards inside cards.
5. Copy: remove "·" separators and redundant explanatory text; no emoji in body copy; write for the actual audience, no slang, no invented words, no fabricated numbers or social proof.
6. Motion: as little as possible; when needed, ease-out at about 250ms; dropdown chevrons must match the icon set and be optically centered.
7. CJK: font stack orders Latin fonts before CJK fonts, uses English font names, quotes names with spaces, and ends with sans-serif.
8. Icons: one icon system for the whole UI; design dark / transparent-mode assets separately instead of filter-converting them.

When done, report: (1) every radius change as "element: old -> new"; (2) which slop items you removed; (3) any remaining hits and why.
```

## 4. 一句话版

源自 @ianneo_ai 的建议（原帖见 `sources.md`）：

```
界面只用黑白灰，颜色留给照片和内容。
```
