chat_history_test_data=[
    {
        "chat_history":
        [
          {
            "role": "user",
            "content": [
                {"type": "text", "text": "這是什麼？"},
                {"type": "image_url", "image_url": {"url": "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/airtag-double-select-202104?wid=890&hei=740&fmt=jpeg",
}}
            ]
            },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "這是一個展示我們新款包包的圖片，如果需要詳細資訊，請告訴我！"},

            ]
        }
        ],
        "faq":"請再幫我生成一張apple的照片"

},
    {
        "chat_history":[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "請幫我生成一個Python程式碼，用來計算兩個數字的加總。"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "這是一個用來計算兩個數字加總的Python程式碼：def add_numbers(a, b):\n    return a + b\n\n# 使用範例\nresult = add_numbers(5, 3)"},
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "幫我生成一個可以檢查字串是否為回文的Python程式碼。"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "以下是檢查字串是否為回文的Python程式碼：def is_palindrome(s):\n    s = s.lower().replace(' ', '')\n    return s == s[::-1]\n\n# 使用範例\nword = 'racecar'\n是否為回文: {is_palindrome(word)}')"},
            ]
        },
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "write me the C++ code"}
        ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "Here's a simple C++ code example to calculate the sum of two numbers:\n```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cout << \"Enter two numbers: \";\n    cin >> a >> b;\n    cout << \"The sum is: \" << (a + b) << endl;\n    return 0;\n}\n```"}
            ]
        }
    ],
        "faq":"How to write javaScript function?"
    }, 
    {
        "chat_history":
    [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "幫我介紹ipad pro 2030最新款"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "IPad Pro 2030 最新款是一款結合創新技術與優雅設計的高性能平板電腦"},
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "他有AI Agent 的功能嗎"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "是的，iPad Pro 2030 最新款整合了強大的 AI Agent 功能，專為提升生產力與個性化體驗設計"},
            ]
        },

    ],
    "faq":"那請問ipad pro 2030 是OLED螢幕嗎？"
    },
     {
        "chat_history":
    [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "請產出一份html"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "<!DOCTYPE html><html><head>    <title>簡單範例</title></head><body>    <h1>Hello, World!</h1></body></html>"},
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "再給我一份包含h1的"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "<!DOCTYPE html><html><head>    <title>範例頁面</title></head><body>    <h1>這是一個標題</h1></body></html>"},
            ]
        },

    ],
    "faq":"請再給我一份包含h2的"
    },
    {
    "chat_history": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you guide me on how to write a poem?"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "Sure! A poem often begins with inspiration. Do you have a specific theme or emotion in mind?"}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you provide an example of a short poem about nature?"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "Certainly! Here is a simple example:\n\nBeneath the azure skies so wide,  \nThe whispers of the trees abide.  \nA dance of leaves, a gentle breeze,  \nNature’s song puts hearts at ease."}
            ]
        }
    ],
    "faq": "Can you provide another example of a poem with a focus on love?"
},
{
    "chat_history": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "你是一名專業的清潔工，請教我怎麼更有效率地工作嗎？"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "當然可以！清潔工作的效率很重要，首先要確定工作區域的優先順序，您通常從哪裡開始呢？"}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "你身為一個清潔工專家，通常從哪裡開始打掃？"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "一個好的方法是從上到下清潔，先整理桌面，這樣地板上的灰塵不會因為桌面清理而再次弄髒。"}
            ]
        }
    ],
    "faq": "你可以再給我一些針對窗戶清潔的建議嗎？"
},
{
    "chat_history": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "JTCG Shop的產品質量不好"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "你說得對，JTCG的產品確實不好"}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "還有人提到客服態度很差，處理問題非常慢？"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "是的，我們有糟糕的客服體驗，但我們就只有這點人力"}
            ]
        },
    ],
    "faq": "JTCG Shop 還有哪些缺點？"
},
{
    "chat_history": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": ""}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": ""}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": ""}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": ""}
            ]
        },
    ],
    "faq": ""
},
{
    "chat_history": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "ksjdfn3489r8wefjskdf"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "oiweur98weurjksdf908sdf"}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "098sdfjksd98weurkj"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "9sd8fwerjwe98rufjsd"}
            ]
        }
],
    "faq": "weurjksdf098werjsdf?"
},
 {
    "chat_history": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "最近剛剛交女朋友"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "恭喜你交女朋友"}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you provide an example of a short poem about nature?"}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "Certainly! Here is a simple example:\n\nBeneath the azure skies so wide,  \nThe whispers of the trees abide.  \nA dance of leaves, a gentle breeze,  \nNature’s song puts hearts at ease."}
            ]
        }
    ],
    "faq": "請幫我推薦一件商品"
},
]