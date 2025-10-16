# TrustMeter — Human–AI Trust Calibration Simulator

### Purpose
**TrustMeter** is a prototype Streamlit dashboard that simulates collaborative decision-making between humans and AI.  
It visualises how user trust aligns with model confidence — a concept known as *trust calibration*.

This experiment explores early ideas from my MSc by Research proposal at the **University of Bristol**,  
*“Cognitive Reliability: Human–AI Collaboration in Incident Response.”*

---

### Features
- Simulated AI incident decisions (Critical, Warning, Safe)
- Adjustable user trust sliders per decision
- Real-time visualisation of trust vs. confidence
- Computation of average *trust calibration error*
- Downloadable CSV of session results

---

### Tech Stack
- **Python 3.10+**  
- **Streamlit** — UI and interactivity  
- **Pandas, NumPy** — data simulation and metrics  
- **Matplotlib** — plotting and visualisation  

---

### How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/TrustMeter-Human-AI-Trust-Dashboard.git
cd TrustMeter-Human-AI-Trust-Dashboard

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
