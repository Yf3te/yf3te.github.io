import os
import re

# 设置根目录和 _posts 文件夹路径
root_dir = os.getcwd()  # 当前目录
posts_dir = os.path.join(root_dir, '_posts')

# 遍历 _posts 文件夹中的所有 Markdown 文件
for filename in os.listdir(posts_dir):
    if filename.endswith('.md'):
        file_path = os.path.join(posts_dir, filename)

        # 获取文件名（不包含扩展名）作为新文件夹的名字
        file_name_without_extension = os.path.splitext(filename)[0]
        image_folder = os.path.join(posts_dir, file_name_without_extension)

        # 如果该文件夹不存在，创建文件夹
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        # 读取 .md 文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式匹配图片路径，并替换为新的路径
        updated_content = re.sub(
            r'!\[([^\]]*)\]\(([^)]+)\)',  # 匹配图片格式
            lambda match: f'![{match.group(1)}](./{file_name_without_extension}/{match.group(2).split("/")[-1]})',
            content
        )

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"已修改 {filename} 中的图片路径。")
