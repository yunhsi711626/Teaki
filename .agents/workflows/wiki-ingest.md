# Workflow 02 — Wiki Ingest

## Goal
逐篇處理已核准的資料，建立來源整理頁，不在此節點直接跨來源合成結論。

## Trigger
Source Research 已通過且使用者核准來源。

## Input
- `AGENTS.md`
- 已核准來源清單
- 原始資料或可讀取的來源內容

## Steps

### Step 1. Read Source
讀取可取得的來源內容；無法讀取部分須註明限制，禁止自行補全文字。

### Step 2. Extract Metadata
擷取 Source ID、標題、作者或機構、年份、URL 或出版資訊、來源類型。

### Step 3. Extract Knowledge
整理主要主題、核心概念、重要事實、分類與定義、製茶工藝、茶葉特徵、引用位置。不適用欄位可留空並註明。

### Step 4. Create Source Page
每篇建立 `wiki/sources/SRC-XXX.md`，建議欄位：
- Metadata
- Summary
- Key Findings
- Evidence（含原始章節或頁碼）
- Related Topics
- Limitations

### Step 5. Validate Extraction
檢查是否忠於原文、來源資訊齊全、關鍵知識有證據、不混淆茶類／品種／產地、未將推論視為事實。

## Local Loop
資料擷取 → 檢查 → 修正來源頁；每篇最多自動修正 3 輪。

## Output
- `wiki/sources/SRC-XXX.md`
- `reports/ingest-log.md`

## Exit Conditions
- 每篇已核准來源都有對應整理頁。
- 來源資訊與證據完整且可查證。
- 至少 5 篇來源成功 Ingest。
- 失敗來源被明確標記、不計入成功數量。

## Failure Routing
- 來源不可讀 → Source Research。
- 擷取錯誤 → Step 3。
- 引用錯誤 → Step 3 或 Step 4。
- 超過修正上限 → 停止受影響工作並通知使用者。

## Logging
記錄各來源結果、錯誤類型、修正次數、成功 Ingest 的實際數量。
