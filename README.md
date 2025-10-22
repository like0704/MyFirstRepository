# 小学四则运算题目生成器

## 项目信息
- 作者：阿卜杜哈力克3123004648
- GitHub项目地址：https://github.com/like0704/MyFirstRepository

## 功能描述
这是一个命令行程序，可以自动生成小学四则运算题目，支持自然数和真分数运算，具有以下功能：

1. 生成指定数量的四则运算题目
2. 控制数值范围
3. 避免重复题目
4. 计算结果并验证答案
5. 统计答题正确率

## 使用说明

### 生成题目
```bash
python arithmetic_generator.py -n 10 -r 10
```

### 验证答案
```bash
python arithmetic_generator.py -e Exercises.txt -a Answers.txt
```

## 项目结构
- `arithmetic_generator.py` - 主程序
- `fraction.py` - 分数运算模块
- `expression.py` - 表达式生成和计算模块
- `validator.py` - 验证和统计模块
- `Exercises.txt` - 生成的题目文件
- `Answers.txt` - 题目答案文件

- `Grade.txt` - 答题统计文件
