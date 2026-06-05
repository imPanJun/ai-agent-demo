import streamlit as st
import time

# 設定網頁為寬版顯示
st.set_page_config(page_title="AI 總協調官 Demo", layout="wide")

st.title("🚀 AI 總協調官 (Prompt Coach Agent)")
st.markdown("---")

# 切割成左右兩個區塊
col1, col2 = st.columns(2)

with col1:
    st.subheader("【使用者的麻瓜介面】")
    st.write("請回答三個簡單問題：")
    
    # 建立選項按鈕
    task = st.radio("1. 您的任務是？", ["做簡報", "寫企劃", "查資料"])
    tone = st.radio("2. 您的語氣風格？", ["自然口語", "專業嚴肅"])
    keyword = st.text_input("3. 請輸入關鍵字：", "新進員工培訓")
    
    st.write("") # 空行排版
    # 建立執行按鈕
    start_btn = st.button("開始執行 AI 代理", type="primary")

with col2:
    st.subheader("【AI 幕後思考日誌】")
    
    if start_btn:
        log_container = st.empty()
        
        with log_container.container():
            st.info(f"💡 收到指令！目標：以「{tone}」語氣，製作關於「{keyword}」的{task}。")
            time.sleep(1.5)
            
            st.write("🔍 步驟 1：正在呼叫 Perplexity API 搜尋最新數據... (成功)")
            time.sleep(1.5)
            
            st.write("📊 步驟 2：正在整合內容並建立邏輯大綱... (成功)")
            time.sleep(1.5)
            
            st.write("📝 步驟 3：正在生成結構化 Prompt...")
            time.sleep(1.5)
            
            # 根據使用者選擇生成 Prompt
            prompt_text = f"""
Act as an AI assistant.
Task: {task}
Tone: {tone}
Topic: {keyword}

Please provide a structured output that matches the task type.
"""
            st.code(prompt_text, language="markdown")
            
            # 工具推薦邏輯
            tool_map = {
                "做簡報": "Gamma (AI 簡報工具)",
                "寫企劃": "Notion AI / ChatGPT",
                "查資料": "Perplexity (AI 搜尋引擎)"
            }
            recommended_tool = tool_map.get(task, "一般 AI 工具")
            
            st.write("🛠️ 步驟 4：推薦工具 →", recommended_tool)
            time.sleep(1.5)
            
            st.success("🎉 任務跨系統協調完畢！")
        
        # 模擬下載按鈕
        st.download_button(
            label="👉 點我下載 Prompt 草稿",
            data=prompt_text,
            file_name="AI_prompt.txt",
            mime="text/plain"
        )
