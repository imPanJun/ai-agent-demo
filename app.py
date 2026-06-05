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
    
    # 當左邊的按鈕被按下時，右邊才會開始跑動態
    if start_btn:
        # st.empty() 是一個容器，讓我們可以動態替換裡面的文字
        log_container = st.empty()
        
        # 模擬黑客松 Demo 最愛看的動態思考過程
        with log_container.container():
            st.info(f"💡 收到指令！目標：以「{tone}」語氣，製作關於「{keyword}」的{task}。")
            time.sleep(1.5)
            
            st.write("🔍 步驟 1：正在呼叫 Perplexity API 搜尋最新數據... (成功)")
            time.sleep(1.5)
            
            st.write("📊 步驟 2：正在整合內容並建立邏輯大綱... (成功)")
            time.sleep(1.5)
            
            st.write("🎨 步驟 3：正在跨系統呼叫簡報生成工具... (完成)")
            time.sleep(1.5)
            
            st.success("🎉 任務跨系統協調完畢！")
        
        # 跑完後，直接在右下角生出一個下載按鈕 (模擬成品產出)
        st.download_button(
            label="👉 點我下載 PPT 簡報草稿",
            data="這是一份假的檔案內容，未來黑客松可以串接真實的 PPT 生成套件",
            file_name="員工培訓簡報.txt",
            mime="text/plain"
        )
