<img width="917" height="426" alt="Screenshot 2026-04-05 180542" src="https://github.com/user-attachments/assets/4a7f4463-180e-4a6b-8e9d-da19127183eb" />

<img width="826" height="401" alt="Screenshot 2026-04-05 180904" src="https://github.com/user-attachments/assets/fa25c990-8ea8-4f74-bba0-74172d42a6f6" />

<img width="896" height="407" alt="Screenshot 2026-04-05 173821" src="https://github.com/user-attachments/assets/14c1a9c7-74dd-4fa2-8cf0-649b6b98cac6" />

<img width="900" height="414" alt="Screenshot 2026-04-05 171928" src="https://github.com/user-attachments/assets/8418c246-1064-458e-8c81-5efcc0af31b5" />

<img width="846" height="438" alt="Screenshot 2026-04-05 172009" src="https://github.com/user-attachments/assets/861c7100-d4a7-4c4f-b641-c9a989ff593d" />

<img width="908" height="429" alt="Screenshot 2026-04-05 180622" src="https://github.com/user-attachments/assets/5eece126-dc7a-482a-912b-b318f8ec472b" />

<img width="925" height="418" alt="Screenshot 2026-04-05 180651" src="https://github.com/user-attachments/assets/4bbc5b82-b281-4cac-8c37-e2df7e405409" />

<img width="752" height="435" alt="Screenshot 2026-04-05 180722" src="https://github.com/user-attachments/assets/cd12d5ef-c0ef-47fb-a925-95baf2805bc2" />

<img width="799" height="207" alt="Screenshot 2026-04-05 180825" src="https://github.com/user-attachments/assets/8ef440df-c845-46bd-bfab-87d1182d2622" />



# 🌱 Carbon Pulse — Personal Carbon Footprint Tracker

A full-stack web application that helps users track, analyze, and reduce their daily carbon footprint across multiple lifestyle categories.  

Built with a modular API-driven architecture, Carbon Pulse provides real-time insights, historical tracking, and comparative analytics against national and global averages.

---

## 🚀 Features

### 👤 User System
- User registration & login (email-based)
- Persistent user profiles
- Personalized carbon tracking

### 📊 Carbon Tracking
- Track emissions across:
  - 🚗 Transport
  - 🍽 Food
  - 💻 Digital Usage
  - ⚡ Home Energy
  - 🛍 Shopping
- Real-time carbon calculation
- Session-based + persistent logging

### 📈 Dashboard & Analytics
- Daily carbon footprint tracking
- Category-wise emission breakdown
- Comparison with:
  - 🇮🇳 India average (5.21 kg/day)
  - 🌍 Global average (11.97 kg/day)
- Visualizations using charts:
  - Bar charts
  - Line graphs
  - Doughnut charts

### 🕒 History Tracking
- Complete user activity history
- Timestamped logs
- Total emissions calculation

### 🌳 Sustainability Insights
- Tree offset estimation
- Top emission category detection
- Personalized recommendations

---

## 🧠 Tech Stack

### Frontend
- React (via CDN)
- Tailwind CSS
- Chart.js (data visualization)

### Backend
- Flask (Python)
- REST API architecture
- Flask-CORS

### Database
- SQLite (`carbon_tracker.db`)
- Tables:
  - `users`
  - `carbon_logs`

### Data Layer
- JSON-based emission factors
---

🚀 Features
👤 User Authentication & Profiles
Register and log in using email, with persistent user profiles and personalized tracking.
📊 Multi-Category Carbon Tracking
Calculate emissions across key lifestyle categories: Transport, Food, Digital Usage, Home Energy, and Shopping.
⚡ Real-Time Carbon Calculation
Instant emission calculations using dynamic emission factors via a RESTful Flask API.
🗃 Persistent Data Storage
Stores user data and carbon logs using SQLite for long-term tracking and retrieval.
🕒 Activity History Tracking
View complete history of carbon entries with timestamps and aggregated totals.
📈 Interactive Dashboard
Visualize carbon footprint through charts including category breakdown, trends, and distribution.
🌍 Comparative Analytics
Compare personal carbon footprint with India’s average (5.21 kg/day) and global average (11.97 kg/day).
🌳 Sustainability Insights
Estimate number of trees required to offset emissions and identify highest contributing category.
🔄 Session + Persistent Logging
Supports both real-time session tracking and permanent storage in database.
🧩 Modular API Architecture
Separate endpoints for each category, enabling scalability and easy feature expansion.
📦 Data-Driven Design
Emission factors stored in JSON for flexibility and easy updates without modifying code.
🖥 Modern Interactive UI
Built with React and Tailwind CSS, featuring responsive design and smooth user experience.
🧠 Normalized Carbon Modeling
Converts diverse inputs (km, meals, kWh, etc.) into a unified daily carbon footprint metric, including lifespan-based calculations for shopping.



## 🧩 Project Overview

Your **carbon footprint** is the total greenhouse gas emissions caused by your daily lifestyle.  
This app turns everyday activities (travel, food, power, purchases) into measurable CO₂ values, helping you:
- Understand which habits have the most environmental impact 🌱  
- Track improvements over time 📊  
- Make informed, sustainable choices 🌞
- Compares users' average with the global and Indian Average

---

Formula -
Emissions = Activity Amount × Emission Factor
Daily CO₂ = (Total CO₂ of Item) ÷ (Expected Lifetime in Days)

**Total Daily CO₂ = Sum of all categories**
Annual CO₂ = (Daily Total × 365) / 1000  [in tonnes]

💡 Insights You Get
🌍 Your total daily & yearly CO₂ emissions
📊 Category-wise breakdown (transport, food, power, etc.)
🎯 How your lifestyle compares to global sustainability targets (≈2 tonnes CO₂/year)
📈 Track your progress over time
💬 Personalized tips to reduce emissions


