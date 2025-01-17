from openai.types.chat.chat_completion import ChatCompletion
import openai
from system_prompt.system_prompt import system_prompt_1
from chat_history.chat_history import chat_history_test_data
import os 
import json
import logging
from pydantic import BaseModel
import time
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# 設定 logging 的基礎設置
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt", mode='a', encoding='utf-8'),  # 寫入 log進入 log.txt
        logging.StreamHandler()  # 同時輸出到Terminal
    ]
)

#透過定義Pydantic模型來描述預設的輸出格式
class Score(BaseModel):
    information_accuracy: float
    brand_engagement : float
    service_attitude : float
class ChatBotOutput(BaseModel):
    context: str
    score:Score

def generate_quick_replies(new_user_messages, system_prompt, chat_history=None):
    """
    根據使用者提供的新訊息，system_prompt和聊天紀錄，產生快速回應

    Args:
    - new_user_messages (str): 使用者的新訊息
    - system_prompt (str): 系統提示
    - chat_history (list, optional): 聊天紀錄,預設為None

    Returns:
    - dict: 回應訊息的Dict,包含context、score、input_token、cache_token和out_token
    """
    #從.env初始化OPEN_AI_KEY
    openai.api_key = OPENAI_API_KEY
    
    #設定System Prompt
    messages = [
        {"role": "developer", "content": system_prompt}, #gpt-4o 以上官方建議可以使用role:developer 作為設定system_prompt 的角色
    ]

    #設定歷史聊天紀錄
    if chat_history is not None:
        messages.extend(chat_history)

    messages.append({"role": "user", "content": new_user_messages})

    #設定錯誤迭代嘗試起始
    iterations = 0
    result=""

    #設定錯誤迭代嘗試 不超過3次
    while type(result) is str and iterations < 3:
        try:
            logging.info(f"Log: Start {new_user_messages}")
            completion: ChatCompletion = openai.beta.chat.completions.parse(
                model="gpt-4o",
                messages=messages,
                temperature=0.7,    
                response_format=ChatBotOutput,
            )
            result = {
            "context": completion.choices[0].message.parsed.context,  #LLM 的回覆
            "score":{
            "information_accuracy" :completion.choices[0].message.parsed.score.information_accuracy, #LLM 自評的準確率
            "brand_engagement" :completion.choices[0].message.parsed.score.brand_engagement,    #LLM 自評的品牌互動
            "service_attitude" :completion.choices[0].message.parsed.score.service_attitude,    #LLM 自評的服務態度
            },
            "input_token": completion.usage.prompt_tokens,  #使用者的輸入token
            "cache_token" : completion.usage.prompt_tokens_details.cached_tokens, #使用者的緩存token
            "out_token": completion.usage.completion_tokens #LLM 的回覆token
        }
            #儲存成功聊天紀錄至log.txt
            logging.info(f"Log: Success: {new_user_messages}")
        except Exception as e:
            #儲存錯誤聊天紀錄至log.txt
            logging.info(f"Log: Error message {e} on {new_user_messages}")
            iterations += 1
            result = "很抱歉,我無法理解您的問題,請再試一次。"
    
    return result
    
def run_test(scope):

    """
    執行測試
    scope: int, 測試報告的數量
    """
    for tag in range(1,scope+1):
        report = []
        for test_data in chat_history_test_data:
            result = generate_quick_replies(test_data['faq'],system_prompt_1,test_data['chat_history'])
            #設置time.sleep避免同時間過多的請求
            time.sleep(1)
            report.append(result)
        #將報告寫入report 資料夾
        with open(f"report/report_{tag}.json", "w", encoding="utf-8") as file:
            json.dump(report, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    run_test("int number of report you want to generate")
