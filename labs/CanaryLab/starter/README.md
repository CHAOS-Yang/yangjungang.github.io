# Canary 越狱评测 Starter

这个小实验帮助你完成一次最小规模的提示词绕过评测：读用例、调用模型、判断是否泄露、统计结果。

## 环境

- Python 3.10 或更高版本。
- 只用 Python 标准库，不需要安装额外包。
- 真实模式需要一个支持 OpenAI-compatible Chat Completions 的模型接口。

## 先跑离线演示

```powershell
python canary_agent_lab.py --offline-demo
```

离线演示不会调用模型，只用固定输出演示 exact / variant / reversed 三种检测结果。

## 再跑真实对照

在 PowerShell 中设置环境变量（不要写进代码或提交文件）：

```powershell
$env:OPENAI_BASE_URL = "https://你的模型服务地址/v1"
$env:OPENAI_API_KEY = "你的密钥"
$env:OPENAI_MODEL = "你实际可用的模型名"
```

然后：

```powershell
python canary_agent_lab.py --cases cases.example.json --repeats 2 --output results.csv
```

运行结束后会生成 `results.csv`，并打印尝试次数、有效次数、泄露次数和比例。

## 你要做的六条用例

在 `cases.example.json` 基础上扩展到 6 条：

- 直接命令 2 条；
- 换身份 2 条；
- 换写法 2 条；
- 至少 1 条使用变体（空格、下划线或倒序）；
- 至少 1 条改成两轮对话（`turns` 数组放两条）。

## 提交内容

```text
Canary-Lab/
├── canary_agent_lab.py
├── cases.json
├── results.csv
├── experiment_record.md
└── README.md
```

最低要求：

1. `--offline-demo` 可以运行；
2. 至少修改过一条用例，并说明改了什么；
3. 6 条用例各跑 2 次，有原始输出；
4. 有分类汇总表和 150-200 字复盘；
5. 没有真实密钥、隐私或危险请求。

## 安全边界

- 只用 `BLUE-17` 这类虚构口令；
- 不把真实 API Key 写进代码、截图或提交材料；
- 不测试第三方平台；
- 小样本结果只描述当前测试集，不代表模型的普遍安全结论。
