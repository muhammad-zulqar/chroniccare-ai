DISEASE_FORMS = {

    "heart_disease": {

    "title": "Heart Health Assessment",

    "description": (
        "Answer a few simple questions and provide basic "
        "health information for an AI-based heart health assessment."
    ),

    "fields": [

        {
            "name": "age",
            "label": "What is your age?",
            "type": "number",
            "placeholder": "Enter your age",
            "min": "1",
            "max": "120",
            "help": "Enter your current age.",
        },

        {
            "name": "sex",
            "label": "What is your sex?",
            "type": "select",
            "options": [
                ("1", "Male"),
                ("0", "Female"),
            ],
            "help": "Select the option that applies to you.",
        },

        {
            "name": "cp",
            "label": "What type of chest discomfort do you usually experience?",
            "type": "select",
            "options": [
    ("1", "Typical chest pain"),
    ("2", "Atypical chest pain"),
    ("3", "Non-anginal chest discomfort"),
    ("4", "No chest pain / asymptomatic"),
],
            "help": (
                "Choose the option that best describes "
                "your usual chest discomfort."
            ),
        },

        {
            "name": "trestbps",
            "label": "What is your resting blood pressure?",
            "type": "number",
            "placeholder": "e.g. 120",
            "min": "50",
            "max": "250",
            "help": (
                "Enter your resting blood-pressure reading "
                "from a recent health check."
            ),
        },

        {
            "name": "chol",
            "label": "What is your cholesterol level?",
            "type": "number",
            "placeholder": "From your blood-test report",
            "min": "50",
            "max": "700",
            "help": (
                "Enter the cholesterol value from your "
                "recent blood-test report."
            ),
        },

        {
            "name": "fbs",
            "label": "Has a blood test shown that your fasting blood sugar is high?",
            "type": "select",
            "options": [
                ("1", "Yes"),
                ("0", "No"),
            ],
            "help": (
                "Choose Yes if you have been told that "
                "your fasting blood sugar is above the normal range."
            ),
        },

        {
            "name": "restecg",
            "label": "What did your resting ECG report show?",
            "type": "select",
            "options": [
                ("0", "Normal"),
                ("1", "ST-T wave abnormality"),
                ("2", "Left ventricular hypertrophy"),
            ],
            "help": (
                "Use the result from your ECG report. "
                "Choose Normal if your report says normal."
            ),
        },

        {
            "name": "thalach",
            "label": "What was your highest heart rate during your test?",
            "type": "number",
            "placeholder": "e.g. 150",
            "min": "50",
            "max": "250",
            "help": (
                "Enter the highest heart-rate value recorded "
                "during your health examination or exercise test."
            ),
        },

        {
            "name": "exang",
            "label": "Did exercise cause chest discomfort during your test?",
            "type": "select",
            "options": [
                ("1", "Yes"),
                ("0", "No"),
            ],
            "help": (
                "Choose Yes if physical activity or exercise "
                "caused chest discomfort during the test."
            ),
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
        "label": "What is your age?",
        "type": "number",
        "placeholder": "Enter your age",
        "min": "1",
        "max": "120",
        "help": "Enter your current age.",
    },

    {
        "name": "gender",
        "label": "What is your gender?",
        "type": "select",
        "options": [
            ("Male", "Male"),
            ("Female", "Female"),
        ],
        "help": "Select the option that applies to you.",
    },

    {
        "name": "polyuria",
        "label": "Do you urinate more often than usual?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Choose Yes if you have noticed unusually frequent urination.",
    },

    {
        "name": "polydipsia",
        "label": "Do you often feel unusually thirsty?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Choose Yes if you experience excessive thirst.",
    },

    {
        "name": "sudden_weight_loss",
        "label": "Have you experienced unexplained weight loss?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Choose Yes if you have lost weight without intentionally trying.",
    },

    {
        "name": "weakness",
        "label": "Do you often feel unusually weak or tired?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Choose Yes if you frequently experience unusual weakness.",
    },

    {
        "name": "polyphagia",
        "label": "Do you feel unusually hungry more often?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Choose Yes if you have noticed increased hunger.",
    },

    {
        "name": "visual_blurring",
        "label": "Do you experience blurred vision?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Choose Yes if your vision sometimes appears unusually blurred.",
    },

    {
        "name": "obesity",
        "label": "Do you consider yourself significantly overweight?",
        "type": "select",
        "options": [
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        "help": "Use your usual health assessment or clinician guidance when answering.",
    },
        ],
    },


    # ========================================================
    # KIDNEY
    # ========================================================
"kidney_disease": {

    "title": "Kidney Health Assessment",

    "description": (
        "Answer a few simple health questions and, where available, "
        "enter values from your recent blood or medical report."
    ),

    "fields": [

        {
            "name": "age",
            "label": "What is your age?",
            "type": "number",
            "placeholder": "Enter your age",
            "min": "1",
            "max": "120",
            "help": "Enter your current age.",
        },

        {
            "name": "bp",
            "label": "What is your blood pressure reading?",
            "type": "number",
            "placeholder": "e.g. 80",
            "help": (
                "Enter the blood-pressure value recorded during "
                "your recent health check."
            ),
        },

        {
            "name": "bgr",
            "label": "What is your blood glucose level?",
            "type": "number",
            "placeholder": "From your blood-test report",
            "help": (
                "Enter the blood glucose value shown on your "
                "recent laboratory report."
            ),
        },

        {
            "name": "bu",
            "label": "What is your blood urea level?",
            "type": "number",
            "placeholder": "From your blood-test report",
            "help": (
                "Enter the blood urea value shown on your "
                "recent laboratory report."
            ),
        },

        {
            "name": "sc",
            "label": "What is your serum creatinine level?",
            "type": "number",
            "step": "0.1",
            "placeholder": "From your blood-test report",
            "help": (
                "Enter the serum creatinine value from your "
                "recent laboratory report."
            ),
        },

        {
            "name": "hemo",
            "label": "What is your hemoglobin level?",
            "type": "number",
            "step": "0.1",
            "placeholder": "From your blood-test report",
            "help": (
                "Enter the hemoglobin value from your "
                "recent laboratory report."
            ),
        },

        {
            "name": "htn",
            "label": "Have you been told that you have high blood pressure?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if a healthcare professional has "
                "told you that you have hypertension."
            ),
        },

        {
            "name": "dm",
            "label": "Have you been told that you have diabetes?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have been diagnosed with diabetes."
            ),
        },

        {
            "name": "appet",
            "label": "How would you describe your appetite?",
            "type": "select",
            "options": [
                ("good", "Good"),
                ("poor", "Poor"),
            ],
            "help": (
                "Choose the option that best describes your usual appetite."
            ),
        },

        {
            "name": "pe",
            "label": "Have you noticed swelling in your feet, ankles, or legs?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed unusual swelling "
                "in your lower legs or feet."
            ),
        },

    ],
},

    # ========================================================
    # BREAST CANCER
    # ========================================================

    "breast_cancer": {

    "title": "Breast Health Screening",

    "description": (
        "Answer a few simple questions about changes you may have "
        "noticed. This screening does not diagnose breast cancer."
    ),

    "fields": [

        {
            "name": "new_lump",
            "label": "Have you noticed a new lump or thickening in your breast?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed a new or unusual "
                "lump or thickened area."
            ),
        },

        {
            "name": "size_shape_change",
            "label": "Have you noticed a change in the size or shape of your breast?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed a new or unusual "
                "change in size or shape."
            ),
        },

        {
            "name": "skin_change",
            "label": "Have you noticed unusual changes in the skin of your breast?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed an unusual change "
                "in the appearance or texture of the skin."
            ),
        },

        {
            "name": "nipple_change",
            "label": "Have you noticed a new change in the appearance or position of a nipple?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed a new or unusual "
                "change in a nipple."
            ),
        },

        {
            "name": "nipple_discharge",
            "label": "Have you noticed unusual discharge from a nipple?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed unexpected "
                "nipple discharge."
            ),
        },

        {
            "name": "persistent_pain",
            "label": "Have you had persistent pain or discomfort in one breast?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if the pain or discomfort has been "
                "persistent or unusual for you."
            ),
        },

        {
            "name": "underarm_change",
            "label": "Have you noticed a new lump or swelling near your armpit?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if you have noticed a new or unusual "
                "lump or swelling near the armpit."
            ),
        },

        {
            "name": "doctor_concern",
            "label": "Has a healthcare professional ever asked you to investigate a breast change?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": (
                "Choose Yes if a healthcare professional has "
                "recommended further evaluation."
            ),
        },

    ],
},

    # ========================================================
    # LIVER
    # ========================================================

    "liver_disease": {

    "title": "Liver Health Screening",

    "description": (
        "Answer simple questions about symptoms and health history. "
        "This screening uses a machine-learning model trained on "
        "patient health information."
    ),

    "fields": [

        {
            "name": "Age",
            "label": "What is your age?",
            "type": "number",
            "placeholder": "Enter your age",
            "min": "1",
            "max": "120",
            "help": "Enter your current age.",
        },

        {
            "name": "Sex",
            "label": "What is your sex?",
            "type": "select",
            "options": [
                ("male", "Male"),
                ("female", "Female"),
            ],
            "help": "Select the option that applies to you.",
        },

        {
            "name": "Fatigue",
            "label": "Have you been feeling unusually tired recently?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Choose Yes if you have been experiencing unusual tiredness.",
        },

        {
            "name": "Malaise",
            "label": "Have you been feeling generally unwell?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Choose Yes if you have recently felt generally unwell.",
        },

        {
            "name": "Anorexia",
            "label": "Has your appetite become unusually poor?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Choose Yes if you have noticed a significant loss of appetite.",
        },

        {
            "name": "Liver Big",
            "label": "Has a healthcare professional ever told you that your liver is enlarged?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Do not try to determine this yourself; use a previous medical assessment.",
        },

        {
            "name": "Spleen Palpable",
            "label": "Has a healthcare professional ever told you that your spleen is enlarged?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Use a previous medical examination if you have one.",
        },

        {
            "name": "Ascites",
            "label": "Have you ever been told that you have unusual fluid buildup or swelling in your abdomen?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Choose Yes if this has been identified during a medical assessment.",
        },

        {
            "name": "Spiders",
            "label": "Has a healthcare professional ever pointed out unusual spider-like blood vessels on your skin?",
            "type": "select",
            "options": [
                ("yes", "Yes"),
                ("no", "No"),
            ],
            "help": "Use Yes only if this has been identified by a healthcare professional.",
        },

    ],
},

}