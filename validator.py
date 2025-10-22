#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证和统计模块
验证答案的正确性并生成统计结果
"""

import re
from fraction import Fraction


class Validator:
    """答案验证器"""
    
    def validate(self, exercise_file, answer_file):
        """验证答案文件"""
        # 读取题目文件
        exercises = self._read_exercises(exercise_file)
        
        # 读取答案文件
        answers = self._read_answers(answer_file)
        
        # 验证答案
        correct_indices = []
        wrong_indices = []
        
        for i, (exercise, expected_answer) in enumerate(zip(exercises, answers), 1):
            try:
                # 计算题目正确答案
                correct_result = self._calculate_expression(exercise)
                
                # 解析用户答案
                user_answer = self._parse_answer(expected_answer)
                
                # 比较答案
                if correct_result == user_answer:
                    correct_indices.append(i)
                else:
                    wrong_indices.append(i)
                    
            except (ValueError, ZeroDivisionError) as e:
                # 如果计算过程中出现错误，视为错误答案
                wrong_indices.append(i)
        
        # 生成统计结果
        self._generate_grade_file(correct_indices, wrong_indices)
    
    def _read_exercises(self, filename):
        """读取题目文件"""
        exercises = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # 移除题号
                    match = re.match(r'^\d+\.\s*(.*)\s*=$', line)
                    if match:
                        exercises.append(match.group(1))
        return exercises
    
    def _read_answers(self, filename):
        """读取答案文件"""
        answers = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # 移除题号
                    match = re.match(r'^\d+\.\s*(.*)$', line)
                    if match:
                        answers.append(match.group(1))
        return answers
    
    def _calculate_expression(self, expression):
        """计算表达式结果"""
        # 将表达式转换为可计算的格式
        expr = expression.replace('×', '*')
        expr = expr.replace('÷', '/')
        
        # 使用分数计算
        return self._evaluate_expression(expr)
    
    def _evaluate_expression(self, expr):
        """递归计算表达式"""
        # 移除空格
        expr = expr.replace(' ', '')
        
        # 处理括号
        while '(' in expr:
            start = expr.rfind('(')
            end = expr.find(')', start)
            if end == -1:
                raise ValueError("括号不匹配")
            
            inner_result = self._evaluate_expression(expr[start+1:end])
            expr = expr[:start] + inner_result.to_string() + expr[end+1:]
        
        # 处理乘除
        operators = ['*', '/', '+', '-']
        
        for op in operators:
            if op in expr:
                parts = expr.split(op, 1)
                left = self._parse_operand(parts[0])
                right = self._parse_operand(parts[1])
                
                if op == '*':
                    return left * right
                elif op == '/':
                    if right == Fraction(0, 1):
                        raise ValueError("除数不能为零")
                    return left / right
                elif op == '+':
                    return left + right
                elif op == '-':
                    if left < right:
                        raise ValueError("减法结果不能为负数")
                    return left - right
        
        # 如果没有运算符，直接解析操作数
        return self._parse_operand(expr)
    
    def _parse_operand(self, operand_str):
        """解析操作数（整数或分数）"""
        operand_str = operand_str.strip()
        
        # 检查是否为分数格式
        if "'" in operand_str:
            parts = operand_str.split("'")
            whole = int(parts[0])
            fraction_parts = parts[1].split('/')
            numerator = int(fraction_parts[0])
            denominator = int(fraction_parts[1])
            return Fraction(whole * denominator + numerator, denominator)
        elif '/' in operand_str:
            parts = operand_str.split('/')
            numerator = int(parts[0])
            denominator = int(parts[1])
            return Fraction(numerator, denominator)
        else:
            return Fraction(int(operand_str), 1)
    
    def _parse_answer(self, answer_str):
        """解析用户答案"""
        return self._parse_operand(answer_str)
    
    def _generate_grade_file(self, correct_indices, wrong_indices):
        """生成成绩统计文件"""
        with open('Grade.txt', 'w', encoding='utf-8') as f:
            f.write(f"Correct: {len(correct_indices)} ({', '.join(map(str, correct_indices))})\n")
            f.write(f"Wrong: {len(wrong_indices)} ({', '.join(map(str, wrong_indices))})\n")