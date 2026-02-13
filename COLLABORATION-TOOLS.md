# 协作工具指南 — funghi88.github.io

基于当前项目框架整理的协作工具说明。用于提升 AI + 设计师协作效率，缩短开发周期。

---

## 一、各工具在本项目中的作用

### 1. ASCII Wireframe（线框图）

**作用：** 用纯文本描述页面布局，无需 Figma/Sketch。AI 可直接理解并实现。

**本项目中的体现：**
- 首页：header、hero、post-list 卡片布局
- 文章页：post-header、content-paper、post-footer 结构

**适用场景：** 新增页面、改版布局、讨论「放哪里」「怎么排」时。

---

### 2. Swimlane Diagram（泳道图）

**作用：** 展示不同角色/系统在同一流程中的职责与顺序。

**本项目中的体现：**
- 内容发布流：Author → Jekyll → Reader
- 未来 Web3：User / Frontend / Wallet 三泳道

**适用场景：** 多角色协作流程、前后端分工、第三方集成（如 Giscus、钱包）时。

---

### 3. State Machine（状态机）

**作用：** 描述「状态 + 触发条件 + 转换」，避免遗漏边界情况。

**本项目中的体现：**
- 搜索 overlay：`[隐藏] ←→ [显示]`
- 未来：钱包连接 `[Disconnected] → [Connecting] → [Connected]`

**适用场景：** 有明确状态切换的 UI（弹窗、加载、连接状态）或后端状态流转。

---

### 4. Sequence Diagram（时序图）

**作用：** 精确描述「谁 → 谁 → 做什么」的调用顺序。

**本项目中的体现：**
- 页面加载：User → Browser → GitHub → 返回 HTML
- 未来 Web3：User → Frontend → Wallet → Chain 的签名流程

**适用场景：** API 调用、前后端交互、第三方服务对接时。

---

### 5. Design Token Table（设计令牌表）

**作用：** 统一颜色、间距、圆角、字体等设计变量，保证视觉一致性。

**本项目中的体现：**
- 已在 `DESIGN-SPEC.md` 中定义：`bg`、`text`、`heading`、`muted`、`link`、`accent-aqua`、`accent-pink`、`accent-rose`
- `override.css` 中实际使用这些值

**适用场景：** 任何颜色/间距/字体改动。新增 token 必须更新表格。

---

### 6. Component Tree Map（组件树）

**作用：** 描述页面结构的层级关系，便于拆组件、找复用点。

**本项目中的体现：**
```
site
├── header (site-brand, site-nav)
├── main
│   ├── home (hero-banner, post-cards)
│   └── post (post-header, post-content, post-footer)
└── footer
```

**适用场景：** 新增模块、重构布局、讨论「这个区块属于哪一层」时。

---

### 7. Constraint Checklist（约束清单）

**作用：** 在动手前做「设计守则」检查，防止偏离规范。

**本项目中的体现：**
- 浅色背景 #EFF7F5
- 仅用 spec 中的 5 色
- 8px 栅格、4px/8px 圆角
- 无必要不加 JS

**适用场景：** 每次视觉/布局改动前过一遍，确保不破坏设计系统。

---

## 二、本项目适配度评估

| 工具 | 适配度 | 说明 |
|------|--------|------|
| **Design Token Table** | ⭐⭐⭐⭐⭐ | 已深度使用，设计师与 AI 共同维护，是视觉一致性的核心 |
| **Component Tree Map** | ⭐⭐⭐⭐⭐ | 结构清晰，Jekyll 的 layout/include 与树一一对应 |
| **Constraint Checklist** | ⭐⭐⭐⭐⭐ | 项目有明确设计规范，清单可直接落地 |
| **ASCII Wireframe** | ⭐⭐⭐⭐ | 布局简单，ASCII 足够表达，无需复杂工具 |
| **Swimlane** | ⭐⭐⭐ | 当前流程简单，未来 Web3/多角色时价值更高 |
| **Sequence Diagram** | ⭐⭐⭐ | 静态站交互少，后端打通后更关键 |
| **State Machine** | ⭐⭐ | 目前仅搜索 overlay 有状态，复杂度低 |

---

## 三、今后其他项目的工具选择建议

| 项目类型 | 优先使用 | 次选 |
|----------|----------|------|
| **内容站 / 博客** | Token Table, Component Tree, Constraint Checklist, ASCII | Swimlane（发布流程） |
| **产品型 Web App** | Token Table, Component Tree, State Machine, Sequence | Swimlane, ASCII |
| **Web3 / 钱包集成** | Swimlane, Sequence, State Machine | Token Table, Constraint |
| **设计系统 / 组件库** | Token Table, Component Tree, Constraint Checklist | ASCII（组件布局） |
| **后台 / 管理端** | Swimlane, Sequence, State Machine | Component Tree, Constraint |

---

## 四、设计师背景 — 建议重点使用的工具

你更关注前端设计与视觉一致性，以下工具建议**优先、高频**使用：

### 核心三件套（每次改版必用）

1. **Design Token Table** — 任何颜色、间距、字体改动都先更新表，再写代码。避免「随手改一个值」导致风格漂移。
2. **Component Tree Map** — 新增区块前先画进树里，确认层级和复用关系。减少「这个放哪」的反复沟通。
3. **Constraint Checklist** — 提交前过一遍，保证不破坏既有规范。

### 布局沟通

4. **ASCII Wireframe** — 讨论新页面/新模块时，用 ASCII 快速画出布局，比口头描述更准确，AI 也能直接实现。

### 建议补充

5. **Typography Scale Table** — 若对字体层级要求高，可单独建表：`h1/h2/h3/body/meta` 的 `font-size`、`line-height`、`weight`。
6. **Spacing Scale** — 若希望间距更系统化，可扩展 Token Table 或单独列出：`space-4/8/16/24/32` 等。

---

## 五、后端 / 功能打通 — 核心工具

当项目涉及 API、数据库、第三方服务时，以下工具更关键：

### 核心三件套

1. **Sequence Diagram** — 描述「前端 → API → 数据库」的调用顺序，是打通功能的基础。每次新增接口建议先画时序。
2. **Swimlane Diagram** — 区分 User / Frontend / Backend / 第三方，避免职责混乱。
3. **State Machine** — 表单提交、加载态、错误态、重试逻辑，都适合用状态机表达。

### 补充

4. **API Contract Table** — 简单表格：`端点 | 方法 | 入参 | 出参`，与 Sequence 配合使用。
5. **Error State Map** — 列出「网络失败 / 超时 / 权限不足」等状态及对应 UI，避免遗漏。

---

## 六、建议补充的工具

| 工具 | 用途 | 何时用 |
|------|------|--------|
| **Typography Scale** | 字体层级表 | 对排版要求高时 |
| **Spacing Scale** | 间距系统表 | 希望 8px 栅格更严格时 |
| **API Contract Table** | 接口约定 | 有后端/第三方 API 时 |
| **Error State Map** | 错误态清单 | 表单、支付、连接等有失败路径时 |
| **Breakpoint Map** | 响应式断点 | 多端适配时 |

---

## 七、快速索引 — 按需求找工具

| 需求 | 工具 |
|------|------|
| 改颜色 / 间距 / 字体 | Design Token Table |
| 新增页面 / 改布局 | ASCII Wireframe, Component Tree |
| 改版前检查规范 | Constraint Checklist |
| 多角色流程（发布、登录、支付） | Swimlane Diagram |
| 弹窗、加载、连接状态 | State Machine |
| API 调用、前后端交互 | Sequence Diagram |
| 后端功能打通 | Sequence + Swimlane + State Machine |

---

## 八、与现有文档的关系

| 文档 | 内容 |
|------|------|
| `DESIGN-SPEC.md` | Token Table、Component Tree、Constraint 的精简版，日常参考 |
| `DESIGN-FRAMEWORK.md` | 完整协作框架，含 ASCII、Swimlane、State、Sequence 等 |
| `COLLABORATION-TOOLS.md`（本文档） | 工具说明、适配度、选型建议、设计师/后端侧重 |

建议：日常改版看 `DESIGN-SPEC.md`；新功能/新项目规划时参考 `DESIGN-FRAMEWORK.md` 和本文档。

---

*保持简洁，按需使用。工具是为了对齐认知，不是为了增加流程。*
