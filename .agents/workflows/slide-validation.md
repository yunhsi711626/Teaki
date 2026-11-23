# Workflow 06 — Slide Validation

## Goal
驗證 HTML 簡報的內容、引用、操作及視覺呈現。

## Trigger
Slide Generation 已產生 HTML。

## Input
- `AGENTS.md`
- `slides/deck.html`、`slides/drafts/`、`slides/evidence-map.md`
- 已通過驗證的 Wiki

## Steps

### Step 1. HTML Structure Check
確認 HTML 可解析、頁數 10–12、各頁有必要內容、引用資訊存在、本機路徑有效。

### Step 2. Navigation Check
實際測試上一頁、下一頁、左右方向鍵、首尾邊界、行動裝置觸控操作。

### Step 3. Visual Check
使用實際瀏覽器測試桌面、平板及手機：文字與圖片是否溢出、圖表是否可用、按鈕是否可見及文字是否易讀。

無瀏覽器測試環境時須標記 `Not Run`，不得宣稱通過。

### Step 4. Content Review
由獨立程序對照 HTML、逐頁草稿、Wiki、原始來源，確認無新增無證據事實、定義／數字／分類準確、引用正確、與核准草稿一致。

### Step 5. Classify Errors
- HTML 結構、按鈕、排版 → HTML 渲染。
- 逐頁文字過多 → Slide Drafts。
- 引用錯誤 → Evidence Map 或 Wiki。
- 知識錯誤 → 對應 Wiki 節點。

### Step 6. Revalidate
只修正失敗項目；修正後重新檢查受影響功能及必要的回歸測試。

### Step 7. Generate Final Report
記錄檢查日期、測試環境、測試項目、`Passed` / `Failed` / `Not Run`、錯誤、修正、前後結果與輪次。

### Step 8. Prepare Delivery
全部必要檢查通過後保存 HTML、更新 README、保存紀錄、建立 Git 版本。**只有使用者授權後**才可發布網頁，並需實際檢查公開連結。

## Local Loop
HTML 測試 → 問題分類 → 局部修正 → 重新測試；最多自動修正 3 輪。

## Output
- `slides/deck.html`
- `reports/slide-validation.md`
- `reports/final-report.md`

## Exit Conditions
- HTML 有 10–12 頁。
- 導覽、圖片與圖表、桌面／行動裝置排版通過實測。
- 教學內容與 Wiki 一致、引用有效。
- 最終檢查報告完整。

## Failure Routing
- 功能問題 → Slide Generation 渲染階段。
- 內容過長 → Slide Generation 草稿階段。
- 引用或知識錯誤 → 對應 Wiki 或證據節點。
- 超過 3 輪 → 停止並通知使用者。

## Logging
保存各輪測試、錯誤數、修正內容、重測結果與最終狀態。
