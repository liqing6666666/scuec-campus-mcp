# SCUEC Campus MCP Server

中南民族大学校园百事通 MCP Server — 为 MaxKB 等 AI 平台提供校园设施查询、导航等能力。

## 工具

| Tool | 说明 |
|------|------|
| `search_campus_pois` | 按关键词搜索校园设施 |
| `get_poi_detail` | 获取设施详情（坐标、描述、标签） |
| `list_categories` | 列出 6 个分类及设施数量 |
| `get_category_pois` | 获取某分类下所有设施 |
| `get_navigation_url` | 生成高德步行导航链接 |
| `get_campus_boundary` | 获取校园边界坐标 |
| `get_nearest_poi` | 查找离指定位置最近的设施 |

## 资源

| URI | 内容 |
|-----|------|
| `campus://pois` | 全部 49 个 POI 数据 |
| `campus://categories` | 6 个分类定义 |
| `campus://outline` | 校园轮廓 24 个坐标点 |

## 使用

### 本地调试

```bash
pip install "mcp[cli]"
mcp dev server.py
```

### MaxKB 配置

```json
{
  "campus-map": {
    "url": "https://api.modelscope.cn/mcp/xxx/sse",
    "transport": "sse"
  }
}
```

### SSE 模式启动

```bash
python server.py --sse
```

## 数据

坐标系统: GCJ-02 (高德坐标系)
数据来源: 中南民族大学校园地理数据
