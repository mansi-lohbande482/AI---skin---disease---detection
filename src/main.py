print("AI Skin Disease Detection System Started")

def preprocess_image(image_path):
    print("Preprocessing image:", image_path)

def predict_disease(image):
    print("Predicting disease...")
    return "Eczema"

if __name__ == "__main__":
    preprocess_image("sample.jpg")
    result = predict_disease("sample.jpg")
    print("Prediction:", result)
