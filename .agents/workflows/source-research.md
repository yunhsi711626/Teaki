# Workflow 01 — Source Research

## Goal
自動搜尋、篩選並建立至少 5 篇茶葉相關資料的候選來源清單。

## Trigger
使用者要求初始化 Wiki、搜尋來源或補充資料時；不得自行啟動定期更新。

## Input
- `AGENTS.md`
- Wiki 主題與知識範圍
- 現有來源清單（如有）
- 使用者指定的額外條件（如有）

## Steps

### Step 1. Search Sources
搜尋政府或官方研究機構、可查證學術論文、專業茶葉研究或教學網站。優先確保來源涵蓋不同知識主題。

### Step 2. Build Source Inventory
為候選來源建立 Source ID，記錄標題、作者或機構、日期、URL 或出版識別碼、類型、涵蓋主題、可信度說明及是否能取得可閱讀內容。

### Step 3. Validate Sources
逐項檢查：
- 來源是否真實存在？
- 是否可取得足夠原始內容？
- 是否與茶葉知識相關？
- 是否為重複來源？
- 是否具有可追溯的發布資訊？
- 是否存在明顯的可靠性疑慮？

無法取得原始內容的來源不得標記為已通過。

### Step 4. Check Coverage
確認候選來源能支援 Wiki 主要主題；欠缺必要面向時補充搜尋。有效來源至少 5 篇。

### Step 5. Human Approval
向使用者呈現候選來源清單，等待確認、刪除或補充來源。未核准不得進入正式 Ingest。

## Local Loop
搜尋 → 來源檢查 → 補充或替換來源 → 重新檢查；最多自動修正 3 輪。

## Output
- `raw/sources.md`
- `reports/source-check.md`
- 經使用者核准的來源清單

## Exit Conditions
- 至少 5 篇不同的有效來源。
- 來源資訊完整且有足夠可讀內容。
- 已完成可信度與去重檢查。
- 使用者已確認清單。

## Failure Routing
- 來源不足、無效或涵蓋不足 → Step 1。
- 超過 3 輪仍失敗 → 停止並通知使用者。
- 使用者拒絕來源 → 依意見返回搜尋階段。

## Logging
記錄搜尋輪次、排除來源及原因、補充來源、最終人工確認結果。未實際執行的步驟標示 `Not Run`。
