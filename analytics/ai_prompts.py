def captain_prompt(context):
    lines = []
    for p in context:
        lines.append(
            f"- {p['web_name']} ({p['team_name']}): "
            f"{p['avg_points']:.2f} avg points over {p['matches']} matches"
        )

    return f"""
Based on the following FPL data, recommend the best captain pick.

Candidates:
{chr(10).join(lines)}

Explain your reasoning clearly using form, consistency, and risk.
"""
