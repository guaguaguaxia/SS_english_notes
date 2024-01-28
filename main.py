# coding=utf-8
import os

def add_text_to_files(directory, text):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # 确保只处理txt文件
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r+', encoding='gbk') as file:
                content = file.read()  # 读取原文件内容
                file.seek(0, 0)  # 将文件指针移动到文件开头
                file.write(text + '\n' + content)  # 在开头添加文本并保留原内容

# 使用示例
directory = 'C:\\Users\\guaguaguaxia\\Desktop\\notes\\feel'  # 替换为您的目录路径
text = '请帮我把这些英语学习相关的文本整理成详细的中文笔记，如果笔记出现了相关知识点例句，每个例句都需要整理到笔记里： \n'
add_text_to_files(directory, text)
