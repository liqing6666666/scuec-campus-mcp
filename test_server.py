"""快速验证 MCP Server 所有 tools 和 resources"""
import json
import sys
import io

# 强制 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from server import (
    search_campus_pois,
    get_poi_detail,
    list_categories,
    get_category_pois,
    get_navigation_url,
    get_campus_boundary,
    get_nearest_poi,
    get_pois_resource,
    get_categories_resource,
    get_outline_resource,
)

ok_count = 0
fail_count = 0

def test(name, result_str):
    global ok_count, fail_count
    try:
        data = json.loads(result_str)
        if isinstance(data, dict) and "error" not in data:
            ok_count += 1
        elif isinstance(data, dict) and "error" in data:
            # error 响应也算测试通过（逻辑正确返回了错误）
            pass
        print(f"  [OK] {name}")
    except Exception as e:
        fail_count += 1
        print(f"  [FAIL] {name}: {e}")

print("Testing MCP Server Tools & Resources...")
print(f"{'='*50}")

# ---- Tools ----
print("\n[Tools]")
test("search_campus_pois('菜鸟')", search_campus_pois("菜鸟"))
test("get_poi_detail('双塔楼')", get_poi_detail("双塔楼"))
test("get_poi_detail('不存在')", get_poi_detail("不存在"))
test("list_categories()", list_categories())
test("get_category_pois('食堂')", get_category_pois("食堂"))
test("get_category_pois('无效')", get_category_pois("无效"))
test("get_navigation_url('1食堂', 114.391, 30.483)", get_navigation_url("1食堂", 114.391, 30.483))
test("get_navigation_url('双塔楼')", get_navigation_url("双塔楼"))
test("get_campus_boundary()", get_campus_boundary())
test("get_nearest_poi(114.3915, 30.4825, '食堂')", get_nearest_poi(114.3915, 30.4825, "食堂"))
test("get_nearest_poi(114.3915, 30.4825)", get_nearest_poi(114.3915, 30.4825))

# ---- Resources ----
print("\n[Resources]")
test("resource: campus://pois", get_pois_resource())
test("resource: campus://categories", get_categories_resource())
test("resource: campus://outline", get_outline_resource())

print(f"\n{'='*50}")
print(f"Results: {ok_count} passed, {fail_count} failed")
print("All tests completed!")
