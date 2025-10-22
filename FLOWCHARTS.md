# 项目流程图

## 1. 主程序流程图

```mermaid
flowchart TD
    A[程序启动] --> B{解析命令行参数}
    B -->|生成题目模式| C[检查参数合法性]
    B -->|验证答案模式| D[检查文件存在性]
    
    C --> E[创建表达式生成器]
    E --> F[生成指定数量题目]
    F --> G[保存题目到Exercises.txt]
    F --> H[保存答案到Answers.txt]
    G --> I[输出成功信息]
    H --> I
    
    D --> J[创建答案验证器]
    J --> K[读取题目文件]
    J --> L[读取答案文件]
    K --> M[验证答案正确性]
    L --> M
    M --> N[生成成绩统计Grade.txt]
    N --> I
```

## 2. 表达式生成流程图

```mermaid
flowchart TD
    A[开始生成表达式] --> B[随机选择运算符数量1-3]
    B --> C[生成操作数列表]
    C --> D[生成运算符列表]
    D --> E[构建表达式树]
    E --> F[计算表达式结果]
    F --> G{检查约束条件}
    G -->|不满足| H[重新生成]
    G -->|满足| I[标准化表达式]
    I --> J{检查重复}
    J -->|重复| H
    J -->|不重复| K[添加到结果列表]
    K --> L{达到指定数量?}
    L -->|否| B
    L -->|是| M[返回题目和答案]
```

## 3. 表达式树构建流程图

```mermaid
flowchart TD
    A[构建表达式树] --> B{操作数数量=1?}
    B -->|是| C[返回单个操作数]
    B -->|否| D{随机添加括号?}
    D -->|是| E[选择分割点]
    E --> F[递归构建左子树]
    E --> G[递归构建右子树]
    F --> H[组合为带括号表达式]
    G --> H
    
    D -->|否| I[从左到右构建]
    I --> J[初始化当前树为第一个操作数]
    J --> K[遍历运算符列表]
    K --> L[组合当前树与下一个操作数]
    L --> M{还有运算符?}
    M -->|是| K
    M -->|否| N[返回完整表达式树]
```

## 4. 答案验证流程图

```mermaid
flowchart TD
    A[开始验证] --> B[读取题目文件]
    A --> C[读取答案文件]
    B --> D[解析题目列表]
    C --> E[解析答案列表]
    D --> F[遍历每道题目]
    E --> F
    
    F --> G[计算题目正确答案]
    G --> H[解析用户答案]
    H --> I{答案正确?}
    I -->|是| J[添加到正确列表]
    I -->|否| K[添加到错误列表]
    J --> L{还有题目?}
    K --> L
    L -->|是| F
    L -->|否| M[生成成绩统计文件]
    M --> N[输出验证结果]
```

## 5. 分数运算流程图

```mermaid
flowchart TD
    A[分数运算] --> B{运算符类型}
    B -->|加法| C[通分计算]
    B -->|减法| D[检查结果非负]
    B -->|乘法| E[分子乘分子，分母乘分母]
    B -->|除法| F[检查除数非零]
    
    C --> G[约分结果]
    D --> H[通分计算]
    H --> G
    E --> G
    F --> I[取倒数相乘]
    I --> G
    
    G --> J[转换为标准格式]
    J --> K[返回结果]
```

## 6. 约束检查流程图

```mermaid
flowchart TD
    A[检查约束条件] --> B{减法运算?}
    B -->|是| C[检查被减数≥减数]
    C -->|否| D[抛出异常: 结果不能为负]
    C -->|是| E{除法运算?}
    
    B -->|否| E
    E -->|是| F[检查除数非零]
    F -->|否| G[抛出异常: 除数不能为零]
    F -->|是| H[检查结果为真分数]
    H -->|否| I[抛出异常: 结果必须为真分数]
    H -->|是| J[约束检查通过]
    
    E -->|否| J
```

## 7. 重复检测流程图

```mermaid
flowchart TD
    A[检测重复题目] --> B[标准化表达式]
    B --> C[移除所有空格]
    C --> D[统一运算符表示]
    D --> E[排序可交换运算符]
    E --> F[生成表达式哈希]
    F --> G{哈希是否存在于集合?}
    G -->|是| H[标记为重复]
    G -->|否| I[添加到已生成集合]
    I --> J[标记为不重复]
```

## 8. 文件处理流程图

```mermaid
flowchart TD
    A[文件处理] --> B{操作类型}
    B -->|生成题目| C[创建Exercises.txt]
    B -->|生成答案| D[创建Answers.txt]
    B -->|验证答案| E[读取题目文件]
    B -->|生成统计| F[创建Grade.txt]
    
    C --> G[格式化题目字符串]
    G --> H[写入文件]
    D --> I[格式化答案字符串]
    I --> H
    E --> J[解析题目编号和内容]
    J --> K[返回题目列表]
    F --> L[格式化统计信息]
    L --> H
```

## 关键函数调用关系图

```mermaid
graph TB
    A[arithmetic_generator.py] --> B[ExpressionGenerator]
    A --> C[Validator]
    
    B --> D[Fraction]
    B --> E[generate_expressions]
    B --> F[_generate_single_expression]
    B --> G[_build_expression_tree]
    B --> H[_evaluate_expression_tree]
    B --> I[_normalize_expression]
    
    C --> J[validate]
    C --> K[_read_exercises]
    C --> L[_read_answers]
    C --> M[_calculate_expression]
    C --> N[_evaluate_expression]
    C --> O[_parse_operand]
    C --> P[_generate_grade_file]
    
    D --> Q[__init__]
    D --> R[from_string]
    D --> S[to_string]
    D --> T[算术运算符重载]
    D --> U[random_fraction]
    D --> V[random_number]
```

## 数据流图

```mermaid
flowchart LR
    A[命令行参数] --> B[主程序]
    B --> C[表达式生成器]
    B --> D[答案验证器]
    
    C --> E[操作数生成]
    C --> F[运算符生成]
    E --> G[表达式树构建]
    F --> G
    G --> H[结果计算]
    H --> I[约束检查]
    I --> J[重复检测]
    J --> K[题目和答案]
    
    D --> L[文件读取]
    L --> M[答案计算]
    L --> N[答案解析]
    M --> O[答案比较]
    N --> O
    O --> P[统计生成]
    
    K --> Q[文件输出]
    P --> R[文件输出]
```

这些流程图展示了项目的核心逻辑和数据处理流程，有助于理解代码的组织结构和执行顺序。