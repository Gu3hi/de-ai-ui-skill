# de-ai-ui · UI 设计去 AI 味 Skill

> 让 vibe coding 出来的界面不再「一眼 AI、一眼廉价」。

一个给 **Claude Code / Cursor / Codex / Muse** 等 Agent 使用的 Skill（`SKILL.md` 格式）。它把 @bruc3van 汇总推荐的 8 位中文设计师在 X 上公开分享的「AI 界面哪里露馅、该怎么跟 AI 说」，转述整理成**可执行、可检查**的规则、自查清单、工作流、可直接复制的 Prompt，外加一个可机械检测的自查脚本。

起点帖：[@bruc3van 的汇总帖](https://x.com/bruc3van/status/2115963644811116732)（2026-10-30）——vibe 界面显廉价往往输在细节，比如嵌套圆角应满足内圆角 = 外圆角 − 间距。

**English summary:** A drop-in agent skill that helps AI coding agents avoid the "AI-generated / cheap" look in UI work. It distills public posts by eight Chinese-speaking designers (curated by @bruc3van) into checkable rules — nested radius `r = R − p`, superellipse corners as progressive enhancement, uniform 0.5px hairlines, ≤4 font sizes with a 12px floor, grayscale chrome with color reserved for content, scale-based color tokens, CJK font stacks — plus a slop self-audit checklist, a before/while/after workflow, copy-paste prompts written for this repo, and a stdlib-only audit script for the machine-checkable subset. All rules are paraphrases with sources cited, not reproductions of the original posts.

## 包含什么

- **核心原则**：先减后加、界面退后内容出彩、一致性靠系统、细节几何正确、先定义再动手、不同模式单独设计。
- **硬规则（可打勾）**：圆角与边框、颜色、字体与中文排版、文案、动效与交互、图标与多模式素材。
- **AI slop 自查清单**：@dingyi 的 19 条典型特征（转述）+ 其他来源补充，交付前逐项过。
- **工作流**：动手前 → 编码中 → 交付前自查；每轮只改一处。
- **Prompt**：本仓依据规则自撰的合并版（中 / 英）、只审查版、一句话版；各原帖的长 Prompt 附链接出处，不转载。
- **示例与脚本**：`tokens.css` 最小 token 集、`before-after.css` 前后对照、`scripts/audit.py` 机器初筛（查紫色渐变、slop 字体、字号档数 / 下限、中点分隔符、卡片左彩线等）。

## 目录

```
skills/de-ai-ui/
├── SKILL.md                      # 入口：触发条件、原则、硬规则速览、工作流
├── references/
│   ├── sources.md                # 主帖 + 15 条来源帖链接与要点摘要
│   ├── slop-checklist.md         # AI slop 自查清单
│   ├── radius-and-borders.md     # r = R − p、超椭圆、0.5px 与回退
│   ├── color.md                  # 黑白灰 chrome + 成套色阶
│   ├── typography-cjk.md         # 字号层级、slop 字体、中文 font-family
│   ├── copy-and-content.md       # 文案规则
│   ├── motion-and-interaction.md # 动效基线、级联菜单、拖拽、按钮手感
│   ├── icons-and-modes.md        # 图标一致性、多模式素材
│   ├── workflow-and-resources.md # 8 条原则、10 个资源、5 个同类 Skill 选用
│   └── prompts.md                # 可复制 Prompt（本仓自撰）
├── examples/
│   ├── tokens.css
│   └── before-after.css
└── scripts/
    └── audit.py                  # 机器可检项初筛（Python stdlib）
```

## 安装

先克隆：

```bash
git clone https://github.com/Gu3hi/de-ai-ui-skill.git
```

**Claude Code**

```bash
mkdir -p ~/.claude/skills && cp -r de-ai-ui-skill/skills/de-ai-ui ~/.claude/skills/
# 或仅当前项目：mkdir -p .claude/skills && cp -r de-ai-ui-skill/skills/de-ai-ui .claude/skills/
```

**Cursor**

```bash
mkdir -p ~/.cursor/skills && cp -r de-ai-ui-skill/skills/de-ai-ui ~/.cursor/skills/
```

Cursor 也会读取 `.agents/skills/`、`~/.agents/skills/` 以及 Claude / Codex 的 skills 目录。在 Agent 对话里输入 `/de-ai-ui` 可手动调用。

**Codex**

```bash
mkdir -p ~/.agents/skills && cp -r de-ai-ui-skill/skills/de-ai-ui ~/.agents/skills/
```

旧版 Codex 使用 `~/.codex/skills/`。在 Codex 里可用 `/skills` 或 `$de-ai-ui` 调用。

**其他 Agent**：没有 Skill 机制的工具，可以直接把 `SKILL.md` 内容贴进项目规则（如 `AGENTS.md`、`.cursor/rules`、`CLAUDE.md`），或按需引用 `references/` 里的文件。

## 怎么用

装好后正常提需求即可，Agent 在做 UI / 落地页 / 组件，或你说「有 AI 味、太廉价」时会自动加载。也可以明确说：

- 「用 de-ai-ui 审查这个页面，先列出命中的 slop 项，不要改代码。」
- 「按 de-ai-ui 的规则重做设置页，每轮只改一处。」
- 「把这个项目的圆角按 r = R − p 统一，并列出 element: old -> new。」

机器初筛（可选）：

```bash
python3 skills/de-ai-ui/scripts/audit.py path/to/project
python3 skills/de-ai-ui/scripts/audit.py path/to/project --strict   # 有命中时退出码 1
```

## 致谢 / Credits

所有规则转述自以下设计师的公开帖子，逐条链接与摘要见 [`references/sources.md`](skills/de-ai-ui/references/sources.md)：

| 作者 | 主题 |
|---|---|
| [@bruc3van](https://x.com/bruc3van) Bruce Van | 汇总推荐这 8 位设计师 |
| [@Kubai087](https://x.com/Kubai087) 枯白啃设计 | 递进式圆角 / 超椭圆、拟物按钮、级联菜单、拖拽排序、图标改造 |
| [@ZaynHao](https://x.com/ZaynHao) | 10 条界面优化提示词、Radix 色阶系统 |
| [@ianneo_ai](https://x.com/ianneo_ai) 伊恩 | 只用黑白灰，把颜色留给内容 |
| [@dingyi](https://x.com/dingyi) | AI slop 典型特征清单 |
| [@Xian0063](https://x.com/Xian0063) 弦 | 8 条审美原则 + 5 个 AI 设计 Skill 评介 |
| [@yanliudreamer](https://x.com/yanliudreamer) 妍妍 | 10 个 UI 组件 / 工具资源、做减法与多方案对比 |
| [@ricouii](https://x.com/ricouii) | 中文网站 font-family 写法 |
| [@remixdesigner](https://x.com/remixdesigner) | Preview 图标 Clear 模式单独图层 |

另感谢同源整理仓 [Florious95/de-ai-ui-skill](https://github.com/Florious95/de-ai-ui-skill)，本仓整理时用它交叉核对过帖目与要点。

本仓库是个人整理，与上述作者无隶属关系；内容为转述与归纳，如与原帖有出入以原帖为准。欢迎提 Issue / PR 补充或更正。

## License

本仓库自有的文字与代码以 [MIT](LICENSE) 发布。规则内容是对上述公开帖子的转述与整理，原帖文字、图片与 Prompt 的权利归原作者所有，请通过 `sources.md` 的链接阅读原文。
