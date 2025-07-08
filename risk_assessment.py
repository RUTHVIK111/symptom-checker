
SYMPTOM_RISK = {
    "fever": 1,
    "cough": 1,
    "fatigue": 1,
    "headache": 1,
    "vomiting": 2,
    "dizziness": 2,
    "abdominal pain": 2,
    "rash": 1,
    "shortness of breath": 3,
    "chest pain": 3
}

def calculate_risk(symptoms):
    total_score = 0
    for symptom in symptoms:
        total_score += SYMPTOM_RISK.get(symptom, 0)
    return total_score