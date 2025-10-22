# 使用说明

## 快速开始

### 1. 安装依赖
本项目使用纯Python实现，无需额外安装依赖包。

### 2. 生成题目
```bash
python arithmetic_generator.py -n 10 -r 10
```
这将生成10道数值范围在10以内的四则运算题目。

### 3. 验证答案
```bash
python arithmetic_generator.py -e Exercises.txt -a Answers.txt
```
这将验证答案文件中的答案是否正确。

## 详细参数说明

### 生成题目模式
- `-n <数量>`: 指定生成题目的数量（必须）
- `-r <范围>`: 指定数值范围（必须）

**示例**:
```bash
# 生成20道数值范围在5以内的题目
python arithmetic_generator.py -n 20 -r 5

# 生成100道数值范围在100以内的题目
python arithmetic_generator.py -n 100 -r 100
```

### 验证答案模式
- `-e <题目文件>`: 指定题目文件路径（必须）
- `-a <答案文件>`: 指定答案文件路径（必须）

**示例**:
```bash
# 验证指定题目和答案文件
python arithmetic_generator.py -e my_exercises.txt -a my_answers.txt
```

## 文件格式说明

### 题目文件格式 (Exercises.txt)
```
1. 3 + 5 =
2. 1/2 + 1/3 =
3. 2'1/4 × 3 =
4. (3 + 4) × 2 =
5. 7 ÷ 2 =
```

### 答案文件格式 (Answers.txt)
```
1. 8
2. 5/6
3. 6'3/4
4. 14
5. 3'1/2
```

### 成绩统计文件格式 (Grade.txt)
```
Correct: 3 (1, 3, 5)
Wrong: 2 (2, 4)
```

## 功能演示

### 演示脚本
运行演示脚本查看程序功能：
```bash
python demo.py
```

### 手动测试
1. 生成少量题目测试基本功能：
```bash
python arithmetic_generator.py -n 5 -r 10
```

2. 查看生成的文件：
```bash
cat Exercises.txt
cat Answers.txt
```

3. 修改Answers.txt中的一些答案，然后验证：
```bash
python arithmetic_generator.py -e Exercises.txt -a Answers.txt
cat Grade.txt
```

## 注意事项

1. **数值范围参数**：`-r`参数控制自然数、真分数分母的范围
2. **题目数量**：支持生成最多10000道题目
3. **文件编码**：所有文件使用UTF-8编码
4. **错误处理**：程序会检查参数合法性并给出帮助信息
5. **重复检测**：自动检测并避免生成重复题目

## 高级功能

### 自定义数值范围
通过调整`-r`参数可以控制题目的难度：
- 小数值范围（如`-r 5`）：适合低年级学生
- 大数值范围（如`-r 100`）：适合高年级学生

### 批量处理
程序支持批量生成和验证，适合教学使用：
```bash
# 批量生成不同难度的题目
for range_val in 5 10 20 50; do
    python arithmetic_generator.py -n 100 -r $range_val
    mv Exercises.txt exercises_${range_val}.txt
    mv Answers.txt answers_${range_val}.txt
done
```