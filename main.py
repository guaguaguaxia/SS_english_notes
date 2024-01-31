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





def convert_md_encoding_to_utf8(directory_path):
    """
    将指定目录下所有md文件从GBK编码转换为UTF-8编码。

    :param directory_path: 要转换文件的目录路径
    """
    # 遍历目录中的所有文件
    for filename in os.listdir(directory_path):
        # 检查文件是否为md文件
        if filename.endswith('.md'):
            file_path = os.path.join(directory_path, filename)

            # 尝试以GBK编码读取文件内容
            try:
                with open(file_path, 'r', encoding='gbk') as file:
                    content = file.read()

                # 将内容以UTF-8编码写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f'文件 {filename} 已转换为UTF-8编码。')

            except UnicodeDecodeError:
                print(f'文件 {filename} 读取失败，可能不是GBK编码。')

def rename_txt_to_md(folder_path):
    """
    Rename all .txt files in the given folder to .md files.

    :param folder_path: Path to the folder where the files are located.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            base = os.path.splitext(filename)[0]
            new_name = base + ".md"
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} to {new_name}")

# 使用示例
# convert_md_encoding_to_utf8('path/to/your/directory')

if __name__ == '__main__':
    # convert_md_encoding_to_utf8("C:\\Users\\guaguaguaxia\\Desktop\\notes\\feel")
    # 使用示例
    directory = 'C:\\Users\\guaguaguaxia\\Desktop\\notes\\feel'  # 替换为您的目录路径
    text = '请帮我把这些英语学习相关的文本整理成详细的中文笔记，如果笔记出现了相关知识点例句，每个例句都需要整理到笔记里： \n'
    # add_text_to_files(directory, text)

    convert_md_encoding_to_utf8("D:\\PythonProject\\SS_english_notes\\notes\\New Concept English")