# Workflow 03 — Wiki Synthesis

## Goal
將已驗證的來源整理頁整合為可追溯的主題茶葉百科。

## Trigger
Wiki Ingest 已完成並通過擷取檢查。

## Input
- `AGENTS.md`
- `wiki/sources/` 已通過檢查的來源頁
- 既有主題百科頁（如有）

## Steps

### Step 1. Classify Knowledge
依六大茶類、茶樹品種、臺灣特色茶、製茶工藝、風味與品飲、沖泡方法分類。

### Step 2. Compare Sources
辨識不同來源之間相互支持、補充、矛盾或證據不足的內容。

### Step 3. Handle Conflicts
保留不同觀點與 Source ID，比較年代、資料性質與適用情境。不能判定時標記待確認，不強行合併。

### Step 4. Generate Topic Pages
每個 `wiki/topics/*.md` 建議包含：
- Overview
- Classification or Characteristics
- Detailed Explanation
- Source Differences
- References
- Related Topics

### Step 5. Create Wiki Index
建立 `wiki/index.md`，包含 Wiki 介紹、六個主題入口、已收錄來源數量、來源索引及主題交叉連結。

### Step 6. Check Structure
檢查分類正確、重複與衝突已處理、重要事實有來源、連結有效、沒有無證據的新增說法。

## Local Loop
整合 → 分類與證據檢查 → 局部修正；每個受影響主題最多自動修正 3 輪。

## Output
- `wiki/topics/*.md`
- `wiki/index.md`
- `reports/synthesis-log.md`

## Exit Conditions
- 六個主要主題均有頁面，並標示證據不足的部分。
- 主題內容均由有效來源支持。
- 來源衝突已標記。
- 導覽及交叉引用完整。

不得為補齊章節而編造資料。

## Failure Routing
- 來源頁內容錯誤 → Wiki Ingest。
- 分類整合錯誤 → Step 1 或 Step 4。
- 證據不足 → Source Research（重新取得使用者核准）。
- 主題架構重大變更 → 使用者確認。

## Logging
記錄各主題整合結果、矛盾、分類修正與待確認知識。
