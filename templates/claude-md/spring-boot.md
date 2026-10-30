<!--
  来源：《驾驭AI编程》第3章（3.3 软约束 Spring Boot 示例）
  用法：复制到 Java/Spring Boot 项目根目录，重命名为 CLAUDE.md
  更新：根据项目需求修改，删除不适用的部分。
  目录、数据库、异常和API规范均为示例约定，须替换为项目事实；命令须与项目配置一致。
-->

# [项目名称] — Spring Boot Backend

## Project Overview

Java [版本] / Spring Boot [版本] / [数据库] / [其他关键依赖]

```
Client → API Gateway → Controller → Service → Repository → DB
                                              ↓
                                      MessageQueue → Consumer → [外部服务]
```

## Build & Test Commands

```bash
# Package without tests (不能据此宣称测试通过)
mvn clean package -DskipTests

# Run tests
mvn test

# Run specific test class
mvn test -Dtest=OrderServiceTest

# Run application
mvn spring-boot:run

# Lint / format check
mvn spotless:check
```

## Project Constraints

<!-- 填入真实约束及理由，让 AI 理解取舍；不要把示例当作作者项目事实。 -->

1. Spring Boot 使用 [当前版本]；兼容性依据：[实际依赖或迁移约束]，版本变化先评估影响
2. 配置文件统一用 `application.yml`，不要生成 `.properties`
3. 异常只抛自定义 `BusinessException`，禁止裸抛 `RuntimeException`
4. 实体类用 Lombok `@Data`，不要手写 getter/setter
5. MyBatis 查询必须用参数化 `#{}`，禁止字符串拼接 SQL `${}`（防 SQL 注入）
6. REST API 统一返回 `Result<T>` 包装类，不要直接返回实体
7. 日志使用 SLF4J + Logback，日志格式：`[traceId] className.method - message`

## Architecture Rules

### Layer Structure

```
controller/   → 只做参数校验和结果包装，不写业务逻辑
service/      → 业务逻辑，事务在这一层管理
repository/   → 数据访问，只写 SQL/MyBatis 映射
dto/          → 对外传输对象
entity/       → 数据库映射对象
config/       → 配置类
common/       → 公共工具
```

- Controller 不直接调用 Repository，必须经过 Service
- Service 之间不互相调用，共享逻辑提取到 common/
- Entity 不暴露给 Controller 层，用 DTO 转换

### Module Permissions

以下为默认边界；任务明确授权后按范围执行。规则文件不代替账号权限和运行隔离。

| Path | Permission | Reason |
|------|-----------|--------|
| `src/main/java/**/payment/` | **只读** | 支付核心，修改需架构师审查 |
| `src/main/java/**/auth/` | **只读** | 认证鉴权，安全敏感 |
| `src/main/java/**/config/` | **只读** | 配置类，手动维护 |
| `src/main/resources/db/migration/` | **默认只读** | 迁移编写、测试演练和实际执行分别明确授权与验证 |
| `src/main/java/**/feature/` | 任务范围内可读写 | 业务功能 |

## Code Conventions

### Naming

- Package: `com.company.project.module`（小写，单数）
- Class: PascalCase，Service 后缀 `OrderService`，Controller 后缀 `OrderController`
- Method: camelCase，查询用 `getXxx` / `findXxx` / `listXxx`，操作用 `createXxx` / `updateXxx` / `deleteXxx`
- Constants: `UPPER_SNAKE_CASE`
- Database table/column: `lower_snake_case`

### Error Handling

```java
// 正确：抛自定义异常，由全局处理器统一处理
throw new BusinessException(ErrorCode.ORDER_NOT_FOUND, "订单不存在: " + orderId);

// 错误：裸抛运行时异常
throw new RuntimeException("订单不存在");

// 错误：吞掉异常
try { ... } catch (Exception e) { }  // 禁止空 catch
```

### Database

- 新表必须包含 `id`(bigint), `created_at`(datetime), `updated_at`(datetime), `is_deleted`(tinyint) 字段
- 索引命名：`idx_表名_字段名`
- 外键：**不使用数据库外键**，在 Service 层做关联（原因：便于分库分表）
- 时间字段统一用 `LocalDateTime`，时区 UTC+8

### API Design

- RESTful 风格，URL 用复数名词：`/api/v1/orders`
- 分页参数：`page`（从 1 开始）、`size`（默认 20，最大 100）
- 统一响应格式：

```json
{
  "code": 200,
  "message": "success",
  "data": {}
}
```

## Verification Rules

- 测试失败时默认修代码，不得为了变绿而删测试、降低断言或跳过失败
- 确需改测试，先说明需求变化或测试本身的错误，按已有授权或经确认后修改
- 验证 Service 的关键业务行为、边界与事务失败路径
- 根据端点风险覆盖参数、权限和集成行为，避免只复述实现的测试
- 代码必须能 `mvn compile` 通过
- 所有已有测试必须通过 `mvn test`
- 报告实际命令、结果、已有失败及未验证范围；编译通过不代表数据库行为已验证

## Forbidden Patterns

- `System.out.println` — 用 `log.info/warn/error`
- `new Date()` — 用 `LocalDateTime.now()`
- `@Autowired` 字段注入 — 用构造器注入
- 硬编码配置值（URL、端口、密钥）— 放 `application.yml`
- `Thread.sleep()` 在非测试代码中
- `SELECT *` — 明确列出需要的字段
- 直接在 Controller 中写 SQL 或访问数据库

## Security

- 密码存储：BCrypt，不可逆
- API 认证：JWT，有效期 [X] 小时
- 敏感接口必须校验权限注解 `@RequirePermission`
- 用户输入全部做参数校验（`@Valid` + `@NotBlank` / `@Size` 等）
- 日志中禁止打印密码、token、身份证号等敏感信息

Last reviewed: [日期]
