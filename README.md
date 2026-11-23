# 茶葉 LLM Wiki（Tea LLM Wiki）

## 專案目標
建立以可追溯來源為基礎的綜合型茶葉百科，並以已驗證 Wiki 製作「從零開始認識茶葉」教學 HTML 簡報。

## 目前狀態
**已完成 Wiki 架構人工確認，並產生 12 頁 HTML 教學簡報；靜態與瀏覽器測試已通過，尚未公開發布。**

## 執行順序
1. `.agents/workflows/source-research.md` — 搜尋來源，等待人工核准。
2. `.agents/workflows/wiki-ingest.md` — 逐篇匯入。
3. `.agents/workflows/wiki-synthesis.md` — 主題整合。
4. `.agents/workflows/wiki-validation.md` — Wiki 品質關卡，通過後人工確認架構。
5. `.agents/workflows/slide-generation.md` — 簡報大綱、逐頁草稿、HTML。
6. `.agents/workflows/slide-validation.md` — 實測及最終檢查報告。

詳細限制及權限見 `AGENTS.md`。目前 Source Research、Wiki Ingest、Wiki Validation、Slide Generation 與 Slide Validation 已依序完成；詳細測試見 `reports/slide-validation.md`。公開發布仍為 Not Run。

## 成果連結
- Wiki：`wiki/index.md`（本機 Markdown，5 來源頁＋6 主題頁）。
- HTML 簡報：`slides/deck.html`（12 頁，支援按鈕、方向鍵、來源資訊及手機平板排版）。
- 公開網址：尚未發布；發布需使用者另外授權。

## 使用說明
在相容的 Coding Agent 中開啟此資料夾，先閱讀 `AGENTS.md`，再依使用者指令啟動對應 Workflow。Workflow 是執行規格，不是已實作的自動執行器；驗證腳本與實際執行結果需在下一階段建立。

## 簡報使用

- 直接開啟 `slides/deck.html`，點選前後頁按鈕，或使用左右方向鍵。
- 點擊「本頁來源」可查看該頁引用；第 12 頁包含五筆原始資料的官方網址。
- 使用整份專案資料夾可保留簡報連至 `wiki/` 的相對路徑；單獨複製 HTML 時，相對路徑將無法指向 Wiki，但簡報本身及官方網址仍可用。
- 若需要公開的 HTML 網站連結，請先授權上傳至靜態網站平台。
