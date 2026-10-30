# 字体与排版（含中文）/ Typography & CJK

主要来源：@ZaynHao / @dingyi（字号与 slop 字体）、@ricouii（中文字体栈）。要点转述，原帖见 `sources.md`。

## 1. 字号层级

- 界面字号**不超过 4 种，最好 3 种**；同一页面更严格时只留 3 种。[@ZaynHao]
- 最小可用字号 **12px**。
- 层级不够时，用**字重、颜色、间距**拉开关系，而不是再加一档字号。

参考档位 `[本 Skill 补充]`：

```css
:root {
  --text-sm: 12px;  /* 辅助信息 */
  --text-md: 14px;  /* 正文与控件 */
  --text-lg: 16px;  /* 小标题（可选第 4 档） */
  --text-xl: 24px;  /* 页面标题；hero 也不要夸张 */
}
```

- hero 区字号大得离谱是 slop 特征。[@dingyi]
- 全大写小标题、标题上方眉标、章节编号、代码式面包屑：不用。[@dingyi]

## 2. 要避开的字体与习惯

- 三款被用烂的字体：**Instrument Serif、Space Grotesk、Bricolage Grotesque**。想靠衬线体出彩，免费默认款基本做不到——原帖作者在回复里直言这类效果通常要付费字体。[@dingyi]
- 滥用等宽字体、到处斜体：不用。等宽只给代码。[@dingyi]
- 不默认全居中排版。[@Xian0063]
- 挑字体的方法：拿同一段文字试 3–5 种，比较字重、字宽、字距与不同字号下的表现（可用 Fontshare 等免费字体库，见 `workflow-and-resources.md`）。[@yanliudreamer]

## 3. 中文 font-family（@ricouii）

原则一句话：**先西后中、兼顾主流操作系统、最后以 `sans-serif` 兜底。**

```css
:root {
  --font-sans:
    /* 西文 */
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Helvetica, Arial,
    /* 中文 */
    "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei",
    "Noto Sans CJK SC", "Noto Sans SC", "Source Han Sans CN",
    sans-serif;
  --font-mono:
    "JetBrains Mono", "SF Mono", ui-monospace, Menlo, Consolas,
    "Liberation Mono", "Courier New", monospace;
}
body { font-family: var(--font-sans); }
code, pre, kbd { font-family: var(--font-mono); }
```

三条避坑：

1. **先西后中**：西文字体写在前面，否则中文字体自带的英文字形会覆盖西文字体，英文与数字显示变差。
2. **写英文名**：如 `"Microsoft YaHei"`，不要写中文名，避免部分系统 / 浏览器识别失败。
3. **带空格加引号**：`"Helvetica Neue"`、`"Microsoft YaHei"` 等必须加双引号。

补充：不声明 `font-family` 时浏览器用的是默认字体，不等于系统字体。原帖代码里等宽变量的一处笔误（少一个 `-`）已按原帖回复区的指正修正为 `var(--font-mono)`。
