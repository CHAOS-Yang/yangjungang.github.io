# Agent 轨迹投毒侦探 · Lab 页面

Agent 安全方向的本科入门实验：观察 Agent 训练示范轨迹，用一段 Python 规则检查轨迹里有没有不符合任务约定的工具调用。

- 实验页面：`index.html`（自包含单页，无需构建、无外部依赖）
- 学生 starter 包：`agent_trace_starter.zip`（解压后保持 `code/ data/ outputs/` 目录结构，`python code/challenge_starter.py` 需在项目根执行）
- 分发用静态资源：`code/`（3 个 starter + 3 个答案）、`data/trajectories.json`（8 条模拟轨迹）、`outputs/expected_output.txt`（参考输出）

页面内容与交互：4 道选择题（点击即出对错与解析，可重选）、3 道代码补全题（默认展示 starter，可展开参考答案与实际输出并复制）、8 条轨迹对照表、实验完成自检进度、资源下载与联系方式。

页面里的代码与 `code/*.py`、`data/*.json`、`outputs/expected_output.txt` 完全一致；改这些文件后需要同步重新生成 `index.html`（构建脚本在站点仓库外，改文件时同步改动页面里的对应代码块）。

素材来源：付于文（Agent 轨迹安全方向）的交付材料。
