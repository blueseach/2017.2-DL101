# -*- coding: utf-8 -*-  
# Exercise 11: Asking Questions

print "How old are you?"
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#  raw_input() 从标准输入（sys.stdin）读取一个输入并返回一个字符串，且尾部的换行符从末尾移除

# print后的逗号让光标保留在当前行，否则会跳到下一行
