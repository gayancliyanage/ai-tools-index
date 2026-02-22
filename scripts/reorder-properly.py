#!/usr/bin/env python3
"""
Reorder AI Tools Index properly:
1. Sort all tools by actual metrics (traffic + users)
2. Assign rankings based on sorted order
3. Make id = ranking for consistency
"""

import json
from datetime import datetime

with open('data/tools.json', 'r') as f:
    data = json.load(f)

tools = data['tools']

# Calculate a score for each tool based on metrics
def get_score(tool):
    traffic = tool.get('estimatedMonthlyVisits', 0) or 0
    users = tool.get('estimatedUsers', 0) or 0
    
    # Social reach
    social = tool.get('social', {})
    ig = social.get('instagram', 0) or 0
    tt = social.get('tiktok', 0) or 0
    tw = social.get('twitter', 0) or 0
    yt = social.get('youtube', 0) or 0
    dc = social.get('discord', 0) or 0
    li = social.get('linkedin', 0) or 0
    
    # Weighted social score (same weights as before)
    social_score = (ig * 0.30 + tt * 0.25 + tw * 0.20 + yt * 0.15 + dc * 0.05 + li * 0.05)
    
    # Combined score: traffic (50%) + users (30%) + social (20%)
    total = (traffic * 0.5) + (users * 0.3) + (social_score * 0.2)
    return total

# Sort tools by score (descending = highest score gets rank 1)
tools_with_scores = [(t, get_score(t)) for t in tools]
tools_with_scores.sort(key=lambda x: x[1], reverse=True)

# Reassign id and ranking based on sorted order
for i, (tool, score) in enumerate(tools_with_scores, start=1):
    tool['id'] = i
    tool['ranking'] = i

# Update the tools array
data['tools'] = [t for t, s in tools_with_scores]
data['lastUpdated'] = datetime.now().isoformat()
data['dataNote'] = "Rankings computed from combined metrics: traffic (50%), users (30%), social reach (20%). Sorted and reordered Feb 2026."

# Find Craftit's new position
for tool in data['tools']:
    if 'craftit' in tool.get('name', '').lower():
        print(f"Craftit AI: Rank #{tool['ranking']} (Traffic: {tool.get('estimatedMonthlyVisits'):,}, Users: {tool.get('estimatedUsers'):,})")

# Save
with open('data/tools.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✅ Reordered {len(tools)} tools by actual metrics")
print("Top 10:")
for t in data['tools'][:10]:
    print(f"  #{t['ranking']} {t['name']} - {t.get('estimatedMonthlyVisits', 0):,} visits")
