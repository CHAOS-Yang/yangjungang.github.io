# 练习 1：读取 Agent 轨迹中的工具名称（参考答案）

trace = {
    "trace_id": "DEMO01",
    "source": "A",
    "task": "读取 report.txt 并保存摘要，保留原文件",
    "allowed_tools": ["read_file", "save_summary"],
    "steps": [
        {
            "tool": "read_file",
            "args": {"filename": "report.txt"},
            "result": "success",
        },
        {
            "tool": "save_summary",
            "args": {"filename": "summary.txt"},
            "result": "success",
        },
    ],
}

print(f"轨迹编号：{trace['trace_id']}")

for step in trace["steps"]:
    tool_name = step["tool"]
    print(f"调用工具：{tool_name}")
