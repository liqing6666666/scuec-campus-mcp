// ===== 中南民族大学 POI 数据（来源: address.xlsx） =====
const campusPOIs = [
    // ---- 驿站 ----
    { name: "23栋菜鸟驿站", category: "驿站", lng: 114.392303, lat: 30.479495,
      desc: "湖北省武汉市洪山区民族大道182号中南民族大学23栋菜鸟驿站", tags: ["快递", "菜鸟"] },
    { name: "25栋菜鸟驿站", category: "驿站", lng: 114.393244, lat: 30.479531,
      desc: "湖北省武汉市洪山区民族大道182号中南民族大学25栋菜鸟驿站", tags: ["快递", "菜鸟"] },
    { name: "北区菜鸟驿站", category: "驿站", lng: 114.395414, lat: 30.493787,
      desc: "湖北省武汉市洪山区民族大道182号中南民族大学北区学生公寓", tags: ["快递", "菜鸟"] },

    // ---- 图书馆 ----
    { name: "南区分馆", category: "图书馆", lng: 114.392468, lat: 30.48102,
      desc: "图书馆南区分馆", tags: ["自习", "借书"] },
    { name: "南书院", category: "图书馆", lng: 114.392078, lat: 30.486579,
      desc: "南书院自习区", tags: ["自习"] },
    { name: "双塔楼", category: "图书馆", lng: 114.391608, lat: 30.487281,
      desc: "双塔楼图书馆", tags: ["自习", "借书"] },
    { name: "老馆", category: "图书馆", lng: 114.392534, lat: 30.487233,
      desc: "老图书馆", tags: ["自习", "借书"] },
    { name: "北书院", category: "图书馆", lng: 114.392072, lat: 30.487857,
      desc: "北书院自习区", tags: ["自习"] },
    { name: "北区分馆-3A", category: "图书馆", lng: 114.395321, lat: 30.495252,
      desc: "北区分馆3A自习区", tags: ["自习"] },
    { name: "北区分馆-鲲鹏书院", category: "图书馆", lng: 114.396933, lat: 30.495173,
      desc: "鲲鹏书院自习区", tags: ["自习"] },

    // ---- 教学楼 ----
    { name: "1号教学楼", category: "教学楼", lng: 114.393552, lat: 30.488275,
      desc: "教学楼", tags: ["教室"] },
    { name: "2号教学楼", category: "教学楼", lng: 114.39264, lat: 30.488261,
      desc: "教学楼", tags: ["教室"] },
    { name: "4号教学楼", category: "教学楼", lng: 114.394778, lat: 30.486846,
      desc: "教学楼", tags: ["教室"] },
    { name: "7号教学楼", category: "教学楼", lng: 114.393842, lat: 30.484338,
      desc: "教学楼", tags: ["教室"] },
    { name: "9号教学楼", category: "教学楼", lng: 114.390118, lat: 30.489614,
      desc: "教学楼", tags: ["教室"] },
    { name: "10号教学楼", category: "教学楼", lng: 114.392632, lat: 30.490622,
      desc: "教学楼", tags: ["教室"] },
    { name: "11号教学楼", category: "教学楼", lng: 114.390722, lat: 30.490246,
      desc: "教学楼", tags: ["教室"] },
    { name: "13号教学楼", category: "教学楼", lng: 114.390386, lat: 30.491092,
      desc: "教学楼", tags: ["教室"] },
    { name: "14号教学楼", category: "教学楼", lng: 114.395122, lat: 30.49037,
      desc: "教学楼", tags: ["教室"] },
    { name: "15号教学楼", category: "教学楼", lng: 114.392019, lat: 30.491828,
      desc: "教学楼", tags: ["教室"] },
    { name: "16号教学楼", category: "教学楼", lng: 114.395866, lat: 30.492735,
      desc: "教学楼", tags: ["教室"] },
    { name: "17号教学楼", category: "教学楼", lng: 114.394956, lat: 30.488739,
      desc: "教学楼", tags: ["教室"] },
    { name: "光谷音乐厅", category: "教学楼", lng: 114.395284, lat: 30.490433,
      desc: "中南民族大学光谷音乐厅", tags: ["演出", "活动"] },
    { name: "光谷美术馆", category: "教学楼", lng: 114.395378, lat: 30.491326,
      desc: "中南民族大学光谷美术馆", tags: ["展览"] },
    { name: "学术会堂", category: "教学楼", lng: 114.391077, lat: 30.489721,
      desc: "学术会堂", tags: ["会议", "讲座"] },
    { name: "大学生活动中心", category: "教学楼", lng: 114.393173, lat: 30.483003,
      desc: "大学生活动中心", tags: ["活动", "社团"] },
    { name: "大礼堂", category: "教学楼", lng: 114.394871, lat: 30.489689,
      desc: "大礼堂", tags: ["演出", "典礼"] },
    { name: "体育馆", category: "教学楼", lng: 114.394006, lat: 30.483417,
      desc: "体育馆", tags: ["运动", "篮球"] },
    { name: "行政楼", category: "教学楼", lng: 114.394735, lat: 30.487642,
      desc: "行政楼", tags: ["办公"] },
    { name: "国际合作与交流处", category: "教学楼", lng: 114.389332, lat: 30.480873,
      desc: "国际合作与交流处", tags: ["留学", "交流"] },
    { name: "学术交流中心", category: "教学楼", lng: 114.392574, lat: 30.48724,
      desc: "学术交流中心", tags: ["会议"] },
    { name: "国际学术会议中心", category: "教学楼", lng: 114.388794, lat: 30.481729,
      desc: "国际学术会议中心", tags: ["会议"] },
    { name: "民族学博物馆", category: "教学楼", lng: 114.38954, lat: 30.482684,
      desc: "民族学博物馆", tags: ["展览", "参观"] },
    { name: "体育训练中心", category: "教学楼", lng: 114.394823, lat: 30.488747,
      desc: "体育训练中心", tags: ["运动"] },
    { name: "游泳馆", category: "教学楼", lng: 114.393818, lat: 30.480472,
      desc: "游泳馆", tags: ["游泳"] },

    // ---- 食堂 ----
    { name: "1食堂", category: "食堂", lng: 114.391489, lat: 30.482543,
      desc: "1食堂", tags: ["餐饮"] },
    { name: "2食堂", category: "食堂", lng: 114.391517, lat: 30.481763,
      desc: "2食堂", tags: ["餐饮"] },
    { name: "3食堂", category: "食堂", lng: 114.391485, lat: 30.480584,
      desc: "3食堂", tags: ["餐饮"] },
    { name: "4食堂", category: "食堂", lng: 114.392245, lat: 30.481202,
      desc: "4食堂", tags: ["餐饮"] },
    { name: "南湖园餐厅", category: "食堂", lng: 114.394741, lat: 30.484292,
      desc: "南湖园餐厅", tags: ["餐饮"] },
    { name: "中心食堂", category: "食堂", lng: 114.394355, lat: 30.490416,
      desc: "中心食堂", tags: ["餐饮"] },
    { name: "北区食堂", category: "食堂", lng: 114.395947, lat: 30.494742,
      desc: "北区食堂", tags: ["餐饮"] },
    { name: "小吃街", category: "食堂", lng: 114.391111, lat: 30.482122,
      desc: "小吃街", tags: ["小吃", "夜宵"] },

    // ---- 打印店 ----
    { name: "21栋打印店", category: "打印店", lng: 114.391163, lat: 30.479922,
      desc: "21栋打印店", tags: ["打印", "复印"] },
    { name: "民大读书坊打印", category: "打印店", lng: 114.391328, lat: 30.482091,
      desc: "民大读书坊打印", tags: ["打印", "复印"] },
    { name: "大购打印", category: "打印店", lng: 114.391338, lat: 30.482726,
      desc: "大购打印", tags: ["打印", "复印"] },
    { name: "图书馆打印", category: "打印店", lng: 114.392194, lat: 30.486725,
      desc: "图书馆打印", tags: ["打印", "复印"] },
    { name: "樱果打印", category: "打印店", lng: 114.395198, lat: 30.491867,
      desc: "樱果打印", tags: ["打印", "复印"] },

    // ---- 医院 ----
    { name: "校医院", category: "医院", lng: 114.396986, lat: 30.487635,
      desc: "校医院", tags: ["看病", "急诊"] },
    { name: "南区药店", category: "医院", lng: 114.391331, lat: 30.482669,
      desc: "南区药店", tags: ["买药"] },
    { name: "北区药店", category: "医院", lng: 114.396053, lat: 30.49486,
      desc: "北区药店", tags: ["买药"] },
];

// ===== 校园轮廓坐标（来源: address.xlsx，逆时针环绕） =====
const campusOutline = [
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
];

// 6个分类及颜色
const categories = [
    { key: "驿站", color: "#fa8c16", icon: "📦" },
    { key: "图书馆", color: "#722ed1", icon: "📚" },
    { key: "教学楼", color: "#1890ff", icon: "🏫" },
    { key: "食堂", color: "#eb2f96", icon: "🍜" },
    { key: "打印店", color: "#13c2c2", icon: "🖨" },
    { key: "医院", color: "#f5222d", icon: "🏥" },
];

// ===== 工具函数 =====
function getCatColor(cat) {
    const found = categories.find(c => c.key === cat);
    return found ? found.color : '#1890ff';
}

function showInfoPanel(poi) {
    window._currentPOI = poi;
    document.getElementById('infoTitle').textContent = poi.name;
    document.getElementById('infoCat').textContent = poi.category;
    document.getElementById('infoDesc').textContent = poi.desc;
    const tagsHtml = (poi.tags || []).map(t => `<span class="info-tag">${t}</span>`).join('');
    document.getElementById('infoTags').innerHTML = tagsHtml;
    document.getElementById('infoPanel').style.display = 'block';
    if (window._map) {
        window._map.setCenter([poi.lng, poi.lat]);
        if (window._map.getZoom() < 17) window._map.setZoom(17);
    }
}

function closeInfoPanel() {
    document.getElementById('infoPanel').style.display = 'none';
    window._currentPOI = null;
    if (window._allMarkers && window._map) {
        window._allMarkers.forEach(m => window._map.remove(m));
        window._allMarkers = [];
    }
}

function startNav() {
    const poi = window._currentPOI;
    if (!poi) return;
    const from = window._userLocation;
    let url;
    if (from) {
        url = `https://uri.amap.com/navigation?from=${from.lng},${from.lat},我的位置&to=${poi.lng},${poi.lat},${poi.name}&mode=walk&coordinate=gaode`;
    } else {
        url = `https://uri.amap.com/navigation?to=${poi.lng},${poi.lat},${poi.name}&mode=walk&coordinate=gaode`;
    }
    window.open(url, '_blank');
}

// ===== 定位功能 =====
let manualLocateMode = false;

function locateMe() {
    if (!window._map) return;
    window._map.plugin('AMap.Geolocation', () => {
        const geolocation = new AMap.Geolocation({
            enableHighAccuracy: true,
            timeout: 10000,
            zoomToAccuracy: true,
            showButton: false
        });
        geolocation.getCurrentPosition((status, result) => {
            if (status === 'complete') {
                const lng = result.position.getLng();
                const lat = result.position.getLat();
                window._userLocation = { lng, lat };
                showUserMarker(lng, lat);
                window._map.setCenter([lng, lat]);
                window._map.setZoom(17);
            } else {
                // GPS 失败，提示手动设置
                if (confirm('自动定位失败或不准，是否手动在地图上点击设置位置？')) {
                    startManualLocate();
                }
            }
        });
    });
}

function startManualLocate() {
    if (manualLocateMode) {
        endManualLocate();
        return;
    }
    manualLocateMode = true;
    const btn = document.getElementById('locateManual');
    btn.classList.add('active');
    btn.textContent = '点击地图设置位置（再点取消）';
}

function endManualLocate() {
    manualLocateMode = false;
    const btn = document.getElementById('locateManual');
    btn.classList.remove('active');
    btn.textContent = '📌 手动设置位置';
}

function showUserMarker(lng, lat) {
    if (window._userMarker) window._map.remove(window._userMarker);
    window._userMarker = new AMap.Marker({
        position: [lng, lat],
        content: `<div class="user-marker">
            <div class="user-dot"></div>
            <div class="user-pulse"></div>
        </div>`,
        offset: new AMap.Pixel(0, 0)
    });
    window._userMarker.setMap(window._map);
}

function locateUniversity() {
    if (!window._map) return;
    window._map.setCenter([114.3928, 30.486]);
    window._map.setZoom(16);
}

// ===== 侧边栏渲染 =====
function renderSidebar() {
    const sidebar = document.getElementById('sidebarList');
    let html = '';

    categories.forEach(cat => {
        const items = campusPOIs.filter(p => p.category === cat.key);
        html += `
        <div class="cat-group" id="group-${cat.key}">
            <div class="cat-header" onclick="toggleCategory('${cat.key}')">
                <div class="cat-header-left">
                    <span class="cat-icon" style="background:${cat.color}">${cat.icon}</span>
                    <span class="cat-name">${cat.key}</span>
                </div>
                <span class="cat-badge">${items.length}</span>
                <span class="cat-arrow" id="arrow-${cat.key}">▸</span>
            </div>
            <div class="cat-body" id="body-${cat.key}" style="display:none">
                <div class="cat-show-all" onclick="event.stopPropagation();showCategoryAll('${cat.key}')">
                    全部显示
                </div>`;
        items.forEach(poi => {
            html += `<div class="cat-item" onclick="event.stopPropagation();locatePOI('${poi.name}')">${poi.name}</div>`;
        });
        html += `</div></div>`;
    });

    sidebar.innerHTML = html;
}

function toggleCategory(key) {
    const body = document.getElementById('body-' + key);
    const arrow = document.getElementById('arrow-' + key);
    if (body.style.display === 'none') {
        body.style.display = 'block';
        arrow.textContent = '▾';
    } else {
        body.style.display = 'none';
        arrow.textContent = '▸';
    }
}

function locatePOI(name) {
    const poi = campusPOIs.find(p => p.name === name);
    if (!poi) return;
    // 只显示这一个设施的标记
    if (window._addMarkers) window._addMarkers([poi]);
    showInfoPanel(poi);
}

function showCategoryAll(catKey) {
    const items = campusPOIs.filter(p => p.category === catKey);
    if (window._addMarkers) window._addMarkers(items);
    // 关闭信息面板但不清除标记
    document.getElementById('infoPanel').style.display = 'none';
    window._currentPOI = null;
    if (items.length > 0 && window._map) {
        const bounds = new AMap.Bounds(
            [Math.min(...items.map(p => p.lng)), Math.min(...items.map(p => p.lat))],
            [Math.max(...items.map(p => p.lng)), Math.max(...items.map(p => p.lat))]
        );
        window._map.setBounds(bounds, false, [60, 60, 60, 60]);
    }
}

// ===== 搜索 =====
function filterPOIs() {
    const keyword = document.getElementById('searchInput').value.trim().toLowerCase();
    if (!keyword) {
        if (window._allMarkers && window._map) {
            window._allMarkers.forEach(m => window._map.remove(m));
            window._allMarkers = [];
        }
        return;
    }
    if (!window._map) return;
    const filtered = campusPOIs.filter(p =>
        p.name.toLowerCase().includes(keyword) ||
        p.desc.toLowerCase().includes(keyword) ||
        p.category.toLowerCase().includes(keyword) ||
        (p.tags || []).some(t => t.includes(keyword))
    );
    if (window._addMarkers) window._addMarkers(filtered);
}

// ===== 坐标拾取工具 =====
let pickMode = false;
let pickMarker = null;

function togglePickMode() {
    pickMode = !pickMode;
    if (pickMode && manualLocateMode) endManualLocate();
    const btn = document.getElementById('pickToggle');
    btn.classList.toggle('active', pickMode);
    btn.textContent = pickMode ? '拾取中...点击地图取坐标' : '坐标拾取模式';
    if (!pickMode) {
        document.getElementById('coordPopup').style.display = 'none';
        if (pickMarker && window._map) { window._map.remove(pickMarker); pickMarker = null; }
    }
}

function showCoordPopup(lng, lat, x, y) {
    const popup = document.getElementById('coordPopup');
    popup.innerHTML = `
        <div>经度: <span class="coord-val" onclick="copyCoord('${lng},${lat}')">${lng.toFixed(6)}</span></div>
        <div>纬度: <span class="coord-val" onclick="copyCoord('${lng},${lat}')">${lat.toFixed(6)}</span></div>
        <div class="coord-tip">点击数字复制 lng, lat 格式</div>
    `;
    popup.style.display = 'block';
    const container = document.getElementById('container');
    const rect = container.getBoundingClientRect();
    popup.style.left = Math.min(x - rect.left + 15, rect.width - 240) + 'px';
    popup.style.top = (y - rect.top - 60) + 'px';
}

function copyCoord(text) {
    const popup = document.getElementById('coordPopup');
    const tip = popup.querySelector('.coord-tip');
    const showCopied = () => {
        tip.textContent = '已复制: ' + text;
        tip.style.color = '#52c41a';
        setTimeout(() => { tip.style.color = '#999'; tip.textContent = '点击数字复制 lng, lat 格式'; }, 1500);
    };

    // 方式1: clipboard API (需 HTTPS)
    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
        navigator.clipboard.writeText(text).then(showCopied).catch(() => {
            fallbackCopy(text, showCopied);
        });
    } else {
        fallbackCopy(text, showCopied);
    }
}

function fallbackCopy(text, cb) {
    // 方式2: textarea + execCommand (兼容 HTTP)
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;left:-9999px;top:0';
    document.body.appendChild(ta);
    ta.focus();
    ta.setSelectionRange(0, ta.value.length);

    let ok = false;
    try { ok = document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);

    if (ok) { cb(); return; }

    // 方式3: 兜底 — 弹出可复制文本
    prompt('复制以下坐标 (Ctrl+C):', text);
}

function exportCoords() {
    const lines = campusPOIs.map(p =>
        `"${p.name}", lng: ${p.lng}, lat: ${p.lat}`
    ).join('\n');
    console.log('===== 所有设施坐标 =====\n' + lines);
    alert('坐标已输出到浏览器控制台（F12 → Console），请查看并复制。');
}

// ===== 地图加载回调 =====
function onAMapLoaded() {
    // 计算中心点
    const allLng = campusPOIs.map(p => p.lng);
    const allLat = campusPOIs.map(p => p.lat);
    const centerLng = (Math.min(...allLng) + Math.max(...allLng)) / 2;
    const centerLat = (Math.min(...allLat) + Math.max(...allLat)) / 2;

    const map = new AMap.Map('container', {
        zoom: 16,
        center: [centerLng, centerLat],
        mapStyle: 'amap://styles/normal'
    });

    map.plugin(['AMap.ToolBar', 'AMap.Scale'], () => {
        map.addControl(new AMap.ToolBar({ position: 'RB' }));
        map.addControl(new AMap.Scale());
    });

    window._map = map;

    // 校园轮廓
    const campusPolygon = new AMap.Polygon({
        path: campusOutline,
        fillColor: '#e6f7ff',
        fillOpacity: 0.12,
        strokeColor: '#1890ff',
        strokeWeight: 2,
        strokeStyle: 'dashed',
        bubble: true
    });
    map.add(campusPolygon);

    // 地图点击拾取坐标 / 手动设置位置
    map.on('click', function (e) {
        // 如果点击的是坐标弹窗内的元素，忽略
        if (e.originEvent && e.originEvent.target &&
            e.originEvent.target.closest && e.originEvent.target.closest('.coord-popup')) {
            return;
        }
        const lng = e.lnglat.getLng();
        const lat = e.lnglat.getLat();

        // 手动设置位置模式
        if (manualLocateMode) {
            window._userLocation = { lng, lat };
            showUserMarker(lng, lat);
            endManualLocate();
            return;
        }

        if (!pickMode) return;
        if (pickMarker) map.remove(pickMarker);
        pickMarker = new AMap.Marker({
            position: [lng, lat],
            content: '<div style="background:#f5222d;width:16px;height:16px;border-radius:50%;border:3px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,0.3);transform:translate(-50%,-50%)"></div>',
            offset: new AMap.Pixel(0, 0)
        });
        map.add(pickMarker);
        showCoordPopup(lng, lat, e.originEvent.clientX, e.originEvent.clientY);
    });

    // 标记管理
    window._allMarkers = [];
    window._currentPOI = null;

    window._addMarkers = function (pois) {
        window._allMarkers.forEach(m => map.remove(m));
        window._allMarkers = [];
        // 保留用户位置标记
        if (window._userMarker) window._userMarker.setMap(map);
        pois.forEach(poi => {
            const color = getCatColor(poi.category);
            const marker = new AMap.Marker({
                position: [poi.lng, poi.lat],
                content: `<div class="marker-bubble" style="border-color:${color};color:${color}">${poi.name}<div class="marker-arrow" style="border-top-color:#fff"></div></div>`,
                offset: new AMap.Pixel(0, -20),
                title: poi.name
            });
            marker.on('click', () => showInfoPanel(poi));
            marker.setMap(map);
            window._allMarkers.push(marker);
        });
    };

    // 渲染侧边栏
    renderSidebar();

    // URL 参数跳转
    const params = new URLSearchParams(window.location.search);
    const targetPOI = params.get('poi');

    // 优先定位用户位置
    setTimeout(() => locateMe(), 500);

    if (targetPOI) {
        const name = decodeURIComponent(targetPOI);
        const found = campusPOIs.find(p => p.name === name);
        if (found) setTimeout(() => {
            window._addMarkers([found]);
            showInfoPanel(found);
        }, 1200);
    }
}

if (typeof AMap !== 'undefined') onAMapLoaded();
