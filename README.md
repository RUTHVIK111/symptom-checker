# 🩺 Medical Symptom Checker and Triage System

## 📌 Project Overview

This project is an AI-powered **rule-based symptom checker** that takes patient symptom inputs and provides a **preliminary risk assessment** along with appropriate **care recommendations**. It is designed as a modular, interpretable, and lightweight diagnostic tool suitable for prototypes or educational applications.

---

## 🎯 Problem Statement

**Goal:**  
Build an AI system that:
- Accepts symptom input from users
- Analyzes severity and combinations of symptoms
- Outputs a risk level (low, moderate, high)
- Recommends a course of action (emergency care, doctor consultation, or self-care)

---

## 🧠 Features and Skills Demonstrated

- ✅ Rule-based decision logic using symptom severity scoring
- ✅ Modular codebase: input validation, risk assessment, care recommendation
- ✅ Critical thinking for triage decisions: balances sensitivity vs specificity
- ✅ Clear architecture and flow from user input to medical advice
- ✅ Ready for extension to machine learning or NLP

---

## ⚙️ How It Works

### 💡 System Flow:
### 🚦 Risk Levels:
| Risk Score | Risk Level   | Recommendation                                |
|------------|--------------|-----------------------------------------------|
| 6 or more  | 🔴 High      | Seek emergency care immediately               |
| 3 - 5      | 🟠 Moderate  | Consult a doctor within 24 hours              |
| 1 - 2      | 🟢 Low       | Monitor symptoms and use self-care            |
| 0          | ✅ None      | No significant symptoms detected              |
