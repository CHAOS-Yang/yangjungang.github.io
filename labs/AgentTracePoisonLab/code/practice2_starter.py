# 练习 2：统计训练示范中的可疑工具调用步骤

allowed_tools = ["read_file", "save_summary"]

steps = [
    {"tool": "read_file", "result": "success"},
    {"tool": "delete_file", "result": "blocked"},
    {"tool": "save_summary", "result": "success"},
]

suspicious_count = 0

for step in steps:
    tool_name = step["tool"]

    # TODO 1：替换 False，判断 tool_name 是否不在 allowed_tools 中
    if False:
        # TODO 2：删除 pass，将 suspicious_count 加 1
        pass

print(f"被标记的可疑步骤数：{suspicious_count}")
