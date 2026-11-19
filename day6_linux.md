# Day 6：Linux 命令入门

## 为什么学这个？
岗位 JD 写了「熟悉 Linux 命令」。服务器基本都跑 Linux，实施岗部署项目、查日志、改配置都要在 Linux 上操作命令行。

## 学习方式
你是 Windows，但装了 Git Bash（Git 自带）。打开 **Git Bash**（开始菜单搜 "Git Bash"），下面的命令在里面跑。

## 先准备一个练习目录
在 Git Bash 里执行（注意 Git Bash 的路径写法，e盘是 /e/）：
```bash
cd /e/shixi
mkdir -p linux_practice/subdir
cd linux_practice
echo "hello world" > a.txt
echo "second line" >> a.txt
echo "foo bar baz" > b.txt
echo "123 456 789" >> b.txt
```

---

## 一、文件目录操作（最常用）

| 命令 | 作用 | 例子 |
|------|------|------|
| `pwd` | 显示当前目录 | `pwd` |
| `ls` | 列出文件 | `ls` 、 `ls -l` 、 `ls -la` |
| `cd` | 切换目录 | `cd subdir` 、 `cd ..`（上一级） |
| `mkdir` | 新建目录 | `mkdir newdir` |
| `touch` | 新建空文件 | `touch c.txt` |
| `cp` | 复制 | `cp a.txt a_backup.txt` |
| `mv` | 移动/改名 | `mv c.txt subdir/` |
| `rm` | 删除 | `rm a_backup.txt` |
| `rmdir` | 删空目录 | `rmdir newdir` |

**练习 1**：
1. 进入 `/e/shixi/linux_practice`
2. 用 `ls -la` 看所有文件（包括隐藏文件）
3. 新建目录 `test`，进去，再 `cd ..` 回来
4. 把 `b.txt` 复制一份叫 `b_copy.txt`，然后删掉它

---

## 二、查看文件内容

| 命令 | 作用 | 例子 |
|------|------|------|
| `cat` | 打印整个文件 | `cat a.txt` |
| `head` | 看前几行 | `head a.txt` |
| `tail` | 看后几行 | `tail a.txt` |
| `less` | 分页查看（q 退出） | `less a.txt` |
| `wc` | 统计行数/字数 | `wc -l a.txt` |

**练习 2**：
1. `cat a.txt` 看内容
2. `wc -l a.txt` 数有几行

---

## 三、查找与搜索（岗位高频）

| 命令 | 作用 | 例子 |
|------|------|------|
| `grep` | 在文件里搜内容 | `grep "hello" a.txt` |
| `find` | 找文件 | `find . -name "*.txt"` |
| `which` | 找命令在哪 | `which python` |

**grep 是实施岗查日志的神器**，比如：
```bash
grep "ERROR" app.log        # 搜错误日志
grep -i "error" app.log     # 忽略大小写
grep -r "关键字" .          # 递归搜当前目录所有文件
```

**练习 3**：
1. `grep "hello" a.txt`
2. `find /e/shixi -name "*.csv"` 找出所有 csv 文件

---

## 四、管道 `|` 和重定向

这是 Linux 的精髓：把一个命令的输出，喂给下一个命令。

```bash
cat a.txt | grep "hello"     # 先 cat 再 grep
ls -la | head -5             # 只看前5行
grep "hello" a.txt > result.txt   # 把结果写入文件（覆盖）
grep "hello" a.txt >> result.txt  # 追加到文件末尾
```

**练习 4**：
1. `cat a.txt | wc -l` —— 用管道统计行数
2. `ls /e/shixi > filelist.txt` —— 把文件列表写入文件

---

## 五、进程与权限（了解即可）

| 命令 | 作用 |
|------|------|
| `ps` | 查看进程（`ps aux` 看全部） |
| `top` | 实时看资源占用（q 退出） |
| `kill` | 杀进程（`kill 进程号`） |
| `chmod` | 改权限（`chmod +x file.sh` 加执行权限） |
| `chown` | 改所有者 |

---

## 六、其他常用

| 命令 | 作用 |
|------|------|
| `echo` | 打印文本 |
| `clear` | 清屏（或 Ctrl+L） |
| `history` | 看历史命令 |
| `man 命令` | 看帮助（`man grep`） |
| `sudo` | 以管理员身份运行（加在命令前） |

---

## Day 6 验收标准
- 能在 Git Bash 里用 `ls / cd / mkdir / cp / rm` 操作文件
- 会用 `grep` 搜文件内容
- 理解 `|` 管道和 `>` 重定向的作用

## 做完后
把练习 1-4 的命令和输出贴给我检查。
