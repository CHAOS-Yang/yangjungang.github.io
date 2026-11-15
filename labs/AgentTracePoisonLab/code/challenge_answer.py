"""综合实验：审查 Agent 训练示范轨迹，并比较不同来源的可疑比例。"""

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

        if tool_name not in allowed_tools:
            findings.append({
                "tool": tool_name,
                "reason": "不在允许工具列表中",
            })

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

        source_stats[source]["total"] += 1

        if findings:
            suspicious_trace_count += 1
            source_stats[source]["suspicious"] += 1

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
        percentage = (suspicious / total * 100) if total else 0.0
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
