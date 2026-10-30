# IoTLab：IoT Agent 工具调用安全实验

一个静态单页实验，用来观察外部设备描述会不会影响 Agent 的工具选择。所有设备和状态都是模拟数据，不连接真实硬件。

## 页面

打开 `index.html` 或双击 `start-iot-lab.cmd（已去除）`。

页面包含：

- normal / injected / 厨房灯边界三种场景切换；
- 设备列表和模型工具调用的对照演示；
- Exposure、Proposed、Executed 三个判断层级；
- 实验步骤、最低验收标准和 starter 下载；
- 任务接应人：计算机工程与科学学院-24122292-郭宇晟，kristy@shu.edu.cn。

## Starter

目录：

```text
starter/
├── iot_agent_tool_lab.py
├── experiment_record_template.md
└── README.md
```

`iot_starter.zip` 是这三个文件的压缩包。

先运行离线演示：

```powershell
cd D:\AI\Codex\AgentStudy\IoTLab\starter
python iot_agent_tool_lab.py --offline-demo --mode normal
python iot_agent_tool_lab.py --offline-demo --mode injected
```

真实模式需要自行设置 `OPENAI_BASE_URL`、`OPENAI_API_KEY`、`OPENAI_MODEL`，不要把密钥写进代码或提交材料。

## 放进 AgentLab 站点

把整个 `IoTLab` 文件夹复制到：

```text
D:\AgentLab\yangjungang.github.io\Lab\IoTLab\
```

主页面卡片链接使用：

```html
<a class="challenge-card lab-card" href="../Lab/IoTLab/index.html">
```

不需要新增后端或构建步骤，GitHub Pages 可以直接托管。

