import streamlit as st
import numpy as np


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cloud Storage Dashboard", layout="wide")

st.title("☁️ Cloud Storage Growth Dashboard")
st.markdown("Predict corporate cloud storage usage using **Exponential + Logistic Growth Model**")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Input Parameters")

S0 = st.sidebar.number_input("Initial Storage (GB)", value=50)
S_max = st.sidebar.number_input("Maximum Capacity (GB)", value=1000)
r = st.sidebar.slider("Growth Rate", 0.01, 0.2, 0.05)
days = st.sidebar.slider("Time (Days)", 10, 365, 200)
daily_upload = st.sidebar.number_input("Daily Upload (GB/day)", value=5)

# ---------------- DATA ----------------
t = np.linspace(0, days, 100)

S_exp = S0 * np.exp(r * t)
S_log = S_max / (1 + np.exp(-r * (t - days/2)))
S_combined = np.minimum(S_exp + daily_upload * t, S_log)

threshold = 0.8 * S_max

# ---------------- EXPANSION DAY ----------------
expansion_day = None
for i in range(len(t)):
    if S_combined[i] >= threshold:
        expansion_day = int(t[i])
        break

# ---------------- METRICS (TOP CARDS) ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📦 Final Storage (GB)", f"{S_combined[-1]:.2f}")
col2.metric("⚡ Growth Rate", f"{r}")
col3.metric("📅 Days Simulated", f"{days}")

# ---------------- ALERT ----------------
if expansion_day:
    st.error(f"⚠️ Expansion needed around Day {expansion_day}")
else:
    st.success("✅ Storage within safe limits")

# ---------------- INTERACTIVE PLOT ----------------
fig = go.Figure()

fig.add_trace(go.Scatter(x=t, y=S_exp, mode='lines', name='Exponential'))
fig.add_trace(go.Scatter(x=t, y=S_log, mode='lines', name='Logistic'))
fig.add_trace(go.Scatter(x=t, y=S_combined, mode='lines', name='Combined', line=dict(width=4)))

fig.add_hline(y=threshold, line_dash="dash", annotation_text="80% Capacity")

fig.update_layout(
    title="Cloud Storage Growth Prediction",
    xaxis_title="Time (Days)",
    yaxis_title="Storage (GB)",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- EXTRA INSIGHT ----------------
st.subheader("📊 Insights")

st.write(f"""
- Combined model prevents unrealistic exponential overflow  
- Storage approaches limit due to logistic constraint  
- Expansion threshold (80%) helps in planning infrastructure  
""")
