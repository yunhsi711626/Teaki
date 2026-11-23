# Workflow 05 — Slide Generation

## Goal
僅根據**已通過驗證的 Wiki**建立 10–12 頁、適合初學者的教學型 HTML 簡報。

## Trigger
Wiki Validation 已通過，且使用者確認 Wiki 架構。

## Input
- `AGENTS.md`
- 已驗證 Wiki、驗證報告
- 已確認 HTML 簡報規格

## Steps

### Step 1. Retrieve Wiki Knowledge
只檢索已通過檢查的 Wiki；不得以外部網頁搜尋結果直接補入簡報內容。

### Step 2. Build Evidence Map
每項教學重點記錄：簡報頁面、教學概念、Wiki 頁面、Source ID、證據位置；無證據則標記不足。

### Step 3. Create Teaching Outline
建議 12 頁（依 Wiki 實際內容調整為 10–12 頁）：
1. 封面
2. 茶葉是什麼？
3. 六大茶類概覽
4. 六大茶類的主要差異
5. 製茶工藝
6. 茶樹品種與茶類的差別
7. 臺灣特色茶
8. 茶葉香氣與風味
9. 基本沖泡方式
10. 如何選擇適合自己的茶
11. 知識總整理
12. 參考資料

### Step 4. Validate Outline
檢查適合初學者、概念涵蓋、順序合理、所有主題有 Wiki 支持及可追溯來源。

### Step 5. Create Slide Drafts
每頁包含標題、教學目標、主要文字、圖像／圖表建議、Wiki 對應資訊、原始引用 ID，避免艱深術語。

### Step 6. Content Fidelity Review
逐頁檢查是否忠於 Wiki、無未授權知識、引用正確、簡化不改變原意、適合初學者。

### Step 7. Render HTML
依通過審查的逐頁草稿生成 HTML，須支援上一頁／下一頁、左右方向鍵、電腦／手機／平板，並提供圖片、比較圖表與引用。

視覺採自然茶文化風格；圖片需有可使用的授權或合法來源。渲染階段不得擅改已核准知識內容。

## Local Loop
大綱 → 檢查 → 修正；逐頁草稿 → 忠實度檢查 → 局部修正。每個修正任務最多 3 輪。

## Output
- `slides/outline.md`
- `slides/evidence-map.md`
- `slides/drafts/`
- `slides/deck.html`
- `reports/slide-generation-log.md`

## Exit Conditions
- 10–12 頁簡報已生成。
- 每頁有教學目標及 Wiki 對應證據。
- 逐頁忠實度檢查通過。
- HTML 存在並可供後續測試。

## Failure Routing
- Wiki 證據不足 → Wiki Synthesis 或 Source Research（需要新的來源核准）。
- 大綱不合理 → Step 3。
- 逐頁內容不正確 → Step 5。
- 渲染異常 → Step 7。
- 超過上限 → 停止並通知使用者。

## Logging
記錄大綱修改、逐頁錯誤、證據不足及修正結果。
