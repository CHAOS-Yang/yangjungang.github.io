# CalendarLab：Agent 错误工具调用的安全提醒与纠正

一个静态单页实验，用来比较“无提醒直接执行”和“有提醒拦截并重试”两条分支。所有日程和修改操作都是模拟数据，不连接真实日历。

## 页面

打开 `index.html`。

页面包含：

- 正常描述、干扰无提醒、干扰有提醒三条分支演示；
- 拦截成功、模型改正、任务完成三个不同结果；
- 实验步骤、结果判断表和最低验收标准；
- starter 下载与任务卡。

任务接应人：计算机工程与科学学院-24121930-马诗絮；邮箱：msx@shu.edu.cn。

## Starter

```text
starter/
├── calendar_agent.py
├── experiment_record_template.md
└── README.md
```

`calendar_starter.zip` 是这三个文件的压缩包。

先运行离线演示：

```powershell
cd D:\AI\Codex\AgentStudy\CalendarLab\starter
python calendar_agent.py --offline-demo
```

真实模式需要自行设置 `OPENAI_BASE_URL`、`OPENAI_API_KEY`、`OPENAI_MODEL`，不要把密钥写进代码或提交材料。

## 放进 AgentLab 站点

把整个 `CalendarLab` 文件夹复制到：

```text
D:\AgentLab\yangjungang.github.io\labs\CalendarLab\
```

主页面卡片链接使用：

```html
<a class="challenge-card lab-card" href="../labs/CalendarLab/index.html">
```

不需要后端或构建步骤，GitHub Pages 可以直接托管。
