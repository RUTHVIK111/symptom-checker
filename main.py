
from input import get_valid_symptoms
from risk_assessment import calculate_risk
from care_recommendation import get_care_recommendation

def main():
    print("👨‍⚕️ Medical Symptom Checker")
    print("Enter your symptoms separated by commas (fever, cough, shortness of breath, chest pain, headache, fatigue,vomiting , dizziness, abdominal pain, rash):")
    
    user_input = input("Your symptoms: ")
    symptoms = get_valid_symptoms(user_input)
    
    if not symptoms:
        print("⚠️ No valid symptoms entered. Please try again.")
        return

    print(f"\n✅ Recognized symptoms: {', '.join(symptoms)}")
    
    risk_score = calculate_risk(symptoms)
    recommendation = get_care_recommendation(risk_score)
    
    print(f"\n📊 Risk Score: {risk_score}")
    print(f"\n📌 Recommendation: {recommendation}")

if __name__ == "__main__":
    main()