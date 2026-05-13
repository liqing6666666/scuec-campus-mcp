"""
中南民族大学 - 校园百事通 MCP Server
使用 FastMCP 框架，提供校园设施查询、导航等能力
支持 SSE 和 Streamable HTTP 传输协议，可直接接入 MaxKB / ModelScope
"""

import math
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("campus-map", host="0.0.0.0", port=8000)

# ===== 校园 POI 数据 =====
CAMPUS_POIS = [
    # ---- 驿站 ----
    {"name": "23栋菜鸟驿站", "category": "驿站", "lng": 114.392303, "lat": 30.479495,
     "desc": "湖北省武汉市洪山区民族大道182号中南民族大学23栋菜鸟驿站", "tags": ["快递", "菜鸟"]},
    {"name": "25栋菜鸟驿站", "category": "驿站", "lng": 114.393244, "lat": 30.479531,
     "desc": "湖北省武汉市洪山区民族大道182号中南民族大学25栋菜鸟驿站", "tags": ["快递", "菜鸟"]},
    {"name": "北区菜鸟驿站", "category": "驿站", "lng": 114.395414, "lat": 30.493787,
     "desc": "湖北省武汉市洪山区民族大道182号中南民族大学北区学生公寓", "tags": ["快递", "菜鸟"]},

    # ---- 图书馆 ----
    {"name": "南区分馆", "category": "图书馆", "lng": 114.392468, "lat": 30.48102,
     "desc": "图书馆南区分馆", "tags": ["自习", "借书"]},
    {"name": "南书院", "category": "图书馆", "lng": 114.392078, "lat": 30.486579,
     "desc": "南书院自习区", "tags": ["自习"]},
    {"name": "双塔楼", "category": "图书馆", "lng": 114.391608, "lat": 30.487281,
     "desc": "双塔楼图书馆", "tags": ["自习", "借书"]},
    {"name": "老馆", "category": "图书馆", "lng": 114.392534, "lat": 30.487233,
     "desc": "老图书馆", "tags": ["自习", "借书"]},
    {"name": "北书院", "category": "图书馆", "lng": 114.392072, "lat": 30.487857,
     "desc": "北书院自习区", "tags": ["自习"]},
    {"name": "北区分馆-3A", "category": "图书馆", "lng": 114.395321, "lat": 30.495252,
     "desc": "北区分馆3A自习区", "tags": ["自习"]},
    {"name": "北区分馆-鲲鹏书院", "category": "图书馆", "lng": 114.396933, "lat": 30.495173,
     "desc": "鲲鹏书院自习区", "tags": ["自习"]},

    # ---- 教学楼 ----
    {"name": "1号教学楼", "category": "教学楼", "lng": 114.393552, "lat": 30.488275, "desc": "教学楼", "tags": ["教室"]},
    {"name": "2号教学楼", "category": "教学楼", "lng": 114.39264, "lat": 30.488261, "desc": "教学楼", "tags": ["教室"]},
    {"name": "4号教学楼", "category": "教学楼", "lng": 114.394778, "lat": 30.486846, "desc": "教学楼", "tags": ["教室"]},
    {"name": "7号教学楼", "category": "教学楼", "lng": 114.393842, "lat": 30.484338, "desc": "教学楼", "tags": ["教室"]},
    {"name": "9号教学楼", "category": "教学楼", "lng": 114.390118, "lat": 30.489614, "desc": "教学楼", "tags": ["教室"]},
    {"name": "10号教学楼", "category": "教学楼", "lng": 114.392632, "lat": 30.490622, "desc": "教学楼", "tags": ["教室"]},
    {"name": "11号教学楼", "category": "教学楼", "lng": 114.390722, "lat": 30.490246, "desc": "教学楼", "tags": ["教室"]},
    {"name": "13号教学楼", "category": "教学楼", "lng": 114.390386, "lat": 30.491092, "desc": "教学楼", "tags": ["教室"]},
    {"name": "14号教学楼", "category": "教学楼", "lng": 114.395122, "lat": 30.49037, "desc": "教学楼", "tags": ["教室"]},
    {"name": "15号教学楼", "category": "教学楼", "lng": 114.392019, "lat": 30.491828, "desc": "教学楼", "tags": ["教室"]},
    {"name": "16号教学楼", "category": "教学楼", "lng": 114.395866, "lat": 30.492735, "desc": "教学楼", "tags": ["教室"]},
    {"name": "17号教学楼", "category": "教学楼", "lng": 114.394956, "lat": 30.488739, "desc": "教学楼", "tags": ["教室"]},
    {"name": "光谷音乐厅", "category": "教学楼", "lng": 114.395284, "lat": 30.490433, "desc": "中南民族大学光谷音乐厅", "tags": ["演出", "活动"]},
    {"name": "光谷美术馆", "category": "教学楼", "lng": 114.395378, "lat": 30.491326, "desc": "中南民族大学光谷美术馆", "tags": ["展览"]},
    {"name": "学术会堂", "category": "教学楼", "lng": 114.391077, "lat": 30.489721, "desc": "学术会堂", "tags": ["会议", "讲座"]},
    {"name": "大学生活动中心", "category": "教学楼", "lng": 114.393173, "lat": 30.483003, "desc": "大学生活动中心", "tags": ["活动", "社团"]},
    {"name": "大礼堂", "category": "教学楼", "lng": 114.394871, "lat": 30.489689, "desc": "大礼堂", "tags": ["演出", "典礼"]},
    {"name": "体育馆", "category": "教学楼", "lng": 114.394006, "lat": 30.483417, "desc": "体育馆", "tags": ["运动", "篮球"]},
    {"name": "行政楼", "category": "教学楼", "lng": 114.394735, "lat": 30.487642, "desc": "行政楼", "tags": ["办公"]},
    {"name": "国际合作与交流处", "category": "教学楼", "lng": 114.389332, "lat": 30.480873, "desc": "国际合作与交流处", "tags": ["留学", "交流"]},
    {"name": "学术交流中心", "category": "教学楼", "lng": 114.392574, "lat": 30.48724, "desc": "学术交流中心", "tags": ["会议"]},
    {"name": "国际学术会议中心", "category": "教学楼", "lng": 114.388794, "lat": 30.481729, "desc": "国际学术会议中心", "tags": ["会议"]},
    {"name": "民族学博物馆", "category": "教学楼", "lng": 114.38954, "lat": 30.482684, "desc": "民族学博物馆", "tags": ["展览", "参观"]},
    {"name": "体育训练中心", "category": "教学楼", "lng": 114.394823, "lat": 30.488747, "desc": "体育训练中心", "tags": ["运动"]},
    {"name": "游泳馆", "category": "教学楼", "lng": 114.393818, "lat": 30.480472, "desc": "游泳馆", "tags": ["游泳"]},

    # ---- 食堂 ----
    {"name": "1食堂", "category": "食堂", "lng": 114.391489, "lat": 30.482543, "desc": "1食堂", "tags": ["餐饮"]},
    {"name": "2食堂", "category": "食堂", "lng": 114.391517, "lat": 30.481763, "desc": "2食堂", "tags": ["餐饮"]},
    {"name": "3食堂", "category": "食堂", "lng": 114.391485, "lat": 30.480584, "desc": "3食堂", "tags": ["餐饮"]},
    {"name": "4食堂", "category": "食堂", "lng": 114.392245, "lat": 30.481202, "desc": "4食堂", "tags": ["餐饮"]},
    {"name": "南湖园餐厅", "category": "食堂", "lng": 114.394741, "lat": 30.484292, "desc": "南湖园餐厅", "tags": ["餐饮"]},
    {"name": "中心食堂", "category": "食堂", "lng": 114.394355, "lat": 30.490416, "desc": "中心食堂", "tags": ["餐饮"]},
    {"name": "北区食堂", "category": "食堂", "lng": 114.395947, "lat": 30.494742, "desc": "北区食堂", "tags": ["餐饮"]},
    {"name": "小吃街", "category": "食堂", "lng": 114.391111, "lat": 30.482122, "desc": "小吃街", "tags": ["小吃", "夜宵"]},

    # ---- 打印店 ----
    {"name": "21栋打印店", "category": "打印店", "lng": 114.391163, "lat": 30.479922, "desc": "21栋打印店", "tags": ["打印", "复印"]},
    {"name": "民大读书坊打印", "category": "打印店", "lng": 114.391328, "lat": 30.482091, "desc": "民大读书坊打印", "tags": ["打印", "复印"]},
    {"name": "大购打印", "category": "打印店", "lng": 114.391338, "lat": 30.482726, "desc": "大购打印", "tags": ["打印", "复印"]},
    {"name": "图书馆打印", "category": "打印店", "lng": 114.392194, "lat": 30.486725, "desc": "图书馆打印", "tags": ["打印", "复印"]},
    {"name": "樱果打印", "category": "打印店", "lng": 114.395198, "lat": 30.491867, "desc": "樱果打印", "tags": ["打印", "复印"]},

    # ---- 医院 ----
    {"name": "校医院", "category": "医院", "lng": 114.396986, "lat": 30.487635, "desc": "校医院", "tags": ["看病", "急诊"]},
    {"name": "南区药店", "category": "医院", "lng": 114.391331, "lat": 30.482669, "desc": "南区药店", "tags": ["买药"]},
    {"name": "北区药店", "category": "医院", "lng": 114.396053, "lat": 30.49486, "desc": "北区药店", "tags": ["买药"]},
]

# ===== 校园轮廓坐标 =====
CAMPUS_OUTLINE = [
    [114.39748, 30.495551],
    [114.394285, 30.495858],
    [114.394206, 30.495295],
    [114.393608, 30.495332],
    [114.393627, 30.49395],
    [114.394468, 30.493813],
    [114.394196, 30.491928],
    [114.390864, 30.492279],
    [114.389116, 30.489683],
    [114.391453, 30.488433],
    [114.391197, 30.486801],
    [114.391553, 30.484705],
    [114.390936, 30.483686],
    [114.388847, 30.482916],
    [114.388322, 30.482305],
    [114.388243, 30.481807],
    [114.388966, 30.479305],
    [114.393949, 30.479338],
    [114.393944, 30.4793],
    [114.395021, 30.47955],
    [114.395243, 30.479752],
    [114.395561, 30.484103],
    [114.39581, 30.489248],
    [114.39577, 30.489442],
]

# ===== 分类定义 =====
CATEGORIES = [
    {"key": "驿站", "color": "#fa8c16", "icon": "📦"},
    {"key": "图书馆", "color": "#722ed1", "icon": "📚"},
    {"key": "教学楼", "color": "#1890ff", "icon": "🏫"},
    {"key": "食堂", "color": "#eb2f96", "icon": "🍜"},
    {"key": "打印店", "color": "#13c2c2", "icon": "🖨"},
    {"key": "医院", "color": "#f5222d", "icon": "🏥"},
]

# ===== 高德地图导航基准 URL =====
AMAP_NAV_BASE = "https://uri.amap.com/navigation"
MAP_BASE_URL = "http://8.160.169.239:8080"


def _find_poi(name: str) -> dict | None:
    """内部: 按名称精确查找 POI（支持模糊匹配）"""
    for p in CAMPUS_POIS:
        if p["name"] == name:
            return p
    # 模糊匹配
    for p in CAMPUS_POIS:
        if name in p["name"]:
            return p
    return None


def _calc_distance(lng1: float, lat1: float, lng2: float, lat2: float) -> float:
    """计算两点间距离 (米)，使用简化的球面余弦公式"""
    rad = math.pi / 180.0
    dlat = (lat2 - lat1) * rad
    dlng = (lng2 - lng1) * rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1 * rad) * math.cos(lat2 * rad) * math.sin(dlng / 2) ** 2
    return 6371000 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# ==================== Tools ====================

@mcp.tool()
def search_campus_pois(keyword: str) -> str:
    """按关键词搜索校园设施（搜索名称、分类、描述、标签）。返回匹配的设施列表。

    Args:
        keyword: 搜索关键词，例如 "菜鸟"、"图书馆"、"食堂"、"打印"
    """
    kw = keyword.strip().lower()
    if not kw:
        return json.dumps({"error": "请提供搜索关键词"}, ensure_ascii=False)

    results = []
    for p in CAMPUS_POIS:
        if (kw in p["name"].lower() or
            kw in p["category"].lower() or
            kw in p["desc"].lower() or
            any(kw in t.lower() for t in p.get("tags", []))):
            results.append({
                "name": p["name"],
                "category": p["category"],
                "lng": p["lng"],
                "lat": p["lat"],
                "desc": p["desc"],
                "tags": p.get("tags", [])
            })

    return json.dumps({
        "count": len(results),
        "keyword": keyword,
        "results": results
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def get_poi_detail(name: str) -> str:
    """获取指定设施的完整信息（坐标、描述、标签）。

    Args:
        name: 设施名称，例如 "双塔楼"、"23栋菜鸟驿站"、"1食堂"
    """
    poi = _find_poi(name)
    if not poi:
        return json.dumps({
            "error": f"未找到设施: {name}",
            "suggestions": [p["name"] for p in CAMPUS_POIS if name in p["name"] or p["name"] in name][:5]
        }, ensure_ascii=False, indent=2)

    return json.dumps(poi, ensure_ascii=False, indent=2)


@mcp.tool()
def list_categories() -> str:
    """列出校园所有设施分类及每类的设施数量。"""
    result = []
    for cat in CATEGORIES:
        items = [p for p in CAMPUS_POIS if p["category"] == cat["key"]]
        result.append({
            "category": cat["key"],
            "icon": cat["icon"],
            "count": len(items),
            "items": [p["name"] for p in items]
        })
    return json.dumps({"total_categories": len(CATEGORIES), "categories": result}, ensure_ascii=False, indent=2)


@mcp.tool()
def get_category_pois(category: str) -> str:
    """获取指定分类下的所有设施。

    Args:
        category: 分类名称，可选: 驿站、图书馆、教学楼、食堂、打印店、医院
    """
    valid_categories = [c["key"] for c in CATEGORIES]
    if category not in valid_categories:
        return json.dumps({
            "error": f"无效分类: {category}",
            "valid_categories": valid_categories
        }, ensure_ascii=False, indent=2)

    items = [p for p in CAMPUS_POIS if p["category"] == category]
    cat_info = next(c for c in CATEGORIES if c["key"] == category)

    return json.dumps({
        "category": category,
        "icon": cat_info["icon"],
        "color": cat_info["color"],
        "count": len(items),
        "items": items
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def get_navigation_url(poi_name: str, user_lng: float = 0.0, user_lat: float = 0.0) -> str:
    """生成高德地图步行导航链接。

    Args:
        poi_name: 目标设施名称
        user_lng: 用户当前经度（可选，不传则只导航到目标点）
        user_lat: 用户当前纬度（可选，不传则只导航到目标点）
    """
    poi = _find_poi(poi_name)
    if not poi:
        return json.dumps({"error": f"未找到设施: {poi_name}"}, ensure_ascii=False)

    if user_lng and user_lat:
        url = (f"{AMAP_NAV_BASE}?from={user_lng},{user_lat},我的位置"
               f"&to={poi['lng']},{poi['lat']},{poi['name']}&mode=walk&coordinate=gaode")
    else:
        url = (f"{AMAP_NAV_BASE}?to={poi['lng']},{poi['lat']},{poi['name']}"
               f"&mode=walk&coordinate=gaode")

    return json.dumps({
        "poi": poi["name"],
        "destination": f"{poi['lng']}, {poi['lat']}",
        "navigation_url": url,
        "mode": "步行导航",
        "tip": "在浏览器中打开链接即可启动高德地图导航"
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def get_campus_boundary() -> str:
    """获取中南民族大学校园轮廓坐标点列表。"""
    return json.dumps({
        "description": "中南民族大学校园边界轮廓",
        "point_count": len(CAMPUS_OUTLINE),
        "coordinate_system": "GCJ-02 (高德坐标系)",
        "outline": [{"lng": p[0], "lat": p[1]} for p in CAMPUS_OUTLINE]
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def get_nearest_poi(lng: float, lat: float, category: str = "") -> str:
    """查找离指定坐标最近的校园设施。

    Args:
        lng: 经度
        lat: 纬度
        category: 可选，限定分类（驿站/图书馆/教学楼/食堂/打印店/医院），不传则搜索全部
    """
    pool = CAMPUS_POIS
    if category:
        valid_categories = [c["key"] for c in CATEGORIES]
        if category not in valid_categories:
            return json.dumps({
                "error": f"无效分类: {category}",
                "valid_categories": valid_categories
            }, ensure_ascii=False, indent=2)
        pool = [p for p in CAMPUS_POIS if p["category"] == category]

    if not pool:
        return json.dumps({"error": "没有可匹配的设施"}, ensure_ascii=False)

    best = min(pool, key=lambda p: _calc_distance(lng, lat, p["lng"], p["lat"]))
    dist = _calc_distance(lng, lat, best["lng"], best["lat"])

    # 返回 TOP 5
    sorted_pois = sorted(pool, key=lambda p: _calc_distance(lng, lat, p["lng"], p["lat"]))

    return json.dumps({
        "query": {"lng": lng, "lat": lat, "category": category or "全部"},
        "nearest": {
            "name": best["name"],
            "category": best["category"],
            "lng": best["lng"],
            "lat": best["lat"],
            "distance_meters": round(dist, 1),
            "desc": best["desc"]
        },
        "top5": [{
            "name": p["name"],
            "category": p["category"],
            "distance_meters": round(_calc_distance(lng, lat, p["lng"], p["lat"]), 1)
        } for p in sorted_pois[:5]]
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def open_campus_map(poi_name: str = "") -> str:
    """打开校园地图页面，可选跳转到指定设施。

    Args:
        poi_name: 设施名称（可选），例如 "双塔楼"、"1食堂"。不传则打开地图首页
    """
    url = MAP_BASE_URL
    if poi_name:
        import urllib.parse
        encoded = urllib.parse.quote(poi_name)
        url = f"{MAP_BASE_URL}/?poi={encoded}"

    return json.dumps({
        "url": url,
        "tip": "在浏览器中打开此链接查看校园地图",
        "poi": poi_name or "地图首页"
    }, ensure_ascii=False, indent=2)


# ==================== Resources ====================

@mcp.resource("campus://pois")
def get_pois_resource() -> str:
    """获取所有校园 POI 数据"""
    return json.dumps({
        "total": len(CAMPUS_POIS),
        "description": "中南民族大学校园设施完整数据",
        "pois": CAMPUS_POIS
    }, ensure_ascii=False, indent=2)


@mcp.resource("campus://categories")
def get_categories_resource() -> str:
    """获取所有分类定义"""
    result = []
    for cat in CATEGORIES:
        items = [p for p in CAMPUS_POIS if p["category"] == cat["key"]]
        result.append({
            "key": cat["key"],
            "color": cat["color"],
            "icon": cat["icon"],
            "count": len(items),
            "names": [p["name"] for p in items]
        })
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.resource("campus://outline")
def get_outline_resource() -> str:
    """获取校园边界坐标"""
    return json.dumps({
        "description": "中南民族大学校园轮廓",
        "coordinate_system": "GCJ-02",
        "points": [{"lng": p[0], "lat": p[1]} for p in CAMPUS_OUTLINE]
    }, ensure_ascii=False, indent=2)


# ===== 入口 =====
def main():
    import sys
    if "--sse" in sys.argv:
        mcp.run(transport="sse")
    else:
        mcp.run()

if __name__ == "__main__":
    main()
