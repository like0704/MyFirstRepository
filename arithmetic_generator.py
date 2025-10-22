#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小学四则运算题目生成器
支持自然数和真分数运算
"""

import argparse
import sys
from fraction import Fraction
from expression import ExpressionGenerator
from validator import Validator


def main():
    parser = argparse.ArgumentParser(description='小学四则运算题目生成器')
    
    # 互斥参数组：生成题目或验证答案
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', type=int, help='生成题目的数量')
    group.add_argument('-e', type=str, help='题目文件路径')
    
    parser.add_argument('-r', type=int, help='数值范围（自然数、真分数分母的范围）')
    parser.add_argument('-a', type=str, help='答案文件路径')
    
    args = parser.parse_args()
    
    # 生成题目模式
    if args.n is not None:
        if args.r is None:
            print("错误：生成题目时必须使用 -r 参数指定数值范围")
            parser.print_help()
            sys.exit(1)
            
        if args.n <= 0 or args.r <= 0:
            print("错误：参数值必须为正整数")
            sys.exit(1)
            
        generator = ExpressionGenerator(max_value=args.r)
        exercises, answers = generator.generate_expressions(args.n)
        
        # 保存题目和答案
        with open('Exercises.txt', 'w', encoding='utf-8') as f:
            for i, exercise in enumerate(exercises, 1):
                f.write(f"{i}. {exercise} = \n")
        
        with open('Answers.txt', 'w', encoding='utf-8') as f:
            for i, answer in enumerate(answers, 1):
                f.write(f"{i}. {answer}\n")
        
        print(f"成功生成 {args.n} 道题目，已保存到 Exercises.txt 和 Answers.txt")
    
    # 验证答案模式
    elif args.e is not None:
        if args.a is None:
            print("错误：验证答案时必须使用 -a 参数指定答案文件")
            parser.print_help()
            sys.exit(1)
            
        validator = Validator()
        validator.validate(args.e, args.a)
        print("验证完成，结果已保存到 Grade.txt")


if __name__ == "__main__":
    main()