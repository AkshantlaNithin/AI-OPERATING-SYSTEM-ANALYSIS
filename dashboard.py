import streamlit as st
import pandas as pd
import psutil
import time
import plotly.express as px

st.set_page_config(
    page_title="AI-powered OS Performance Analyser",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚡ AI-powered OS Performance Analyzer")
st.write("Welcome to the AI-driven system performance monitoring tool!")

# Live data
def get_live_data():
    return {
        'CPU Usage (%)': psutil.cpu_percent(),
        'Memory Usage (%)': psutil.virtual_memory().percent,
        'Disk Usage (%)': psutil.disk_usage('/').percent,
        'Running Processes': len(psutil.pids())
    }

live_data = []
for _ in range(10):
    live_data.append(get_live_data())
    time.sleep(1)

df = pd.DataFrame(live_data)

# CPU load status
latest_cpu = df['CPU Usage (%)'].iloc[-1]
if latest_cpu < 50:
    cpu_status = "🟢 Normal Load"
    color = "green"
elif latest_cpu < 80:
    cpu_status = "🟡 Medium Load"
    color = "yellow"
else:
    cpu_status = "🔴 High Load! Optimize Now!"
    color = "red"

st.markdown(
    f"""<div style="padding:12px;border-radius:10px;background:linear-gradient(135deg,#1E3C72,#2A5298);color:white;font-size:22px;text-align:center">
    🖥️ CPU Status: <span style="color: {color};">{cpu_status}</span>
    </div>""", unsafe_allow_html=True
)

# Plot CPU Usage
fig = px.line(df, y="CPU Usage (%)", title="📊 CPU Usage Over Time", markers=True)
fig.update_layout(plot_bgcolor="#161B22", paper_bgcolor="#0E1117", font=dict(color="white"))
st.plotly_chart(fig, use_container_width=True)

# High usage warning
if latest_cpu > 80:
    st.error(" **Warning: High CPU Usage Detected!** 🚨")

# Display data
st.markdown("### 📋 System Performance Data")
st.dataframe(df.style.set_properties(**{'background-color': '#161B22', 'color': 'white'}))
