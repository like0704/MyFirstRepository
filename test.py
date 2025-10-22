#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试模块
包含各种测试用例
"""

import unittest
from fraction import Fraction
from expression import ExpressionGenerator
from validator import Validator


class TestFraction(unittest.TestCase):
    """分数类测试"""
    
    def test_fraction_creation(self):
        """测试分数创建"""
        f1 = Fraction(3, 5)
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 5)
        
        f2 = Fraction(4, 8)  # 应该自动约分
        self.assertEqual(f2.numerator, 1)
        self.assertEqual(f2.denominator, 2)
    
    def test_from_string(self):
        """测试从字符串创建分数"""
        f1 = Fraction.from_string("3/5")
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 5)
        
        f2 = Fraction.from_string("2'3/8")
        self.assertEqual(f2.numerator, 19)  # 2*8 + 3 = 19
        self.assertEqual(f2.denominator, 8)
        
        f3 = Fraction.from_string("5")
        self.assertEqual(f3.numerator, 5)
        self.assertEqual(f3.denominator, 1)
    
    def test_arithmetic_operations(self):
        """测试算术运算"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        
        # 加法
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)
        
        # 减法
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)
        
        # 乘法
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)
        
        # 除法
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)


class TestExpressionGenerator(unittest.TestCase):
    """表达式生成器测试"""
    
    def setUp(self):
        self.generator = ExpressionGenerator(max_value=10)
    
    def test_generate_expressions(self):
        """测试表达式生成"""
        exercises, answers = self.generator.generate_expressions(5)
        
        self.assertEqual(len(exercises), 5)
        self.assertEqual(len(answers), 5)
        
        # 检查表达式格式
        for exercise in exercises:
            self.assertIn('+', exercise)  # 至少包含一个运算符
    
    def test_expression_constraints(self):
        """测试表达式约束条件"""
        # 生成多个表达式，检查是否满足约束
        for _ in range(100):
            try:
                expr, result = self.generator._generate_single_expression(2)
                # 检查运算符数量不超过3个
                operator_count = sum(1 for char in expr if char in ['+', '-', '×', '÷'])
                self.assertLessEqual(operator_count, 3)
            except (ValueError, ZeroDivisionError):
                # 允许生成过程中出现约束检查失败
                continue


class TestValidator(unittest.TestCase):
    """验证器测试"""
    
    def setUp(self):
        self.validator = Validator()
    
    def test_parse_operand(self):
        """测试操作数解析"""
        # 整数
        result = self.validator._parse_operand("5")
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 1)
        
        # 真分数
        result = self.validator._parse_operand("3/5")
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 5)
        
        # 带分数
        result = self.validator._parse_operand("2'3/8")
        self.assertEqual(result.numerator, 19)
        self.assertEqual(result.denominator, 8)
    
    def test_calculate_expression(self):
        """测试表达式计算"""
        # 简单加法
        result = self.validator._calculate_expression("1/2 + 1/3")
        self.assertEqual(result.to_string(), "5/6")
        
        # 带括号的表达式
        result = self.validator._calculate_expression("(1 + 2) × 3")
        self.assertEqual(result.to_string(), "9")


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    suite = unittest.TestSuite()
    
    # 添加测试类
    suite.addTest(unittest.makeSuite(TestFraction))
    suite.addTest(unittest.makeSuite(TestExpressionGenerator))
    suite.addTest(unittest.makeSuite(TestValidator))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    # 运行测试
    success = run_tests()
    
    if success:
        print("\n✅ 所有测试通过！")
    else:
        print("\n❌ 部分测试失败！")
    
    # 演示程序功能
    print("\n=== 功能演示 ===")
    
    # 生成10道题目
    generator = ExpressionGenerator(max_value=10)
    exercises, answers = generator.generate_expressions(5)
    
    print("生成的题目：")
    for i, (exercise, answer) in enumerate(zip(exercises, answers), 1):
        print(f"{i}. {exercise} = {answer}")
    
    # 演示分数运算
    print("\n分数运算演示：")
    f1 = Fraction(1, 6)
    f2 = Fraction(1, 8)
    result = f1 + f2
    print(f"{f1.to_string()} + {f2.to_string()} = {result.to_string()}")