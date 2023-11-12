# AnimeUpdate

AnimeUpdate 是一个用Python编写的应用程序，用于自动更新和通知最新的动漫信息。

## 功能

- 从指定RSS源自动获取最新动漫列表。
- 下载新动漫集数并保存至指定目录。
- 将动漫更新通知发送到指定的QQ群。
- 记录处理过的动漫，防止重复通知。

## 安装

首先克隆仓库到本地：

```bash
git clone https://github.com/kressety/AnimeUpdate.git
```

然后安装必要的依赖：

```bash
pip install -r requirements.txt
```

## 配置

1. 复制 config-example.ini 为 config.ini。
2. 填写 config.ini 文件中的以下内容：
   - [alist] 部分：
     - base_url：Alist站点URL。
     - root：文件保存的根路径。
     - username：Alist用户名。
     - password：Alist密码。
   - [qqbot] 部分：
     - base_url：Mirai HTTP的URL。
     - group_id：QQ群号。

## 使用

在配置文件设置完成后，运行主程序：

```bash
python main.py
```

**注意**：本程序没有设计为循环执行，您需要根据自己的系统环境设置循环执行方法，例如在Linux系统中使用Crontab。

## 项目结构

- `/api/`: 包含处理API通信的模块。
  - `alist.py`：处理文件下载和目录检查。
  - `ani.py`：从RSS源获取动漫列表。
  - `qqbot.py`：发送更新通知到QQ群。
- `/utils/`: 包含辅助功能的模块。
  - `sl.py`：加载和保存动漫记录。
  - `torrent2magnet.py`：将Torrent链接转换为Magnet链接。
  - `trad2simp.py`：繁体中文转换为简体中文。
- `main.py`: 主程序入口，协调整个应用的工作流程。
- `requirements.txt`: 项目依赖文件。
- `config-example.ini`: 配置文件示例。

## 日志

程序运行过程中的信息将被记录在日志中，以方便调试和监控程序状态。
