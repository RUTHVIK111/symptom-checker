
def get_care_recommendation(score):
    if score >= 6:
        return "🔴 High Risk: Seek emergency medical attention immediately."
    elif score >= 3:
        return "🟠 Moderate Risk: Consult a doctor within 24 hours."
    elif score > 0:
        return "🟢 Low Risk: Monitor symptoms and use self-care."
    else:
        return "✅ No significant symptoms detected. No action needed."