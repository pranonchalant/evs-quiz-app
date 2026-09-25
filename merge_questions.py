import json

with open("/Users/pran/devjams26/questions.json") as f:
    pdf_qs = json.load(f)

with open("/Users/pran/devjams26/website_mcqs.json") as f:
    site_qs = json.load(f)

# Build a unified list where each question has a clean id and source tags
master_list = []
seen_questions = set()
curr_id = 1

# 1. First add the 63 official website questions so they can be taken as an exact replica test
for q in site_qs:
    q_norm = q["question"].strip().lower()
    item = {
        "id": curr_id,
        "question": q["question"],
        "options": q["options"],
        "correctAnswer": q["correctAnswer"],
        "explanation": q["explanation"],
        "category": q["category"],
        "isWebsiteOfficial63": q.get("isOfficial63", False),
        "isWebsiteGenerated": True,
        "isTop30": False
    }
    master_list.append(item)
    seen_questions.add(q_norm)
    curr_id += 1

# 2. Add PDF questions (tagging duplicates if any)
for q in pdf_qs:
    q_norm = q["question"].strip().lower()
    if q_norm in seen_questions:
        continue
    item = {
        "id": curr_id,
        "question": q["question"],
        "options": q["options"],
        "correctAnswer": q["correctAnswer"],
        "explanation": q["explanation"],
        "category": q["category"],
        "isWebsiteOfficial63": False,
        "isWebsiteGenerated": False,
        "isTop30": q.get("isTop30", False)
    }
    master_list.append(item)
    seen_questions.add(q_norm)
    curr_id += 1

with open("/Users/pran/devjams26/master_questions.json", "w") as f:
    json.dump(master_list, f, indent=2)

print(f"Master question list created with {len(master_list)} total questions.")
print(f"Website Official 63: {sum(1 for q in master_list if q['isWebsiteOfficial63'])}")
print(f"Website Generated: {sum(1 for q in master_list if q['isWebsiteGenerated'])}")
print(f"Top 30 High Yield: {sum(1 for q in master_list if q['isTop30'])}")
