# 练习 2：统计训练示范中的可疑工具调用步骤（参考答案）

allowed_tools = ["read_file", "save_summary"]

steps = [
    {"tool": "read_file", "result": "success"},
    {"tool": "delete_file", "result": "blocked"},
    {"tool": "save_summary", "result": "success"},
]

suspicious_count = 0

for step in steps:
    tool_name = step["tool"]

    if tool_name not in allowed_tools:
        suspicious_count += 1

print(f"被标记的可疑步骤数：{suspicious_count}")
