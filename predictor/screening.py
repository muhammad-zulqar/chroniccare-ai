BREAST_SCREENING_FIELDS = [
    "new_lump",
    "size_shape_change",
    "skin_change",
    "nipple_change",
    "nipple_discharge",
    "persistent_pain",
    "underarm_change",
    "doctor_concern",
]


def screen_breast_health(data):

    yes_answers = []

    for field in BREAST_SCREENING_FIELDS:

        value = str(
            data.get(field, "")
        ).strip().lower()

        if value == "yes":
            yes_answers.append(field)

    return {
        "attention_recommended": len(yes_answers) > 0,
        "yes_count": len(yes_answers),
        "total_questions": len(BREAST_SCREENING_FIELDS),
        "flagged_fields": yes_answers,
    }