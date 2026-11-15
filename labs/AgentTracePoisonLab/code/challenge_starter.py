"""综合实验：补全关键代码，检查 Agent 训练示范轨迹。"""

import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "trajectories.json"


def load_traces():
    """读取模拟训练轨迹数据。"""
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def find_suspicious_steps(trace):
    """找出单条轨迹中违反工具白名单规则的步骤。"""
    findings = []
    allowed_tools = trace["allowed_tools"]

    for step in trace["steps"]:
        tool_name = step["tool"]

        # TODO 1：将 False 替换为工具名称不在 allowed_tools 中的判断条件
        if False:
            # TODO 2：删除 pass，使用 findings.append(...) 记录工具名称和原因
            # 记录格式：{"tool": tool_name, "reason": "不在允许工具列表中"}
            pass

    return findings


def audit_traces(traces):
    """汇总可疑步骤，按轨迹统计各来源的可疑数量。"""
    suspicious_records = []
    suspicious_trace_count = 0
    source_stats = {}

    for trace in traces:
        trace_id = trace["trace_id"]
        source = trace["source"]
        findings = find_suspicious_steps(trace)

        if source not in source_stats:
            source_stats[source] = {"total": 0, "suspicious": 0}

        # TODO 3：删除 pass，将当前来源的轨迹总数加 1
        pass

        if findings:
            suspicious_trace_count += 1
            # TODO 4：删除 pass，将当前来源的可疑轨迹数加 1
            # 注意：一条轨迹即使有两个可疑步骤，也只计为一条可疑轨迹
            pass

        for finding in findings:
            suspicious_records.append({
                "trace_id": trace_id,
                "source": source,
                "tool": finding["tool"],
                "reason": finding["reason"],
            })

    return suspicious_records, suspicious_trace_count, source_stats


def print_report(traces, suspicious_records, suspicious_trace_count, source_stats):
    """打印固定格式的审查报告。"""
    print("Agent 训练轨迹审查报告")
    print("========================")
    print(f"轨迹总数：{len(traces)}")
    print()

    print("一、可疑工具调用")
    if not suspicious_records:
        print("未发现触发本次规则的步骤")
    else:
        for record in suspicious_records:
            print(
                f"[可疑轨迹] {record['trace_id']} | 来源 {record['source']} | "
                f"{record['tool']} {record['reason']}"
            )
    print(f"可疑步骤数：{len(suspicious_records)}")
    print(f"可疑轨迹数：{suspicious_trace_count}")
    print()

    print("二、来源对照")
    for source in sorted(source_stats):
        total = source_stats[source]["total"]
        suspicious = source_stats[source]["suspicious"]
        percentage = 0.0  # TODO 5：根据 total 和 suspicious 计算百分比
        print(
            f"来源 {source}：总数 {total}，可疑 {suspicious}，"
            f"可疑比例 {percentage:.1f}%"
        )


def main():
    traces = load_traces()
    suspicious_records, suspicious_trace_count, source_stats = audit_traces(traces)
    print_report(traces, suspicious_records, suspicious_trace_count, source_stats)


if __name__ == "__main__":
    main()
