import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🤝 TrustMeter - Human–AI Trust Calibration Simulator")

# Sample AI predictions
data = pd.DataFrame({
    "Incident_ID": range(1, 6),
    "AI_Confidence": np.random.uniform(0.5, 1.0, 5),
    "AI_Decision": np.random.choice(["Critical", "Warning", "Safe"], 5)
})

st.write("### AI Incident Decisions")
st.dataframe(data)

user_trust = []
for i in range(len(data)):
    trust = st.slider(f"Your trust in Incident {i+1} ({data.AI_Decision[i]})", 0.0, 1.0, 0.5, 0.1)
    user_trust.append(trust)

data["User_Trust"] = user_trust
data["Trust_Calibration_Error"] = abs(data["User_Trust"] - data["AI_Confidence"])

st.write("### Trust Calibration Visualization")
fig, ax = plt.subplots()
ax.scatter(data["AI_Confidence"], data["User_Trust"], color="blue")
ax.plot([0,1],[0,1],"--",color="gray")
ax.set_xlabel("AI Confidence")
ax.set_ylabel("User Trust")
st.pyplot(fig)

st.write("Average Trust Calibration Error:", round(data["Trust_Calibration_Error"].mean(), 3))
