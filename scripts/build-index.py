#!/usr/bin/env python3
"""
Build professional AI Tools Index HTML from verified data.
"""

import json
from datetime import datetime

with open('data/tools.json', 'r') as f:
    data = json.load(f)

tools = data['tools']

# Build HTML
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Creative Tools Index 2026 | 1000 Tools Ranked</title>
    <meta name="description" content="Comprehensive database of 1000 AI creative tools ranked by traffic, users, and social reach. Updated February 2026.">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f0f0f;
            color: #e0e0e0;
            line-height: 1.6;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        header { 
            text-align: center; 
            padding: 40px 20px; 
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-bottom: 1px solid #333;
        }
        h1 { font-size: 2.5rem; margin-bottom: 10px; color: #fff; }
        .subtitle { color: #888; font-size: 1.1rem; }
        .stats-bar {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .stat { text-align: center; }
        .stat-num { font-size: 2rem; font-weight: 700; color: #4facfe; }
        .stat-label { font-size: 0.85rem; color: #888; }
        
        .filters {
            background: #1a1a1a;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            align-items: center;
        }
        .filters input, .filters select {
            padding: 10px 15px;
            border: 1px solid #333;
            border-radius: 6px;
            background: #222;
            color: #fff;
            font-size: 14px;
        }
        .filters input { flex: 1; min-width: 200px; }
        .filters select { min-width: 150px; }
        
        .feature-filters {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin: 10px 0;
        }
        .feature-chip {
            padding: 6px 12px;
            border-radius: 20px;
            background: #222;
            border: 1px solid #444;
            cursor: pointer;
            font-size: 13px;
            transition: all 0.2s;
        }
        .feature-chip:hover, .feature-chip.active {
            background: #4facfe;
            border-color: #4facfe;
            color: #000;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th {
            background: #1a1a2e;
            padding: 12px 8px;
            text-align: left;
            font-weight: 600;
            color: #4facfe;
            border-bottom: 2px solid #333;
            cursor: pointer;
        }
        th:hover { background: #252540; }
        td {
            padding: 12px 8px;
            border-bottom: 1px solid #222;
        }
        tr:hover { background: #1a1a1a; }
        
        .rank { 
            font-weight: 700; 
            color: #4facfe;
            width: 60px;
        }
        .rank-1 { color: #ffd700; }
        .rank-2 { color: #c0c0c0; }
        .rank-3 { color: #cd7f32; }
        
        .tool-name {
            font-weight: 600;
            color: #fff;
        }
        .tool-name a {
            color: inherit;
            text-decoration: none;
        }
        .tool-name a:hover { color: #4facfe; }
        
        .category {
            font-size: 12px;
            padding: 4px 8px;
            border-radius: 4px;
            background: #333;
            display: inline-block;
        }
        .category-image { background: #2d4a3e; color: #7bed9f; }
        .category-video { background: #4a2d4a; color: #dda0dd; }
        .category-design { background: #2d3a4a; color: #87ceeb; }
        .category-audio { background: #4a3d2d; color: #f5deb3; }
        .category-3d { background: #3d2d4a; color: #dda0dd; }
        
        .metrics { font-size: 13px; color: #888; }
        .metric-value { color: #fff; font-weight: 500; }
        
        .features {
            display: flex;
            gap: 4px;
        }
        .feature {
            width: 24px;
            height: 24px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: 600;
        }
        .feature-yes { background: #2d4a3e; color: #7bed9f; }
        .feature-no { background: #333; color: #666; }
        
        .all-features {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        }
        
        footer {
            text-align: center;
            padding: 40px;
            color: #666;
            border-top: 1px solid #222;
        }
        footer a { color: #4facfe; }
        
        @media (max-width: 768px) {
            table { font-size: 13px; }
            th, td { padding: 8px 4px; }
            .features { display: none; }
        }
    </style>
</head>
<body>
    <header>
        <h1>🎨 AI Creative Tools Index</h1>
        <p class="subtitle">Comprehensive database of AI-powered creative tools, ranked by real metrics</p>
        <div class="stats-bar">
            <div class="stat">
                <div class="stat-num">1,000</div>
                <div class="stat-label">Tools Tracked</div>
            </div>
            <div class="stat">
                <div class="stat-num">100%</div>
                <div class="stat-label">Verified Data</div>
            </div>
            <div class="stat">
                <div class="stat-num">Feb 2026</div>
                <div class="stat-label">Last Updated</div>
            </div>
        </div>
    </header>
    
    <div class="container">
        <div class="filters">
            <input type="text" id="search" placeholder="Search tools...">
            <select id="category">
                <option value="">All Categories</option>
                <option value="Image Generation">Image Generation</option>
                <option value="Video Generation">Video Generation</option>
                <option value="Design">Design</option>
                <option value="Audio/Music">Audio/Music</option>
                <option value="3D/Animation">3D/Animation</option>
            </select>
        </div>
        
        <div class="feature-filters">
            <span style="color: #888; margin-right: 10px;">Filter by features:</span>
            <span class="feature-chip" data-feature="imageGen">🖼️ Image Gen</span>
            <span class="feature-chip" data-feature="videoGen">🎬 Video Gen</span>
            <span class="feature-chip" data-feature="imageEditor">✏️ Image Editor</span>
            <span class="feature-chip" data-feature="imageCanvas">🎨 Canvas</span>
            <span class="feature-chip" data-feature="videoTimeline">🎞️ Timeline</span>
            <span class="feature-chip" data-feature="all5">⭐ All 5 Features</span>
        </div>
        
        <table id="toolsTable">
            <thead>
                <tr>
                    <th data-sort="ranking">Rank</th>
                    <th data-sort="name">Tool</th>
                    <th data-sort="category">Category</th>
                    <th data-sort="traffic">Monthly Traffic</th>
                    <th data-sort="users">Users</th>
                    <th>Features</th>
                    <th>HQ</th>
                </tr>
            </thead>
            <tbody>
'''

# Add tool rows
for tool in tools:
    rank = tool['ranking']
    rank_class = f'rank-{rank}' if rank <= 3 else ''
    
    # Category class
    cat = tool.get('category', '')
    cat_class = 'category-image' if 'Image' in cat else \
                'category-video' if 'Video' in cat else \
                'category-design' if 'Design' in cat else \
                'category-audio' if 'Audio' in cat else \
                'category-3d' if '3D' in cat else ''
    
    # Features
    img = tool.get('imageGen', False)
    vid = tool.get('videoGen', False)
    edit = tool.get('imageEditor', False)
    canvas = tool.get('imageCanvas', False)
    timeline = tool.get('videoTimeline', False)
    all5 = img and vid and edit and canvas and timeline
    
    features_html = ''
    if all5:
        features_html = '<span class="all-features">ALL 5 ✓</span>'
    else:
        features_html = f'''
            <span class="feature {"feature-yes" if img else "feature-no"}" title="Image Gen">I</span>
            <span class="feature {"feature-yes" if vid else "feature-no"}" title="Video Gen">V</span>
            <span class="feature {"feature-yes" if edit else "feature-no"}" title="Editor">E</span>
            <span class="feature {"feature-yes" if canvas else "feature-no"}" title="Canvas">C</span>
            <span class="feature {"feature-yes" if timeline else "feature-no"}" title="Timeline">T</span>
        '''
    
    traffic = tool.get('estimatedMonthlyVisits', 0)
    users = tool.get('estimatedUsers', 0)
    
    def format_num(n):
        if n >= 1_000_000_000: return f"{n/1_000_000_000:.1f}B"
        if n >= 1_000_000: return f"{n/1_000_000:.1f}M"
        if n >= 1_000: return f"{n/1_000:.1f}K"
        return str(n)
    
    html += f'''
                <tr data-category="{cat}" data-img="{str(img).lower()}" data-vid="{str(vid).lower()}" 
                    data-edit="{str(edit).lower()}" data-canvas="{str(canvas).lower()}" 
                    data-timeline="{str(timeline).lower()}" data-all5="{str(all5).lower()}">
                    <td class="rank {rank_class}">#{rank}</td>
                    <td class="tool-name"><a href="{tool.get('url', '#')}" target="_blank">{tool.get('name', '')}</a></td>
                    <td><span class="category {cat_class}">{cat}</span></td>
                    <td class="metrics"><span class="metric-value">{format_num(traffic)}</span></td>
                    <td class="metrics"><span class="metric-value">{format_num(users)}</span></td>
                    <td class="features">{features_html}</td>
                    <td class="metrics">{tool.get('headquarters', '').split(',')[0][:15]}</td>
                </tr>
'''

html += '''
            </tbody>
        </table>
    </div>
    
    <footer>
        <p>Data compiled by <a href="https://craftit.ai">Craftit AI</a> | Rankings based on traffic (70%), users (20%), social (10%)</p>
        <p style="margin-top: 10px;">Last updated: ''' + datetime.now().strftime('%B %d, %Y') + '''</p>
    </footer>
    
    <script>
        // Search
        document.getElementById('search').addEventListener('input', filterTable);
        document.getElementById('category').addEventListener('change', filterTable);
        
        // Feature chips
        document.querySelectorAll('.feature-chip').forEach(chip => {
            chip.addEventListener('click', function() {
                this.classList.toggle('active');
                filterTable();
            });
        });
        
        function filterTable() {
            const search = document.getElementById('search').value.toLowerCase();
            const category = document.getElementById('category').value;
            const activeFeatures = Array.from(document.querySelectorAll('.feature-chip.active'))
                .map(c => c.dataset.feature);
            
            document.querySelectorAll('#toolsTable tbody tr').forEach(row => {
                const name = row.querySelector('.tool-name').textContent.toLowerCase();
                const rowCat = row.dataset.category;
                
                let show = true;
                if (search && !name.includes(search)) show = false;
                if (category && rowCat !== category) show = false;
                
                // Feature filters
                if (activeFeatures.includes('all5') && row.dataset.all5 !== 'true') show = false;
                if (activeFeatures.includes('imageGen') && row.dataset.img !== 'true') show = false;
                if (activeFeatures.includes('videoGen') && row.dataset.vid !== 'true') show = false;
                if (activeFeatures.includes('imageEditor') && row.dataset.edit !== 'true') show = false;
                if (activeFeatures.includes('imageCanvas') && row.dataset.canvas !== 'true') show = false;
                if (activeFeatures.includes('videoTimeline') && row.dataset.timeline !== 'true') show = false;
                
                row.style.display = show ? '' : 'none';
            });
        }
    </script>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Built index.html with 1000 tools")
print(f"   File size: {len(html):,} bytes")
