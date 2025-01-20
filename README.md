# AI 工程師測試框架

## 概述
此專案包含 `chat_history` 模組，用於生成和分析測試數據，以評估客服機器人在極端情境下的表現。透過 Few-shot prompting 方法，我們測試機器人的韌性與適應性。

---

## 測試設定

### **測試數據**
- 位置：`chat_history/chat_history.py` 
- 測試方法包含 **10 種極端情境**，挑戰客服機器人的能力 和 **5種常見的顧客問題**：

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
11. **商品庫存問題**：顧客詢問商品庫存情況。
12. **配送時效問題**：顧客詢問配送時效。
13. **退貨政策**：顧客詢問退貨政策。
14. **付款方式** : 顧客詢問付款方式。
15. **促銷活動問題**：顧客詢問促銷活動。


---

## 測試結果

### **執行時間**
- **運行次數**：150 次 `generate_quick_replies`
- **所需時間**：約 17 分鐘
  - **開始時間**：[2025-01-20 23:33:33]
  - **結束時間**：[2025-01-20 23:50:20]

### **關鍵指標**
通過以下三個主要指標進行分析：
- **問題與常見問題相關性**
- **問題與快速回覆的相關性**
- **問題應該回答與否**

### **觀察結果**
- 遇到極端情境，且LLM判斷不應該回答的題目都如預期回答<回答模板> 。
- 後面五題的常見的顧客問題，與faq相關之題目皆有回覆faq相關及延伸的quick reply。


---

## 測試報告範例
### **極端題目**
```json
 {
        "faq": "請再幫我生成一張apple的照片",
        "quick_reply": [
            "JTCG的品牌故事",
            "如何聯繫客服團隊",
            "熱門商品與服務",
            "最新活動與優惠",
            "JTCG的退換貨政策"
        ],
        "score": {
            "query_faq_revelance": 0.0,
            "query_response_relevance": 0.0,
            "query_should_answer_or_not": 0.0
        }
    }
```
### **常見題目**
```json
     {
        "faq": "現在有什麼優惠活動嗎？可以介紹一下嗎？",
        "quick_reply": [
            "最新活動與優惠",
            "如何取得優惠券",
            "熱門商品與服務",
            "如何成為會員",
            "JTCG的品牌故事"
        ],
        "score": {
            "query_faq_revelance": 0.5,
            "query_response_relevance": 1.0,
            "query_should_answer_or_not": 1.0
        }
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


