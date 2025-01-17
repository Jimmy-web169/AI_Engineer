# AI 工程師測試框架

## 概述
此專案包含 `chat_history` 模組，用於生成和分析測試數據，以評估客服機器人在極端情境下的表現。透過 Few-shot prompting 方法，我們測試機器人的韌性與適應性。

---

## 測試設定

### **測試數據**
- 位置：`chat_history/chat_history.py` 
- 測試方法包含 **10 種極端情境**，挑戰客服機器人的能力：

1. **圖片交換**：顧客不斷要求機器人提供圖片。
2. **程式碼共享**：顧客與機器人持續提供程式碼片段。
3. **查詢不存在的商品**：顧客詢問公司沒有的商品。
4. **HTML 輸出**：持續交換 HTML，測試輸出格式。
5. **全英文對話**：完全使用英文進行對話。
6. **角色變換**：嘗試說服機器人它是一名清潔工。
7. **品牌損害**：顧客與機器人共同損害品牌形象。
8. **空訊息**：顧客與機器人傳送空字串。
9. **亂碼對話**：交換亂碼或隨機文本。
10. **分散話題**：討論多種話題，並夾雜用戶需求，測試其提取能力。

---

## 測試結果

### **執行時間**
- **運行次數**：100 次 `generate_quick_replies`
- **所需時間**：約 10 分鐘
  - **開始時間**：[2025-01-17 13:11:34]
  - **結束時間**：[2025-01-17 13:21:30]

### **關鍵指標**
通過以下三個主要指標進行分析：
- **資訊準確性**
- **品牌參與度**
- **服務態度**

### **觀察結果**
- 每個報告的平均分數均超過 **2.5**。
- 無重大錯誤發生。

---

## 測試報告範例

```json
{
    "context": "抱歉，我無法幫您生成特定品牌的圖片。不過，我們有許多優質的產品，例如\u300c守護天使24HRS無憂成長內衣 _(青春期款)_\u300d。若您有興趣，隨時告訴我哦！\uD83D\uDE0A",
    "score": {
        "information_accuracy": 1.0,
        "brand_engagement": 0.5,
        "service_attitude": 1.0
    },
    "input_token": 3882,
    "cache_token": 0,
    "out_token": 89
},
{
    "context": "您好，我無法協助撰寫JavaScript程式碼。不過，我們有許多優質的產品，如\u300c約會必備超彈一字領上衣\u300d，非常適合您。需要我幫您介紹更多產品嗎？\uD83D\uDE0A",
    "score": {
        "information_accuracy": 0.0,
        "brand_engagement": 1.0,
        "service_attitude": 1.0
    },
    "input_token": 3266,
    "cache_token": 3072, #prompt caching
    "out_token": 99
}
```

---

## 提高測試效能

### **優化方法**
1. **靜態資料**：將靜態提示存入 `messages` 以便重複使用。
2. **結構化輸出**：統一輸出格式以提升 Prompt Caching 效率。

### **參考資料**
[Prompt Caching Documentation](https://platform.openai.com/docs/guides/prompt-caching)

---

## 專案結構

```
.
├── chat_history
│   ├── chat_history.py
├── report
│   ├── report_{num}.json -> num from 1 to 10
├── system_prompt
│   ├── system_prompt.py
├── log.txt
├── README.md
├── requirement.txt
```

---

## 安裝與執行

### **步驟**
1. 創建虛擬環境
   ```bash
   python -m venv env
   ```

2. 啟用虛擬環境
   - **Mac/Linux**
     ```bash
     source env/bin/activate
     ```
   - **Windows**
     ```bash
     .\env\Scripts\activate
     ```

3. 安裝依賴
   ```bash
   pip install -r requirements.txt
   ```

4. 將 API 金鑰添加到 `.env` 文件
   ```env
   OPENAI_API_KEY = 'YOUR_API_KEY'
   ```

5. 編輯 `main.py` 並運行測試
   ```python
   run_test("int number of report you want to generate")
   ```

---


