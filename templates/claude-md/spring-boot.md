<!--
  来源：《驾驭AI编程》第3章（3.3 软约束 Spring Boot 示例）
  用法：复制到 Java/Spring Boot 项目根目录，重命名为 CLAUDE.md
  更新：根据项目需求修改，删除不适用的部分
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
# Build
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

<!-- 每条来自真实踩坑，给理由让 AI 遇到边界场景时能自己判断（第 3 章） -->

1. 依赖版本锁定 Spring Boot 2.7.x，不要升级到 3.x（3.x 跟我们的中间件不兼容）
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

| Path | Permission | Reason |
|------|-----------|--------|
| `src/main/java/**/payment/` | **只读** | 支付核心，修改需架构师审查 |
| `src/main/java/**/auth/` | **只读** | 认证鉴权，安全敏感 |
| `src/main/java/**/config/` | **只读** | 配置类，手动维护 |
| `src/main/resources/db/migration/` | **禁止创建/修改** | Flyway 迁移必须人工编写 |
| `src/main/java/**/feature/` | AI 可读写 | 业务功能 |

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

- 禁止删除或修改已有测试用例，除非需求本身变更了测试预期
- 测试失败时，修代码，不许改测试
- 新增 Service 方法必须附带单元测试
- 新增 Controller 端点必须附带集成测试
- 代码必须能 `mvn compile` 通过
- 所有已有测试必须通过 `mvn test`

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
