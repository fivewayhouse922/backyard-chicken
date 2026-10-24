# 5wayhouse-hualien-youth
## 「雞鳴豐田」兒少農牧培力方案——從雞舍到社區食農的教育協力行動

本儲存庫為 **2026 花蓮縣青年夢想家計畫** 獲獎/提案專案之完整數位檔案庫與後續協同開發專案網頁之代碼倉庫。

🌐 **成果展官方網頁**：[https://chinkunlim.github.io/5wayhouse-hualien-youth/](https://chinkunlim.github.io/5wayhouse-hualien-youth/)

---

## 專案基本資訊

- **成果展官方網頁**：[https://chinkunlim.github.io/5wayhouse-hualien-youth/](https://chinkunlim.github.io/5wayhouse-hualien-youth/)
- **計畫名稱**：「雞鳴豐田」兒少農牧培力方案——從雞舍到社區食農的教育協力行動
- **參賽類別**：2026 花蓮青年夢想家計畫提案競賽（自選議題組—公私立大專院校組）
- **執行團隊**：聞雞起舞
- **合作單位**：豐田五味屋（社團法人花蓮縣鄉村社區大學發展協會 / 農學願小菜園）
- **申請代表人**：林錦坤（國立東華大學 諮商與臨床心理學系）
- **指導老師**：顧瑜君 教授（國立東華大學特聘教授）
- **指導業師**：李宏韡 獸醫師（國立東華大學兼任講師）
- **專業協力**：黎明方舟牧場

---

## 成果影片

專案成果記錄影片（雞舍建置與兒少培力實況）：
- 📺 **YouTube 成果影片**：[點此觀看 YouTube 影片](https://youtu.be/XY_cvZ4_GZw)

> **說明**：為符合 GitHub 單一檔案上限（100MB）並提升載入效能，原始 247MB 高畫質 `.mov` 影音檔案不直接存放於 Git 倉庫，後續網頁展示將採用 YouTube 嵌入式播放器呈現。

---

## 目錄結構與導覽

本儲存庫已精簡為成果展官方網頁之核心程式碼與前端資源：

```text
.
├── index.html             # 成果展官方故事型一頁式展示網頁（相容 GitHub Pages）
├── scripts/               # 自動化工具腳本庫
│   └── sync_egg_data.py   # 產蛋大數據自動統計與同步工具
├── web_assets/            # 網頁專屬前端資源庫
│   ├── data/              # 結構化設定與數據檔
│   │   ├── coop_specs.json       # 雞舍動福硬體規格設定
│   │   ├── egg_records.csv       # 收蛋原始歷史明細數據
│   │   ├── egg_stats.json        # 產蛋統計指標與雲端同步設定
│   │   └── gallery_config.json   # 現場相簿圖說與燈箱設定
│   └── images/            # 網頁精選圖片與視覺素材
│       ├── about/         # 專案緣起照片
│       ├── chickens/      # 10 隻雞老師專屬特寫照片
│       ├── coop-building/ # 雞舍搭建與動福指導照片
│       ├── data/          # 系統操作介面截圖
│       ├── gallery/       # 現場精選活動照片（12 張）
│       ├── mindmap/       # 兒少手繪心智圖照片
│       ├── specs/         # 動福工法特寫照片
│       ├── egg_carton_realistic.png # 擬真蛋盒主視覺
│       ├── logo.png       # 五味屋官方視覺標誌
│       └── logo_icon.webp # 網頁 Favicon 圖示
└── README.md              # 專案說明文件
```

---

## 成果展專案網頁 (GitHub Pages)

本倉庫根目錄已建構專為成果展設計的現代化響應式單頁網站 [index.html](file:///Users/slone/Documents/Chicken%20Project/index.html)。

🔗 **線上訪問網址**：[https://chinkunlim.github.io/5wayhouse-hualien-youth/](https://chinkunlim.github.io/5wayhouse-hualien-youth/)

### 網頁特色功能
- 🌟 **四大教育維度**：科學體感（FCR料蛋比/氣象監測）、責任承諾（五大自由/非水洗）、地方歷史（耆老訪談）、社區客廳（青銀共學）。
- 🐔 **10 隻雞老師專屬檔案圖鑑**：完整收錄兒少命名之伊莎蛋雞個別特寫照與個性特徵。
- 📊 **智慧養雞與產蛋大數據儀表板**：展示真實累計 182 顆收蛋歷程、58.4g 平均蛋重、GAS 手機登錄操作實況。
- 🎬 **YouTube 成果影音嵌入**：無縫串接高畫質成果短片，極速載入且不佔倉庫空間。
- 🖼️ **GLightbox 12 張精選高解析相簿**：支援手機雙指捏合縮放、滑動檢視大圖。
- 🐣 **成果展攤位小測驗 (Quiz) 闖關升級**：現場掃碼闖關，答對自動生成專屬防偽兌換序號（如 `#5WAY-XXXX`），活化攤位人流！

### 本地即時預覽
直接於瀏覽器中開啟 [index.html](file:///Users/slone/Documents/Chicken%20Project/index.html)，或於終端機執行輕量本機伺服器：
```bash
python3 -m http.server 8000
```
瀏覽器訪問 `http://localhost:8000`。

### GitHub Pages 啟用與永久網址
1. 前往 GitHub 倉庫 `Settings` ➔ 點選左側 `Pages`。
2. **Build and deployment** ➔ **Source** 選擇 `Deploy from a branch`。
3. **Branch** 選擇 `main`，資料夾選擇 `/ (root)`，點擊 `Save`。
4. **GitHub Pages visibility** 設為 `Public`（Student Pack 支援私有代碼搭配公開網頁）。
5. 永久網址固定為：`https://chinkunlim.github.io/5wayhouse-hualien-youth/`（每次 push 網址**絕不變動**，自動完成最新部署）。

---

## 協同合作指引

### 協作步驟
1. **Clone 倉庫**：
   ```bash
   git clone https://github.com/chinkunlim/5wayhouse-hualien-youth.git
   ```
2. **新增或更換網頁照片**：
   - 將精選照片放至 `web_assets/images/`。
   - 在 `index.html` 的相簿區塊更新圖片路徑。
   - 執行 `git commit` 與 `git push` 即刻全球發布！

### 圖片分類資料夾與獨立 JSON 後台維護指引

為方便管理，專案內的所有圖片均已按展示區塊分類歸檔至專屬資料夾；其中**精選現場照片牆（Gallery）**與**雞舍硬體動福規範輪播（Specs）**由獨立 JSON 設定檔驅動，支援免動程式碼即可維護圖片說明文字：

| 網頁區塊 | 圖片分類目錄 | 對應 JSON 設定檔 | 圖片文字說明（Caption）支援 |
| :--- | :--- | :--- | :--- |
| **現場相簿牆** | `web_assets/images/gallery/` | `web_assets/data/gallery_config.json` | ✅ 支援（照片下方圖說、GLightbox 燈箱標題與詳細描述） |
| **硬體規範輪播** | `web_assets/images/specs/` | `web_assets/data/coop_specs.json` | ✅ 支援（6 項工法標準、數據與詳細說明） |
| **Hero 封面背景** | `web_assets/images/hero/` | 靜態 HTML 直接指定 | 無需額外圖說，替換目錄內同名照片即可更新 |
| **專案緣起** | `web_assets/images/about/` | 靜態 HTML 直接指定 | 無需額外圖說，替換目錄內同名照片即可更新 |
| **雞舍搭建三卡片** | `web_assets/images/coop-building/` | 靜態 HTML 直接指定 | 卡片標題與內文由 HTML 維護，圖片無額外圖說 |
| **動物福利** | `web_assets/images/welfare/` | 靜態 HTML 直接指定 | 卡片標題與內文由 HTML 維護，圖片無額外圖說 |
| **10 隻雞老師** | `web_assets/images/chickens/` | 靜態 HTML 直接指定 | 包含姓名、個性標籤與性格介紹，圖片無額外圖說 |
| **數位大數據** | `web_assets/images/data/` | `web_assets/data/egg_stats.json` & `egg_records.csv` | ✅ 支援動態自動運算（累計產蛋數、單重、破損率、筆數與時間區間） |
| **孩子手繪心智圖**| `web_assets/images/mindmap/` | 靜態 HTML 直接指定 | 小仁、小柔、小菱手繪真跡，支援點擊放大 |

### 📊 產蛋大數據自動更新與同步指引

網頁中的 Hero 累計指標與 **第 08 章節「智慧養雞管理系統」大數據卡片** 支援**全自動動態統計與更新**：

#### 兩種更新方式：
1. **即時雲端連線模式（即時自動更新）**：
   - 在 Google 試算表（五味屋養雞管理系統）中，點選 `檔案` ➔ `共用` ➔ `發布到網路` ➔ 選擇「`收蛋記錄`」工作表 ➔ 格式選「`CSV`」並發布。
   - 將產生的 CSV 網址填入 `web_assets/data/egg_stats.json` 的 `"remote_csv_url"` 欄位。
   - 網頁載入時會自動自 Google Sheets 抓取最新收蛋明細並動態運算所有數據，**完全無需手動修改程式碼**！
2. **本機/倉庫資料更新模式**：
   - 當團隊更新 `web_assets/data/egg_records.csv` 後，在終端機執行一鍵同步腳本：
     ```bash
     python3 scripts/sync_egg_data.py
     ```
   - 腳本將自動重新計算各項指標，並更新 `web_assets/data/egg_stats.json`。

### 📸 網頁精選照片與說明（Caption）維護手冊

網頁上的精選照片區塊採 **「資料驅動（Data-Driven）」** 架構，**負責修改網頁的人員完全不需要修改任何 HTML 程式碼**，即可更新照片與文字說明。

#### 1. 照片命名與排序規則（依活動日期 `mmdd` 先後排序）
- 實體圖片目錄：`web_assets/images/gallery/`
- 檔名規範：**`mmdd_流水號_簡述.jpg`**（例如 `0530_01_visit_farm.jpg` 至 `0825_12_presentation_prep.jpg`，共 12 張）。
- **展現版面規則**：
  - **電腦/桌面版（Desktop）**：呈現 12 張真實精選照片，維持最完美的 **3 × 4 矩陣對稱網格**。
  - **手機版（Mobile）**：完整呈現全部 12 張照片（時間序完整從 05/30 黎明方舟至 08/25 結案成發），直向 2 欄排列（共 6 列滿版，保持對齊無空白）。
- **更換照片方式**：若要替換或新增照片，請將新照片放置於 `web_assets/images/gallery/` 並維持 `mmdd_流水號_簡述.jpg` 檔名，並至 `web_assets/data/gallery_config.json` 更新對應之路徑與圖說。

#### 2. 如何修改照片說明（Caption）？
所有精選照片的圖說均記錄在獨立的 JSON 設定檔中：
- **設定檔路徑**：`web_assets/data/gallery_config.json`

使用任何文字編輯器（如 VS Code、記事本或 GitHub 網頁線上編輯）打開該檔案，即可看到如下結構：
```json
{
  "id": "gallery_01",
  "image": "web_assets/images/gallery/0530_01_visit_farm.jpg",
  "alt": "參訪黎明方舟牧場",
  "caption": "五味屋兒少參訪黎明方舟牧場，實地觀摩友善畜牧環境。",
  "description": "五味屋兒少赴壽豐黎明方舟牧場實地見習，初次接觸符合動物福利標準的非籠飼飼養環境與母雞生活作息。"
}
```

各欄位修改指南：
- **`caption`**：**【最核心】** 顯示在網頁照片正下方的說明文字（建議 10~25 字，簡明扼要）。
- **`description`**：點擊照片放大進入燈箱（Lightbox）模式時，右下方顯示的詳細介紹故事（若無可留空 `""`）。
- **`alt`**：無障礙讀取與替代文字。
- **`image`**：圖片路徑（對應 `web_assets/images/gallery/mmdd_...jpg`）。

#### 3. 儲存與發布上線流程
1. 在本機修改並儲存 `web_assets/data/gallery_config.json`（若有替換照片，一併將圖片放入 `web_assets/images/gallery/`）。
2. 在終端機執行安全同步三步驟：
   ```bash
   git add web_assets/data/gallery_config.json web_assets/images/gallery/
   git commit -m "docs/content: 更新精選照片說明與圖庫"
   git push origin main
   ```
3. GitHub Pages 即會在 1~2 分鐘內自動構建發布，全球訪問者均能看到最新更新的照片與說明文字！

---

### 🤖 延續 Gemini AI 對話協作（共同完成網頁）
若協作者需要對網頁版面、文案細節、互動模組或攤位海報規劃繼續提問或迭代，可直接點擊以下分享連結接續對話：
- 💬 **Gemini 網頁設計對話（可直接繼續提問）**：[https://share.gemini.google/hWfb7eqjiXg9](https://share.gemini.google/hWfb7eqjiXg9)

---
*本專案由「聞雞起舞」團隊與五味屋共同推動。*

