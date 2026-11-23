# Workflow 04 — Wiki Validation

## Goal
驗證 Wiki 知識準確性、引用可追溯性及結構完整性。

## Trigger
Wiki Synthesis 完成或 Wiki 更新後。

## Input
- `AGENTS.md`
- `wiki/sources/`、`wiki/topics/`、`wiki/index.md`
- 原始來源、既有檢查紀錄

## Steps

### Step 1. Structural Validation
檢查首頁、必要主題頁、來源頁、內部連結、Source ID 一致性及成功 Ingest 數量至少 5 篇。

### Step 2. Citation Validation
逐項驗證來源 ID 真實存在、引用位置對應原始證據、轉述無誤、沒有虛構引用。

### Step 3. Knowledge Validation
檢查茶類分類、品種與茶類區別、製程說明、來源衝突標示、過度推論。

### Step 4. Independent Review
由與生成分離的審查程序只看 Wiki、原始來源及審查標準；僅提出問題和證據，不直接修改內容。

### Step 5. Generate Report
問題清單需含問題 ID、頁面、類型、來源、說明、退回節點及修正狀態。

## Local Loop
檢查 → 問題清單 → 退回指定節點 → 重查受影響內容；每個修正任務最多 3 輪。

## Output
- `reports/wiki-validation.md`
- Wiki 檢查狀態與通過版本識別

## Exit Conditions
- 所有必要檢查通過。
- 無未處理重大知識錯誤。
- 重要引用均可追溯。
- 衝突標示、結構及連結皆通過。

未通過不得進入 Slide Generation。

## Failure Routing
- 來源資訊錯誤 → Source Research。
- 擷取錯誤 → Wiki Ingest。
- 主題錯誤 → Wiki Synthesis。
- 單純來源 ID 錯誤 → 對應頁局部修正。
- 超過 3 輪 → 停止並通知使用者。

## Logging
記錄錯誤類別、受影響頁面、修正輪次、每輪檢查結果。
