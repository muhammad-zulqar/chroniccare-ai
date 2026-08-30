DISEASE_FORMS = {

    "heart_disease": {

        "title": "Heart Disease Risk Assessment",

        "description": "Provide the cardiovascular measurements required by our trained model.",

        "fields": [

            {
                "name": "age",
                "label": "Age",
                "type": "number",
                "placeholder": "e.g. 45",
                "min": "1",
                "max": "120",
            },

            {
                "name": "sex",
                "label": "Sex",
                "type": "select",
                "options": [
                    ("1", "Male"),
                    ("0", "Female"),
                ],
            },

            {
                "name": "cp",
                "label": "Chest Pain Type",
                "type": "select",
                "options": [
                    ("0", "Typical angina"),
                    ("1", "Atypical angina"),
                    ("2", "Non-anginal pain"),
                    ("3", "Asymptomatic"),
                ],
            },

            {
                "name": "trestbps",
                "label": "Resting Blood Pressure",
                "type": "number",
                "placeholder": "e.g. 120",
                "min": "50",
                "max": "250",
            },

            {
                "name": "chol",
                "label": "Serum Cholesterol",
                "type": "number",
                "placeholder": "e.g. 200",
                "min": "50",
                "max": "700",
            },

            {
                "name": "fbs",
                "label": "Fasting Blood Sugar > 120 mg/dl",
                "type": "select",
                "options": [
                    ("1", "Yes"),
                    ("0", "No"),
                ],
            },

            {
                "name": "restecg",
                "label": "Resting ECG",
                "type": "select",
                "options": [
                    ("0", "Normal"),
                    ("1", "ST-T wave abnormality"),
                    ("2", "Left ventricular hypertrophy"),
                ],
            },

            {
                "name": "thalach",
                "label": "Maximum Heart Rate",
                "type": "number",
                "placeholder": "e.g. 150",
                "min": "50",
                "max": "250",
            },

            {
                "name": "exang",
                "label": "Exercise-Induced Angina",
                "type": "select",
                "options": [
                    ("1", "Yes"),
                    ("0", "No"),
                ],
            },

            {
                "name": "oldpeak",
                "label": "ST Depression",
                "type": "number",
                "placeholder": "e.g. 1.0",
                "step": "0.1",
            },

            {
                "name": "slope",
                "label": "ST Segment Slope",
                "type": "select",
                "options": [
                    ("0", "Upsloping"),
                    ("1", "Flat"),
                    ("2", "Downsloping"),
                ],
            },

            {
                "name": "ca",
                "label": "Major Vessels",
                "type": "select",
                "options": [
                    ("0", "0"),
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                ],
            },

            {
                "name": "thal",
                "label": "Thalassemia",
                "type": "select",
                "options": [
                    ("0", "Normal"),
                    ("1", "Fixed defect"),
                    ("2", "Reversible defect"),
                ],
            },
        ],
    },


    # ========================================================
    # DIABETES
    # ========================================================

    "diabetes": {

        "title": "Diabetes Risk Assessment",

        "description": "Answer the following questions based on the information requested by the trained model.",

        "fields": [

            {
                "name": "age",
                "label": "Age",
                "type": "number",
                "placeholder": "e.g. 35",
                "min": "1",
                "max": "120",
            },

            {
                "name": "gender",
                "label": "Gender",
                "type": "select",
                "options": [
                    ("Male", "Male"),
                    ("Female", "Female"),
                ],
            },

            {
                "name": "polyuria",
                "label": "Frequent Urination",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "polydipsia",
                "label": "Excessive Thirst",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "sudden_weight_loss",
                "label": "Sudden Weight Loss",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "weakness",
                "label": "Weakness",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "polyphagia",
                "label": "Excessive Hunger",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "genital_thrush",
                "label": "Genital Thrush",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "visual_blurring",
                "label": "Visual Blurring",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "itching",
                "label": "Itching",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "irritability",
                "label": "Irritability",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "delayed_healing",
                "label": "Delayed Healing",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "partial_paresis",
                "label": "Partial Paresis",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "muscle_stiffness",
                "label": "Muscle Stiffness",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "alopecia",
                "label": "Hair Loss",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },

            {
                "name": "obesity",
                "label": "Obesity",
                "type": "select",
                "options": [
                    ("Yes", "Yes"),
                    ("No", "No"),
                ],
            },
        ],
    },


    # ========================================================
    # KIDNEY
    # ========================================================

    "kidney_disease": {

        "title": "Chronic Kidney Disease Risk Assessment",

        "description": "Provide the measurements required by the kidney disease model.",

        "fields": [

            {
                "name": "age",
                "label": "Age",
                "type": "number",
                "min": "1",
                "max": "120",
            },

            {
                "name": "bp",
                "label": "Blood Pressure",
                "type": "number",
                "placeholder": "e.g. 80",
            },

            {
                "name": "sg",
                "label": "Specific Gravity",
                "type": "number",
                "step": "0.001",
                "placeholder": "e.g. 1.020",
            },

            {
                "name": "al",
                "label": "Albumin",
                "type": "number",
                "min": "0",
                "max": "5",
            },

            {
                "name": "su",
                "label": "Sugar",
                "type": "number",
                "min": "0",
                "max": "5",
            },

            {
                "name": "rbc",
                "label": "Red Blood Cells",
                "type": "select",
                "options": [
                    ("normal", "Normal"),
                    ("abnormal", "Abnormal"),
                ],
            },

            {
                "name": "pc",
                "label": "Pus Cell",
                "type": "select",
                "options": [
                    ("normal", "Normal"),
                    ("abnormal", "Abnormal"),
                ],
            },

            {
                "name": "pcc",
                "label": "Pus Cell Clumps",
                "type": "select",
                "options": [
                    ("present", "Present"),
                    ("notpresent", "Not Present"),
                ],
            },

            {
                "name": "ba",
                "label": "Bacteria",
                "type": "select",
                "options": [
                    ("present", "Present"),
                    ("notpresent", "Not Present"),
                ],
            },

            {
                "name": "bgr",
                "label": "Blood Glucose Random",
                "type": "number",
            },

            {
                "name": "bu",
                "label": "Blood Urea",
                "type": "number",
            },

            {
                "name": "sc",
                "label": "Serum Creatinine",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "sod",
                "label": "Sodium",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "pot",
                "label": "Potassium",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "hemo",
                "label": "Hemoglobin",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "pcv",
                "label": "Packed Cell Volume",
                "type": "number",
            },

            {
                "name": "wbcc",
                "label": "White Blood Cell Count",
                "type": "number",
            },

            {
                "name": "rbcc",
                "label": "Red Blood Cell Count",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "htn",
                "label": "Hypertension",
                "type": "select",
                "options": [
                    ("yes", "Yes"),
                    ("no", "No"),
                ],
            },

            {
                "name": "dm",
                "label": "Diabetes Mellitus",
                "type": "select",
                "options": [
                    ("yes", "Yes"),
                    ("no", "No"),
                ],
            },

            {
                "name": "cad",
                "label": "Coronary Artery Disease",
                "type": "select",
                "options": [
                    ("yes", "Yes"),
                    ("no", "No"),
                ],
            },

            {
                "name": "appet",
                "label": "Appetite",
                "type": "select",
                "options": [
                    ("good", "Good"),
                    ("poor", "Poor"),
                ],
            },

            {
                "name": "pe",
                "label": "Pedal Edema",
                "type": "select",
                "options": [
                    ("yes", "Yes"),
                    ("no", "No"),
                ],
            },

            {
                "name": "ane",
                "label": "Anemia",
                "type": "select",
                "options": [
                    ("yes", "Yes"),
                    ("no", "No"),
                ],
            },
        ],
    },


    # ========================================================
    # BREAST CANCER
    # ========================================================

    "breast_cancer": {

        "title": "Breast Cancer Risk Assessment",

        "description": "Enter the tumor measurement values required by the trained classification model.",

        "fields": [

            {
                "name": "radius1",
                "label": "Radius",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "texture1",
                "label": "Texture",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "perimeter1",
                "label": "Perimeter",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "area1",
                "label": "Area",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "smoothness1",
                "label": "Smoothness",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "compactness1",
                "label": "Compactness",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "concavity1",
                "label": "Concavity",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "concave_points1",
                "label": "Concave Points",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "symmetry1",
                "label": "Symmetry",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "fractal_dimension1",
                "label": "Fractal Dimension",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "radius2",
                "label": "Radius SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "texture2",
                "label": "Texture SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "perimeter2",
                "label": "Perimeter SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "area2",
                "label": "Area SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "smoothness2",
                "label": "Smoothness SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "compactness2",
                "label": "Compactness SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "concavity2",
                "label": "Concavity SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "concave_points2",
                "label": "Concave Points SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "symmetry2",
                "label": "Symmetry SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "fractal_dimension2",
                "label": "Fractal Dimension SE",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "radius3",
                "label": "Worst Radius",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "texture3",
                "label": "Worst Texture",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "perimeter3",
                "label": "Worst Perimeter",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "area3",
                "label": "Worst Area",
                "type": "number",
                "step": "0.0001",
            },

            {
                "name": "smoothness3",
                "label": "Worst Smoothness",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "compactness3",
                "label": "Worst Compactness",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "concavity3",
                "label": "Worst Concavity",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "concave_points3",
                "label": "Worst Concave Points",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "symmetry3",
                "label": "Worst Symmetry",
                "type": "number",
                "step": "0.000001",
            },

            {
                "name": "fractal_dimension3",
                "label": "Worst Fractal Dimension",
                "type": "number",
                "step": "0.000001",
            },
        ],
    },


    # ========================================================
    # LIVER
    # ========================================================

    "liver_disease": {

        "title": "Liver Disease Risk Assessment",

        "description": "Enter the laboratory measurements required by the trained model.",

        "fields": [

            {
                "name": "age",
                "label": "Age",
                "type": "number",
                "min": "1",
                "max": "120",
            },

            {
                "name": "gender",
                "label": "Gender",
                "type": "select",
                "options": [
                    ("Male", "Male"),
                    ("Female", "Female"),
                ],
            },

            {
                "name": "tb",
                "label": "Total Bilirubin",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "db",
                "label": "Direct Bilirubin",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "alkphos",
                "label": "Alkaline Phosphotase",
                "type": "number",
            },

            {
                "name": "sgpt",
                "label": "SGPT",
                "type": "number",
            },

            {
                "name": "sgot",
                "label": "SGOT",
                "type": "number",
            },

            {
                "name": "tp",
                "label": "Total Protein",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "alb",
                "label": "Albumin",
                "type": "number",
                "step": "0.1",
            },

            {
                "name": "a/g_ratio",
                "label": "Albumin / Globulin Ratio",
                "type": "number",
                "step": "0.01",
            },
        ],
    },
}