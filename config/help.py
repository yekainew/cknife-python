helpTxt="""
                   cknife-python 1.0 帮助界面              \n\n\
参数:      -h  唤出帮助文档\n\
     -u  ['url']  目标链接参数[必须]\n\
     -k  ['key']  目标连接参数值[必须]\n\
     -t  ['type'] 目标类型[必须](php、jsp、asp、asp等，目前仅支持php、jsp)\n\n\
     --shell[必须1/3]  进入模拟shell界面\n\
       模拟shell模式下直接输入cmd命令执行，不支持与内嵌式命令行交互\n\n\
     --db / --database[必须1/3]   进入数据库管理界面\n\
       数据库管理界面按照提示输入数据库相关参数后使用标准数据库命令操作\n\n\
     --file[必须1/3]   进入文件管理界面\n\
       文件管理界面有如下命令：\n\
                [cd] 目录名\n\
                                切换文件目录\n\
                [mkdir] 目录名\n\
                                在当前目录下新建目录\n\
                [rmdir] 目录名\n\
                                删除当前目录下的目录\n\
                [ls] [dir]\n\
                                列出该目录下所有文件\n\
                [pwd] [cwd]\n\
                                返回当前所在绝对路径\n\
                [read] 文件名\n\
                                读取文件内容\n\
                [mkfile] 文件名\n\
                                建立新文件
                [delete] [rm] 文件名\n\
                                删除文件\n\
                [rename] 源文件名 新文件名\n\
                                重命名文件\n\
                [copy] 源文件名 新文件名\n\
                                复制源文件为新文件\n\
                [write] 文件名 文本内容\n\
                                向文件中写入内容，覆盖原内容\n\
                [writeto] 文件名 文本内容\n\
                                向文件中追加内容，不覆盖原内容\n\
                [upload] 本地文件 新文件名\n\
                                将本地文件上传至远程服务器\n\
                [download] 服务端文件\n\
                                将服务端文件下载至本地，保存后的文件将会在文件名前添加六位随机数\
"""