import json

with open("master_questions.json") as f:
    existing_list = json.load(f)

with open("vit_fat_questions.json") as f:
    fat_list = json.load(f)

# Re-assign clean sequential IDs
master_list = []
curr_id = 1

# First add the 161 VIT Vellore FAT questions as premier exam pack
for q in fat_list:
    item = {
        "id": curr_id,
        "question": q["question"],
        "options": q["options"],
        "correctAnswer": q["correctAnswer"],
        "explanation": q["explanation"],
        "category": q["category"],
        "section": q["section"],
        "isFatExam": True,
        "isWebsiteOfficial63": False,
        "isWebsiteGenerated": False,
        "isTop30": False
    }
    master_list.append(item)
    curr_id += 1

# Add all existing questions
for q in existing_list:
    item = {
        "id": curr_id,
        "question": q["question"],
        "options": q["options"],
        "correctAnswer": q["correctAnswer"],
        "explanation": q["explanation"],
        "category": q["category"],
        "section": q.get("section", "General EVS"),
        "isFatExam": False,
        "isWebsiteOfficial63": q.get("isWebsiteOfficial63", False),
        "isWebsiteGenerated": q.get("isWebsiteGenerated", False),
        "isTop30": q.get("isTop30", False)
    }
    master_list.append(item)
    curr_id += 1

with open("master_questions.json", "w") as f:
    json.dump(master_list, f, indent=2)

print(f"Master question list compiled with {len(master_list)} total questions.")
print(f"VIT Vellore FAT Questions: {sum(1 for q in master_list if q.get('isFatExam'))}")
print(f"Website Official 63: {sum(1 for q in master_list if q.get('isWebsiteOfficial63'))}")
