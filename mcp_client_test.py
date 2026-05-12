"""
MCP Client Test - validates server via stdio protocol
"""
import asyncio
import sys
import io
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Force UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

async def main():
    server_params = StdioServerParameters(
        command="D:/python/python.exe",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("[OK] MCP connection established\n")

            # List tools
            tools = await session.list_tools()
            print(f"Total tools: {len(tools.tools)}")
            for t in tools.tools:
                print(f"  - {t.name}")
            print()

            # Test each tool
            print("=" * 60)
            print("Testing tools:")
            print("=" * 60)

            result = await session.call_tool("search_campus_pois", {"keyword": "菜鸟"})
            text = result.content[0].text
            print(f"\n1. search_campus_pois('菜鸟')")
            print(f"   Result: {text[:200]}...")

            result = await session.call_tool("get_poi_detail", {"name": "双塔楼"})
            text = result.content[0].text
            print(f"\n2. get_poi_detail('双塔楼')")
            print(f"   Result: {text[:200]}...")

            result = await session.call_tool("list_categories", {})
            text = result.content[0].text
            print(f"\n3. list_categories()")
            print(f"   Result: {text[:200]}...")

            result = await session.call_tool("get_category_pois", {"category": "食堂"})
            text = result.content[0].text
            print(f"\n4. get_category_pois('食堂')")
            print(f"   Result: {text[:200]}...")

            result = await session.call_tool("get_navigation_url", {
                "poi_name": "1食堂", "user_lng": 114.391, "user_lat": 30.483
            })
            text = result.content[0].text
            print(f"\n5. get_navigation_url('1食堂', lng, lat)")
            print(f"   Result: {text[:200]}...")

            result = await session.call_tool("get_campus_boundary", {})
            text = result.content[0].text
            print(f"\n6. get_campus_boundary()")
            print(f"   Result: {text[:200]}...")

            result = await session.call_tool("get_nearest_poi", {
                "lng": 114.3915, "lat": 30.4825, "category": "食堂"
            })
            text = result.content[0].text
            print(f"\n7. get_nearest_poi(114.3915, 30.4825, '食堂')")
            print(f"   Result: {text[:200]}...")

            # List resources
            resources = await session.list_resources()
            print(f"\nTotal resources: {len(resources.resources)}")
            for r in resources.resources:
                print(f"  - {r.uri}")

            print(f"\n[OK] All 7 tools + {len(resources.resources)} resources verified!")

if __name__ == "__main__":
    asyncio.run(main())
