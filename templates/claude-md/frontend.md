<!--
  来源：《驾驭AI编程》第3章（约束）、第5章（验证）综合
  用法：复制到前端项目根目录，重命名为 CLAUDE.md
  更新：根据项目需求修改，删除不适用的部分
-->

# [项目名称] — Frontend

## Project Overview

[React 18 / Vue 3 / Next.js 14 / ...] + [TypeScript 5.x] + [状态管理] + [UI 库]

```
Pages/Routes → Components → Hooks/Composables → API Layer → Backend
                                                    ↓
                                              State Store
```

## Build & Test Commands

```bash
# Install dependencies
npm install        # 或 pnpm install / yarn

# Dev server
npm run dev

# Run tests
npm run test       # 单元测试
npm run test:e2e   # E2E 测试 (Playwright / Cypress)

# Lint & format
npm run lint
npm run format

# Type check
npm run typecheck  # 或 tsc --noEmit

# Build
npm run build
```

## Framework Constraints

<!-- 版本锁定 + 原因（第 3 章：给理由，AI 遇到边界场景时能自己判断） -->

- [框架] version: [版本号]（锁定此版本，[原因]）
- Node.js: >= [版本]
- TypeScript: strict mode enabled，不使用 `any` 类型
- 包管理器: [npm / pnpm / yarn]，**不要混用**

## Architecture Rules

### Directory Structure

```
src/
├── pages/          → 页面/路由组件（一个文件 = 一个路由）
├── components/
│   ├── ui/         → 通用 UI 组件（Button, Modal, Input...）
│   └── feature/    → 业务组件（OrderCard, UserProfile...）
├── hooks/          → 自定义 hooks（useAuth, useOrder...）
├── stores/         → 状态管理（Zustand / Pinia / Redux）
├── api/            → API 请求层（统一封装，不在组件里直接 fetch）
├── types/          → TypeScript 类型定义
├── utils/          → 纯函数工具
├── styles/         → 全局样式 / 主题变量
└── constants/      → 常量定义
```

### Component Patterns

- **组件不超过 200 行**。超过就拆分
- **一个组件一个文件**，文件名 = 组件名（PascalCase）
- **Props 必须定义 TypeScript interface**，不使用 `any`
- **业务逻辑抽到 hooks / composables**，组件只负责渲染
- **不在组件中直接调用 API**，通过 hooks 或 store 中转

```tsx
// 正确：逻辑在 hook 中
function OrderList() {
  const { orders, isLoading, error } = useOrders();
  if (isLoading) return <Skeleton />;
  return <OrderTable data={orders} />;
}

// 错误：逻辑和渲染混在一起
function OrderList() {
  const [orders, setOrders] = useState([]);
  useEffect(() => { fetch('/api/orders').then(...) }, []);
  // ... 50 行数据处理逻辑 ...
  return <table>...</table>;
}
```

### State Management

- **局部状态**（仅当前组件用）：`useState` / `ref`
- **共享状态**（多组件共用）：[Zustand / Pinia / Redux Toolkit]
- **服务端状态**（API 数据缓存）：[React Query / SWR / TanStack Query]
- **不要把所有东西都放全局 store**。只放跨页面共享的数据（用户信息、主题、权限）
- **不要在 store 里调 API**，API 调用走 query 层，store 只存 UI 状态

## Code Conventions

### Naming

- Components: PascalCase (`OrderCard.tsx`)
- Hooks: camelCase with `use` prefix (`useOrder.ts`)
- Utils/helpers: camelCase (`formatPrice.ts`)
- Constants: UPPER_SNAKE_CASE (`MAX_RETRY_COUNT`)
- CSS classes: [BEM / Tailwind / CSS Modules] — **不混用多种方案**
- Event handlers: `handleXxx` (`handleSubmit`, `handleClick`)

### CSS / Styling

- 方案: [Tailwind CSS / CSS Modules / styled-components / ...]
- **不使用内联 style 对象**（除非动态计算值）
- **不使用 `!important`**
- 响应式断点: [sm: 640px / md: 768px / lg: 1024px / xl: 1280px]
- 主题变量定义在 [位置]，组件通过变量引用，不硬编码颜色值

### TypeScript

- **strict mode**，不允许 `any`
- API 响应类型定义在 `types/api.ts`
- 组件 Props 用 `interface`，工具函数参数用 `type`
- 枚举优先用 `as const` 对象，避免 `enum`

## Testing Requirements

### Unit Tests

- 工具函数 (`utils/`): **100% 覆盖**
- Hooks: **核心逻辑必须测试**
- 组件: 测试用户交互和关键渲染逻辑，不测样式
- 测试框架: [Vitest / Jest] + [React Testing Library / Vue Test Utils]

### E2E Tests

- 关键用户流程必须有 E2E 覆盖: 登录、核心业务操作、支付
- 框架: [Playwright / Cypress]
- 测试数据: 使用 mock 或测试环境，**不连接生产 API**

## Verification Rules

- 禁止删除或修改已有测试用例，除非需求本身变更了测试预期
- 测试失败时，修代码，不许改测试
- 新增页面/组件必须附带基本测试
- 代码必须通过 `npm run typecheck` 和 `npm run lint`
- **不得引入 `node_modules` 中不存在的包**（先 `npm install`）
- 不得声称"已完成"而未提供浏览器运行验证

## Forbidden Patterns

- `any` 类型
- `console.log` 在提交代码中（使用项目 logger）
- `// @ts-ignore` / `// @ts-expect-error`（修复类型问题而不是绕过）
- `innerHTML` 赋值（XSS 风险）
- `eval()` / `new Function()`
- 直接操作 DOM（`document.getElementById` 等），用框架的方式
- 在组件中硬编码 API URL / 配置值
- `var` 声明（使用 `const` / `let`）

## Accessibility

- 交互元素必须可键盘操作
- 图片必须有 `alt` 属性
- 表单输入必须有关联的 `label`
- 颜色对比度满足 WCAG AA 标准

## Module Permissions

| Path | Permission | Reason |
|------|-----------|--------|
| `src/components/` | AI 可读写 | 组件开发 |
| `src/pages/` | AI 可读写 | 页面开发 |
| `src/api/` | AI 可读写（需审查） | API 层改动影响全局 |
| `public/` | **只读** | 静态资源手动管理 |
| `.env*` | **禁止访问** | 环境变量含敏感信息 |
| `package.json` | **需确认** | 依赖变更需人工审查 |

Last reviewed: [日期]
