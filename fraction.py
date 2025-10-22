#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分数运算模块
支持真分数的加减乘除运算
"""

import math
import random


class Fraction:
    """真分数类"""
    
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为零")
        
        # 确保分母为正数
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
            
        # 约分
        gcd_val = math.gcd(abs(numerator), denominator)
        self.numerator = numerator // gcd_val
        self.denominator = denominator // gcd_val
    
    @classmethod
    def from_string(cls, s):
        """从字符串创建分数，支持格式：3/5, 2'3/8"""
        if "'" in s:
            # 带分数格式
            parts = s.split("'")
            whole = int(parts[0])
            frac_parts = parts[1].split('/')
            numerator = int(frac_parts[0])
            denominator = int(frac_parts[1])
            return cls(whole * denominator + numerator, denominator)
        elif '/' in s:
            # 真分数格式
            parts = s.split('/')
            numerator = int(parts[0])
            denominator = int(parts[1])
            return cls(numerator, denominator)
        else:
            # 整数格式
            return cls(int(s), 1)
    
    def to_string(self):
        """转换为字符串表示"""
        if self.denominator == 1:
            return str(self.numerator)
        elif abs(self.numerator) < self.denominator:
            return f"{self.numerator}/{self.denominator}"
        else:
            whole = self.numerator // self.denominator
            numerator = abs(self.numerator) % self.denominator
            if numerator == 0:
                return str(whole)
            else:
                return f"{whole}'{numerator}/{self.denominator}"
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = (self.numerator * other.denominator + 
                    other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = (self.numerator * other.denominator - 
                    other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if other.numerator == 0:
            raise ValueError("除数不能为零")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.numerator * other.denominator == 
                other.numerator * self.denominator)
    
    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.numerator * other.denominator < 
                other.numerator * self.denominator)
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other
    
    def is_proper(self):
        """判断是否为真分数"""
        return abs(self.numerator) < self.denominator
    
    @staticmethod
    def random_fraction(max_value):
        """生成随机真分数"""
        denominator = random.randint(2, max_value)
        numerator = random.randint(1, denominator - 1)
        return Fraction(numerator, denominator)
    
    @staticmethod
    def random_number(max_value):
        """生成随机数（整数或真分数）"""
        if random.random() < 0.3:  # 30%概率生成分数
            return Fraction.random_fraction(max_value)
        else:
            return Fraction(random.randint(0, max_value - 1), 1)