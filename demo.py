#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示脚本
展示四则运算题目生成器的功能
"""

import os
import sys
from fraction import Fraction
from expression import ExpressionGenerator
from validator import Validator


def demo_basic_operations():
    """演示基础运算功能"""
    print("=== 基础运算演示 ===")
    
    # 分数运算演示
    print("\n1. 分数运算：")
    f1 = Fraction(1, 6)
    f2 = Fraction(1, 8)
    result = f1 + f2
    print(f"   {f1.to_string()} + {f2.to_string()} = {result.to_string()}")
    
    # 带分数运算
    f3 = Fraction.from_string("2'1/4")
    f4 = Fraction.from_string("1'1/2")
    result = f3 + f4
    print(f"   {f3.to_string()} + {f4.to_string()} = {result.to_string()}")
    
    # 除法运算（结果为真分数）
    f5 = Fraction(1, 2)
    f6 = Fraction(2, 1)
    result = f5 / f6
    print(f"   {f5.to_string()} ÷ {f6.to_string()} = {result.to_string()}")


def demo_expression_generation():
    """演示表达式生成"""
    print("\n=== 表达式生成演示 ===")
    
    generator = ExpressionGenerator(max_value=10)
    
    # 生成5道题目
    print("\n生成5道题目：")
    exercises, answers = generator.generate_expressions(5)
    
    for i, (exercise, answer) in enumerate(zip(exercises, answers), 1):
        print(f"{i}. {exercise} = {answer}")
    
    # 展示题目多样性
    print("\n题目类型统计：")
    operator_counts = {}
    for exercise in exercises:
        for op in ['+', '-', '×', '÷']:
            count = exercise.count(op)
            if count > 0:
                operator_counts[op] = operator_counts.get(op, 0) + count
    
    for op, count in operator_counts.items():
        print(f"  {op} 运算符出现次数: {count}")


def demo_validation():
    """演示答案验证功能"""
    print("\n=== 答案验证演示 ===")
    
    # 创建测试题目和答案
    test_exercises = [
        "3 + 5",
        "1/2 + 1/3", 
        "2'1/4 × 3",
        "(3 + 4) × 2",
        "7 ÷ 2"
    ]
    
    correct_answers = [
        "8",
        "5/6",
        "6'3/4", 
        "14",
        "3'1/2"
    ]
    
    wrong_answers = [
        "7",  # 错误答案
        "5/6", # 正确答案
        "7",  # 错误答案
        "15", # 错误答案
        "3'1/2" # 正确答案
    ]
    
    # 创建测试文件
    with open('test_exercises.txt', 'w', encoding='utf-8') as f:
        for i, exercise in enumerate(test_exercises, 1):
            f.write(f"{i}. {exercise} = \n")
    
    with open('correct_answers.txt', 'w', encoding='utf-8') as f:
        for i, answer in enumerate(correct_answers, 1):
            f.write(f"{i}. {answer}\n")
    
    with open('wrong_answers.txt', 'w', encoding='utf-8') as f:
        for i, answer in enumerate(wrong_answers, 1):
            f.write(f"{i}. {answer}\n")
    
    # 验证正确答案
    validator = Validator()
    validator.validate('test_exercises.txt', 'correct_answers.txt')
    
    with open('Grade.txt', 'r', encoding='utf-8') as f:
        correct_result = f.read()
    
    print("\n验证正确答案结果：")
    print(correct_result)
    
    # 验证错误答案
    validator.validate('test_exercises.txt', 'wrong_answers.txt')
    
    with open('Grade.txt', 'r', encoding='utf-8') as f:
        wrong_result = f.read()
    
    print("验证错误答案结果：")
    print(wrong_result)
    
    # 清理测试文件
    os.remove('test_exercises.txt')
    os.remove('correct_answers.txt')
    os.remove('wrong_answers.txt')
    os.remove('Grade.txt')


def demo_performance():
    """演示性能测试"""
    print("\n=== 性能测试演示 ===")
    
    import time
    
    # 测试生成100道题目的性能
    print("\n测试生成100道题目的性能：")
    generator = ExpressionGenerator(max_value=20)
    
    start_time = time.time()
    exercises, answers = generator.generate_expressions(100)
    end_time = time.time()
    
    print(f"生成时间: {end_time - start_time:.2f} 秒")
    print(f"题目数量: {len(exercises)}")
    print(f"平均每道题目时间: {(end_time - start_time) / len(exercises) * 1000:.2f} 毫秒")
    
    # 展示前5道题目
    print("\n前5道题目示例：")
    for i, (exercise, answer) in enumerate(zip(exercises[:5], answers[:5]), 1):
        print(f"{i}. {exercise} = {answer}")


def main():
    """主演示函数"""
    print("小学四则运算题目生成器 - 功能演示")
    print("=" * 50)
    
    try:
        # 演示基础运算
        demo_basic_operations()
        
        # 演示表达式生成
        demo_expression_generation()
        
        # 演示答案验证
        demo_validation()
        
        # 演示性能测试
        demo_performance()
        
        print("\n" + "=" * 50)
        print("✅ 演示完成！")
        print("\n使用说明：")
        print("1. 生成题目: python arithmetic_generator.py -n 10 -r 10")
        print("2. 验证答案: python arithmetic_generator.py -e Exercises.txt -a Answers.txt")
        print("3. 运行测试: python test.py")
        
    except Exception as e:
        print(f"\n❌ 演示过程中出现错误: {e}")
        print("请检查代码是否正确。")


if __name__ == "__main__":
    main()