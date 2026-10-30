# 圆角与边框 / Radius & borders

主要来源：@Kubai087（递进式圆角）、@ZaynHao / @dingyi（0.5px 与统一粗细）。要点转述，原帖见 `sources.md`。

## 1. 递进式圆角：r = R − p

嵌套时每一层都满足：

```
内圆角 r = 外圆角 R − 内边距 p
```

内外共用一个圆心，视觉上才是「等距内缩」。

从外往里逐层推：dialog / card → panel、input、button → chip、tag。

示例：

| 外层 | R | p | 内层 r |
|---|---|---|---|
| dialog | 32 | 16 | 16 |
| panel | 16 | 8 | 8（chip） |

配套规则：

- 同一层级的盒子共用同一个圆角值。
- 计算结果最低不低于 4px。
- pill 与圆形保持全圆，不参与递减。
- padding、gap、radius 全部落在 4px 网格上。
- 项目有 radius token 时改 token，不要在组件里硬编码数值。
- 改完输出变更清单：`element: old -> new`。

## 2. 连续圆角 / 超椭圆（渐进增强）

普通圆角在与直边相接处有折痕感；超椭圆过渡更顺，接近 iOS 的连续圆角。写法是「保留普通圆角 + 支持时增强」：

```css
.card {
  border-radius: 32px;
}
@supports (corner-shape: superellipse(1.25)) {
  .card { corner-shape: superellipse(1.25); }
  .pill, .circle { corner-shape: round; }
}
```

支持情况（据原帖，2026-10）：Chrome / Edge 139+ 生效；Safari、Firefox 不支持时自动回退普通圆角，不会坏版。

## 3. 边框：0.5px 与全站统一

- 需要细线 / 边框时优先 0.5px（hairline），这是高清屏上「精致感」的重要来源之一。[@ZaynHao]
- 比数值更重要的是**全站粗细统一**：该用细线的地方用了 1px、或同一页面两种粗细混用，都是 slop 特征。[@dingyi]

回退与边界 `[本 Skill 补充 + 作者自注]`：

- @ZaynHao 自注这条偏个人经验，未专门考虑低分屏 / 老旧设备。
- 在低 DPR 屏幕上 0.5px 可能发虚或被取整；做法：用 `border` + 媒体查询 / DPR 判断做回退，而不是全站无条件写死。
- 原生 App 里对应的是 hairlineWidth / 1/scale，不要写死 0.5pt。

## 4. 圆角与阴影的克制

- 不随意加圆角和阴影；要用时，取值要匹配功能场景（层级越高、离表面越远，阴影才越大）。[@ZaynHao]
- 禁止卡片左边缘彩色竖线。[@ZaynHao][@dingyi]
- 不堆多层阴影、半透明叠色和带边框容器来「制造细节」。[@dingyi]
