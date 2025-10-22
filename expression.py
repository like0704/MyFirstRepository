#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
表达式生成模块
生成四则运算表达式并计算结果
"""

import random
import itertools
from fraction import Fraction


class ExpressionGenerator:
    """表达式生成器"""
    
    def __init__(self, max_value=10):
        self.max_value = max_value
        self.operators = ['+', '-', '×', '÷']
        self.generated_expressions = set()
    
    def generate_expressions(self, count):
        """生成指定数量的表达式"""
        exercises = []
        answers = []
        
        while len(exercises) < count:
            try:
                # 随机选择运算符数量（1-3个）
                operator_count = random.randint(1, 3)
                expression, result = self._generate_single_expression(operator_count)
                
                # 检查是否重复
                normalized_expr = self._normalize_expression(expression)
                if normalized_expr not in self.generated_expressions:
                    self.generated_expressions.add(normalized_expr)
                    exercises.append(expression)
                    answers.append(result.to_string())
                    
            except (ValueError, ZeroDivisionError):
                # 如果生成过程中出现错误（如除数为零），重新生成
                continue
        
        return exercises, answers
    
    def _generate_single_expression(self, operator_count):
        """生成单个表达式"""
        # 生成操作数
        numbers = [Fraction.random_number(self.max_value) 
                  for _ in range(operator_count + 1)]
        
        # 生成运算符
        operators = [random.choice(self.operators) 
                    for _ in range(operator_count)]
        
        # 构建表达式树
        expression_tree = self._build_expression_tree(numbers, operators)
        
        # 计算表达式结果
        result = self._evaluate_expression_tree(expression_tree)
        
        # 转换为字符串表达式
        expression_str = self._tree_to_string(expression_tree)
        
        return expression_str, result
    
    def _build_expression_tree(self, numbers, operators):
        """构建表达式树，考虑运算符优先级"""
        # 简单的表达式树构建，支持括号
        if len(numbers) == 1:
            return numbers[0]
        
        # 随机决定是否加括号
        if len(operators) > 1 and random.random() < 0.5:
            # 随机选择分割点
            split_point = random.randint(1, len(operators) - 1)
            
            left_numbers = numbers[:split_point + 1]
            left_operators = operators[:split_point]
            right_numbers = numbers[split_point + 1:]
            right_operators = operators[split_point + 1:]
            
            left_tree = self._build_expression_tree(left_numbers, left_operators)
            right_tree = self._build_expression_tree(right_numbers, right_operators)
            
            return (operators[split_point], left_tree, right_tree)
        else:
            # 不加括号，从左到右计算
            current_tree = numbers[0]
            
            for i, op in enumerate(operators):
                right_tree = numbers[i + 1]
                current_tree = (op, current_tree, right_tree)
            
            return current_tree
    
    def _evaluate_expression_tree(self, tree):
        """计算表达式树的结果"""
        if isinstance(tree, Fraction):
            return tree
        
        op, left, right = tree
        left_val = self._evaluate_expression_tree(left)
        right_val = self._evaluate_expression_tree(right)
        
        # 检查约束条件
        if op == '-' and left_val < right_val:
            raise ValueError("减法结果不能为负数")
        if op == '÷' and right_val == Fraction(0, 1):
            raise ValueError("除数不能为零")
        if op == '÷' and not (left_val / right_val).is_proper():
            raise ValueError("除法结果必须为真分数")
        
        # 执行运算
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '×':
            return left_val * right_val
        elif op == '÷':
            return left_val / right_val
    
    def _tree_to_string(self, tree):
        """将表达式树转换为字符串"""
        if isinstance(tree, Fraction):
            return tree.to_string()
        
        op, left, right = tree
        left_str = self._tree_to_string(left)
        right_str = self._tree_to_string(right)
        
        # 根据运算符优先级决定是否加括号
        if isinstance(left, tuple) and self._need_parentheses(left, op, 'left'):
            left_str = f"({left_str})"
        if isinstance(right, tuple) and self._need_parentheses(right, op, 'right'):
            right_str = f"({right_str})"
        
        return f"{left_str} {op} {right_str}"
    
    def _need_parentheses(self, child_tree, parent_op, position):
        """判断子表达式是否需要加括号"""
        if not isinstance(child_tree, tuple):
            return False
        
        child_op, _, _ = child_tree
        
        # 运算符优先级
        precedence = {'+': 1, '-': 1, '×': 2, '÷': 2}
        
        child_prec = precedence[child_op]
        parent_prec = precedence[parent_op]
        
        # 左结合性规则
        if position == 'left':
            return child_prec < parent_prec
        else:  # position == 'right'
            if parent_op == '-' and child_op == '+':
                return True
            if parent_op == '÷' and child_op in ['×', '÷']:
                return True
            return child_prec <= parent_prec
    
    def _normalize_expression(self, expression):
        """标准化表达式以检测重复"""
        # 移除所有空格
        expr = expression.replace(' ', '')
        
        # 将运算符转换为标准形式
        expr = expr.replace('×', '*')
        expr = expr.replace('÷', '/')
        
        # 这里可以添加更复杂的标准化逻辑
        # 比如重新排序可交换的运算符
        
        return expr
    
    def _is_commutative(self, op):
        """判断运算符是否可交换"""
        return op in ['+', '×']