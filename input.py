
VALID_SYMPTOMS = {
    "fever", "cough", "shortness of breath", "chest pain",
    "headache", "fatigue", "vomiting", "dizziness",
    "abdominal pain", "rash"
}

def get_valid_symptoms(user_input):
    symptoms = [s.strip().lower() for s in user_input.split(",")]
    
    filtered = [s for s in symptoms if s in VALID_SYMPTOMS]
    
    return filtered