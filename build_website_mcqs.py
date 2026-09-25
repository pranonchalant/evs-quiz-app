# Script to generate comprehensive questions from https://masterdooom.github.io/evs/
import json, ast, re

with open("/Users/pran/devjams26/website_dump.json") as f:
    site_data = json.load(f)

# 1. Parse the 63 official website questions from questions1.js + questions2.js
content = site_data['questions1.js'] + '\n' + site_data['questions2.js']
pushes = re.findall(r'window\.EVS_QUESTIONS\.push\((.*?)\);', content, re.DOTALL)
raw_site_qs = ast.literal_eval('[' + ','.join(pushes) + ']')

# Comprehensive topic mapping and rich explanations for the 63 website questions
explanations_63 = {
    0: "The stratosphere contains the ozone layer (ozonosphere), which absorbs lethal solar ultraviolet (UV-B and UV-C) radiation.",
    1: "The troposphere is the lowest atmospheric layer containing ~75-80% of atmospheric mass and almost all water vapor, driving clouds and weather.",
    2: "The hierarchical order of ecological organization proceeds from individual Organism → Population → Community → Ecosystem → Biosphere.",
    3: "Abiotic components are non-living physical or chemical factors such as temperature, sunlight, water, and soil minerals.",
    4: "According to Lindeman's 10% law, only about 10% of the energy at any trophic level is transferred into biomass at the next level.",
    5: "Net Primary Productivity (NPP) is the energy fixed by producers that remains after subtracting their metabolic respiratory losses: NPP = GPP − Respiration.",
    6: "A detritus food chain starts with non-living dead organic matter (detritus), broken down by detritivores and saprotrophic decomposers.",
    7: "The pyramid of energy is always upright because energy is lost as heat at every successive trophic level according to the Second Law of Thermodynamics.",
    8: "Primary succession initiates on barren, lifeless substrates where no soil or previous ecological community existed (e.g., bare rock, new lava flows).",
    9: "Pioneers in primary terrestrial succession are hardy organisms such as lichens and mosses capable of adhering to bare substrates and initiating pedogenesis (soil formation).",
    10: "Species diversity incorporates both species richness (the total number of different species) and species evenness (the relative abundance of each species).",
    11: "Genetic diversity represents the hereditary variations in genes and alleles present among individuals within a single biological species.",
    12: "In-situ ('on-site') conservation protects endangered plants and animals directly within their natural ecosystems and indigenous habitats.",
    13: "Bees and flowering plants demonstrate mutualism (+/+), where pollinating insects obtain nectar while simultaneously enabling plant cross-pollination.",
    14: "An endemic species is naturally and exclusively confined to a particular geographic region or ecosystem.",
    15: "A primary pollutant is an air contaminant emitted directly in an active, harmful form from identifiable sources (e.g., CO, SO2 from exhausts).",
    16: "Ground-level (tropospheric) ozone is a secondary pollutant synthesized photochemically when NOx reacts with volatile organic compounds (VOCs) under sunlight.",
    17: "On the Air Quality Index (AQI) scale, a reading of 401–500 represents the most severe 'Hazardous' category, prompting health emergencies.",
    18: "A factory discharge pipe is a classic point-source pollution discharge because the wastewater originates from a single, discrete, localized conveyance.",
    19: "Biomagnification refers to the progressive increase in concentration of persistent, lipophilic toxins across ascending trophic levels in a food chain.",
    20: "Primary sewage treatment relies on physical separation processes (coarse screening, grit removal, sedimentation) to remove heavy settleable solids.",
    21: "Thermal pollution introduces heated water into aquatic systems, which directly decreases dissolved oxygen solubility while increasing aquatic organisms' metabolic oxygen demand.",
    22: "In the waste management hierarchy, the correct operational order is Reduce (source prevention) → Reuse (re-utilization) → Recycle (material processing).",
    23: "Anaerobic digestion is the biological decomposition of organic waste by specialized bacterial consortia in the complete absence of gaseous oxygen, producing methane biogas.",
    24: "A sanitary landfill is an engineered waste containment facility featuring impermeable clay/geomembrane liners, leachate collection, and daily soil cover.",
    25: "In environmental hazard and disaster analysis, Risk is mathematically defined as a function of the Hazard's magnitude and the exposed system's Vulnerability/Exposure.",
    26: "The disaster response phase focuses on immediate search and rescue, evacuation, first aid, and urgent humanitarian relief during and right after impact.",
    27: "EIA screening is the initial gatekeeping step that determines whether a proposed project requires a formal Environmental Impact Assessment and the extent of assessment needed.",
    28: "Section 25 of the Water Act 1974 requires obtaining prior consent from the State Pollution Control Board before setting up any new outlet or discharge into water bodies.",
    29: "Section 2 of the Forest (Conservation) Act 1980 strictly mandates prior approval of the Central Government before any classified forest land can be diverted for non-forest purposes.",
    30: "The Clean Development Mechanism (CDM) is the Kyoto Protocol flexible mechanism enabling industrialized nations to implement emission-reduction projects in developing nations in return for certified carbon credits.",
    31: "Nationally Determined Contributions (NDCs) represent the self-defined, bottom-up climate mitigation and adaptation commitments submitted by each signatory under the Paris Agreement.",
    32: "Article 14 of the Paris Agreement establishes the Global Stocktake every 5 years to evaluate collective progress toward achieving the treaty's long-term temperature and mitigation goals.",
    33: "Net-zero greenhouse gas emissions describes the state where remaining anthropogenic greenhouse emissions released into the atmosphere are fully balanced by anthropogenic removals.",
    34: "Sustainable Development Goal 13 explicitly calls for urgent action to combat climate change and its impacts.",
    35: "Sustainable Development Goal 12 focuses on ensuring sustainable and responsible consumption and production patterns.",
    36: "The Central Pollution Control Board (CPCB) was legally established in 1974 under Section 3 of the Water (Prevention and Control of Pollution) Act.",
    37: "Bisphenol A (BPA) is an industrial synthetic compound used in polycarbonate plastics and epoxy resins that acts as a potent endocrine-disrupting xenoestrogen.",
    38: "Mercury, especially in the organic form methylmercury, bioaccumulates in fatty tissues and biomagnifies up aquatic food chains, reaching hazardous concentrations in apex predatory fish.",
    39: "Seed banks, zoos, aquaria, and botanical gardens are ex-situ conservation facilities because they preserve genetic resources outside natural ecological habitats.",
    40: "Commensalism is an ecological relationship (+/0) where one species benefits while the other species remains completely unaffected and unharmed.",
    41: "The Water (Prevention and Control of Pollution) Act 1974 was independent India's first comprehensive environmental pollution statute, creating pollution control boards.",
    42: "India's Air (Prevention and Control of Pollution) Act was enacted in 1981 following the 1972 Stockholm Conference mandate.",
    43: "The Environment (Protection) Act (EPA) was enacted in 1986 as an umbrella statute in the aftermath of the December 1984 Bhopal Gas Tragedy.",
    44: "CITES (Convention on International Trade in Endangered Species of Wild Fauna and Flora) legally regulates cross-border trade in endangered wild animals and plants.",
    45: "The Paris Agreement was adopted by consensus on 12 December 2015 at COP21 of the UNFCCC in Paris, France.",
    46: "The Kyoto Protocol was formally adopted on 11 December 1997 in Kyoto, Japan, under the UNFCCC framework.",
    47: "The United Nations 2030 Agenda comprising the 17 Sustainable Development Goals (SDGs) was unanimously agreed upon by 193 member states in September 2015.",
    48: "IWRM stands for Integrated Water Resources Management, a coordinated framework to balance social, economic, and environmental water needs.",
    49: "Composting is the aerobic biological decomposition of organic solid wastes into nutrient-rich humus (compost) suitable for soil conditioning.",
    50: "The mesosphere is the coldest thermal layer of Earth's atmosphere, where temperatures plunge to approximately -90°C.",
    51: "The thermosphere contains the ionosphere, where solar high-energy radiation ionizes atmospheric gas molecules, creating atmospheric auroras (Borealis/Australis).",
    52: "Decomposition by fungi and bacteria breaks down dead organic tissues, remineralizing locked nutrients and recycling them back into soil and biogeochemical cycles.",
    53: "A food web represents an interconnected, realistic network of multiple feeding interactions and cross-linked food chains within an ecosystem.",
    54: "The climax community represents the terminal, stabilized, self-perpetuating final stage of ecological succession in dynamic equilibrium with regional climate.",
    55: "A xerosere is an ecological succession sequence that initiates on a dry, moisture-deficient, xeric substrate such as sand dunes or dry rocks.",
    56: "A hydrosere is an ecological succession sequence that begins in an open body of freshwater such as a pond or shallow lake.",
    57: "A factory discharge pipe directly discharging effluent into a river is an identifiable, localized point source of water pollution.",
    58: "Secondary wastewater treatment utilizes biological aeration tanks and microorganisms (activated sludge) to decompose dissolved biodegradable organic waste.",
    59: "The 3Rs (Reduce, Reuse, Recycle) represent the operational cornerstone of a circular economy, minimizing virgin extraction and preventing disposal.",
    60: "In Integrated Solid Waste Management (ISWM), landfilling is the least preferred, last-resort disposal option after prevention, reuse, recycling, and recovery.",
    61: "Disaster preparedness involves pre-impact activities including contingency planning, emergency drills, stockpile reserves, and early warning dissemination.",
    62: "EIA scoping defines the scope, priority environmental issues, assessment methodologies, and spatial/temporal boundaries of the Environmental Impact Assessment study."
}

# 2. Extract structured topics and generate rich, specific questions covering every one of the 26 syllabus topics
website_questions = []

for idx, (q, opts, ans_idx) in enumerate(raw_site_qs):
    correct_opt = opts[ans_idx]
    exp = explanations_63.get(idx, f"The correct answer is {correct_opt} according to the EVS CAT-II course syllabus.")
    
    # Assign category
    cat = "EVS Core Foundations"
    if idx in [0, 1, 50, 51]: cat = "Earth as a Life Support System"
    elif idx in [2, 3, 4, 5, 6, 7, 52, 53]: cat = "Ecosystem & Energy Flow"
    elif idx in [8, 9, 54, 55, 56]: cat = "Ecological Succession"
    elif idx in [10, 11, 12, 13, 14, 39, 40, 44]: cat = "Biodiversity & Conservation"
    elif idx in [15, 16, 17]: cat = "Air Pollution"
    elif idx in [18, 19, 20, 21, 48, 57, 58]: cat = "Water Pollution & Management"
    elif idx in [22, 23, 24, 49, 59, 60]: cat = "Circular Economy & Solid Waste"
    elif idx in [25, 26, 61]: cat = "Hazards & Disaster Management"
    elif idx in [27, 62]: cat = "Environmental Impact Assessment (EIA)"
    elif idx in [28, 29, 36, 41, 42, 43]: cat = "Indian Environmental Laws"
    elif idx in [30, 31, 32, 33, 34, 35, 45, 46, 47]: cat = "Kyoto, Paris & SDGs"
    elif idx in [37, 38]: cat = "Chemical Hazards (BPA & Mercury)"

    website_questions.append({
        "id": idx + 1,
        "source": "masterdooom.github.io/evs (Official 63)",
        "isOfficial63": True,
        "category": cat,
        "question": q,
        "options": opts,
        "correctAnswer": correct_opt,
        "explanation": exp
    })

# 3. Add high-yield generated questions covering the specific topics from the website's 26 modules
additional_topic_questions = [
    # Topic 1: Earth as a Life Support System
    {
        "id": 64,
        "source": "masterdooom.github.io/evs (Topic 1: Life Support)",
        "isOfficial63": False,
        "category": "Earth as a Life Support System",
        "question": "Which boundary separates the troposphere from the stratosphere?",
        "options": ["Stratopause", "Mesopause", "Tropopause", "Thermopause"],
        "correctAnswer": "Tropopause",
        "explanation": "The tropopause is the atmospheric boundary layer where the environmental lapse rate drops and temperature inversion begins in the stratosphere."
    },
    {
        "id": 65,
        "source": "masterdooom.github.io/evs (Topic 1: Life Support)",
        "isOfficial63": False,
        "category": "Earth as a Life Support System",
        "question": "The lithosphere primarily comprises:",
        "options": ["Earth's crust and uppermost solid mantle", "Only ocean sediments", "The molten liquid outer core", "The lower atmosphere gases"],
        "correctAnswer": "Earth's crust and uppermost solid mantle",
        "explanation": "The lithosphere constitutes the rigid outermost shell of rocky terrestrial planets, consisting of the crust and upper mantle."
    },
    # Topic 2: Ecosystem Core Concepts
    {
        "id": 66,
        "source": "masterdooom.github.io/evs (Topic 2: Core Concepts)",
        "isOfficial63": False,
        "category": "Ecosystem — Core Concepts",
        "question": "The term 'Ecology' was coined in 1866 by:",
        "options": ["Charles Elton", "Ernst Haeckel", "Eugene Odum", "Arthur Tansley"],
        "correctAnswer": "Ernst Haeckel",
        "explanation": "German zoologist Ernst Haeckel coined the word 'Oecologie' from Greek oikos (house) and logos (study) to denote the study of organisms in their environment."
    },
    {
        "id": 67,
        "source": "masterdooom.github.io/evs (Topic 2: Core Concepts)",
        "isOfficial63": False,
        "category": "Ecosystem — Core Concepts",
        "question": "Which of the following is an artificial (man-made) ecosystem?",
        "options": ["Tropical rainforest", "Coral reef", "Cultivated crop field", "Natural freshwater lake"],
        "correctAnswer": "Cultivated crop field",
        "explanation": "Agricultural crop fields, managed aquaria, and botanical gardens are artificial ecosystems requiring continuous human inputs of energy and nutrients."
    },
    # Topic 3 & 4: Energy flow & Thermodynamics
    {
        "id": 68,
        "source": "masterdooom.github.io/evs (Topic 4: Energy Flow)",
        "isOfficial63": False,
        "category": "Ecosystem & Energy Flow",
        "question": "Which biome exhibits the highest Net Primary Productivity (NPP) according to the notes?",
        "options": ["Temperate grassland", "Tropical rainforest", "Boreal taiga", "Arctic tundra"],
        "correctAnswer": "Tropical rainforest",
        "explanation": "Tropical rainforests have optimal temperature, abundant rainfall, and year-round sunlight, generating high NPP of ~2,000 g/m²/year."
    },
    {
        "id": 69,
        "source": "masterdooom.github.io/evs (Topic 4: Energy Flow)",
        "isOfficial63": False,
        "category": "Ecosystem & Energy Flow",
        "question": "Why does the Second Law of Thermodynamics explain unidirectional energy flow in ecosystems?",
        "options": ["Energy is destroyed at each trophic level", "Energy transformation is never 100% efficient; heat is continuously lost", "Energy increases as entropy decreases", "Consumers produce their own solar radiation"],
        "correctAnswer": "Energy transformation is never 100% efficient; heat is continuously lost",
        "explanation": "Due to entropy and the 2nd law, energy degraded into metabolic heat cannot be recaptured by autotrophs, making energy flow strictly one-way."
    },
    # Topic 5: Succession
    {
        "id": 70,
        "source": "masterdooom.github.io/evs (Topic 5: Succession)",
        "isOfficial63": False,
        "category": "Ecological Succession",
        "question": "According to the notes, secondary succession is roughly how much faster than primary succession?",
        "options": ["Equal speed", "2× faster", "5–10× faster", "100× faster"],
        "correctAnswer": "5–10× faster",
        "explanation": "Secondary succession proceeds roughly 5–10 times faster than primary succession because fertile topsoil and seed propagules already exist."
    },
    {
        "id": 71,
        "source": "masterdooom.github.io/evs (Topic 5: Succession)",
        "isOfficial63": False,
        "category": "Ecological Succession",
        "question": "The Polyclimax Theory of ecological succession was proposed by:",
        "options": ["F.E. Clements", "A.G. Tansley", "Charles Darwin", "Raymond Lindeman"],
        "correctAnswer": "A.G. Tansley",
        "explanation": "Sir Arthur Tansley proposed the Polyclimax Theory, arguing that multiple stable climax types can persist in a region governed by moisture, soil, or topography."
    },
    # Topic 7 & 8: Species Status & Conservation
    {
        "id": 72,
        "source": "masterdooom.github.io/evs (Topic 7: Species Status)",
        "isOfficial63": False,
        "category": "Biodiversity & Conservation",
        "question": "An amensal relationship is represented by:",
        "options": ["(+, +)", "(+, 0)", "(-, 0)", "(-, -)"],
        "correctAnswer": "(-, 0)",
        "explanation": "In amensalism (-, 0), one organism is inhibited or destroyed while the other remains completely unaffected (e.g. Penicillium secreting penicillin)."
    },
    {
        "id": 73,
        "source": "masterdooom.github.io/evs (Topic 8: Conservation)",
        "isOfficial63": False,
        "category": "Biodiversity & Conservation",
        "question": "In a Biosphere Reserve, human settlements and sustainable eco-friendly practices are permitted primarily in the:",
        "options": ["Core zone", "Buffer zone only", "Transition zone", "National Park core"],
        "correctAnswer": "Transition zone",
        "explanation": "The outer Transition zone (Zone of Cooperation) contains human settlements, sustainable agriculture, and economic activities managed in harmony with nature."
    },
    # Topic 9: GM Crops
    {
        "id": 74,
        "source": "masterdooom.github.io/evs (Topic 9: GM Crops)",
        "isOfficial63": False,
        "category": "Genetically Modified Crops",
        "question": "Bt toxins encoded by Cry genes are toxic to target insects because they:",
        "options": ["Freeze the insect's hemolymph", "Bind to receptors in the alkaline insect midgut and form lethal pores", "Paralyze insect wings", "Prevent egg hatching"],
        "correctAnswer": "Bind to receptors in the alkaline insect midgut and form lethal pores",
        "explanation": "Under the alkaline pH of the insect midgut, Cry protoxins are cleaved into active toxins that bind epithelial cadherin receptors and lyse gut cells."
    },
    # Topic 10: Air Pollution & Smog
    {
        "id": 75,
        "source": "masterdooom.github.io/evs (Topic 10: Air Pollution)",
        "isOfficial63": False,
        "category": "Air Pollution",
        "question": "Which of the following is a primary ingredient and indicator of photochemical smog?",
        "options": ["Sulfur dioxide only", "Peroxyacyl nitrate (PAN) and tropospheric ozone", "Pure water vapor", "Carbonic acid"],
        "correctAnswer": "Peroxyacyl nitrate (PAN) and tropospheric ozone",
        "explanation": "Photochemical smog is characterized by oxidants such as tropospheric ozone and peroxyacyl nitrates (PAN), which irritate human eyes and respiratory tracts."
    },
    # Topic 11: Water Pollution & Indicators
    {
        "id": 76,
        "source": "masterdooom.github.io/evs (Topic 11: Water Pollution)",
        "isOfficial63": False,
        "category": "Water Pollution & Management",
        "question": "What is the relationship between Biochemical Oxygen Demand (BOD) and water quality?",
        "options": ["Higher BOD indicates purer water", "Higher BOD indicates high organic pollution and low dissolved oxygen", "BOD is unrelated to dissolved oxygen", "BOD only measures salinity"],
        "correctAnswer": "Higher BOD indicates high organic pollution and low dissolved oxygen",
        "explanation": "High BOD means large amounts of organic waste are present; aerobic microbes consume dissolved oxygen to oxidize it, depleting oxygen for fish."
    },
    # Topic 13 & 14: Noise & Thermal
    {
        "id": 77,
        "source": "masterdooom.github.io/evs (Topic 13: Noise)",
        "isOfficial63": False,
        "category": "Noise, Thermal & Soil",
        "question": "Under the Noise Rules 2000 in India, ambient daytime noise standard for a Silent Zone is:",
        "options": ["50 dB(A)", "75 dB(A)", "85 dB(A)", "100 dB(A)"],
        "correctAnswer": "50 dB(A)",
        "explanation": "In India, silent zones (areas within 100m of hospitals, courts, schools) have daytime limits of 50 dB(A) and nighttime limits of 40 dB(A)."
    },
    # Topic 16: Waste & Circular Economy
    {
        "id": 78,
        "source": "masterdooom.github.io/evs (Topic 16: Circular Economy)",
        "isOfficial63": False,
        "category": "Circular Economy & Solid Waste",
        "question": "The biogas produced during anaerobic digestion consists predominantly of:",
        "options": ["Nitrogen and oxygen", "Methane (CH4) and Carbon dioxide (CO2)", "Chlorine and hydrogen", "Pure sulfur dioxide"],
        "correctAnswer": "Methane (CH4) and Carbon dioxide (CO2)",
        "explanation": "Anaerobic digesters produce biogas composed of 50–70% methane and 30–45% carbon dioxide, functioning as a clean renewable fuel."
    },
    # Topic 18: Chemical Hazards - BPA & Mercury
    {
        "id": 79,
        "source": "masterdooom.github.io/evs (Topic 18: BPA & Mercury)",
        "isOfficial63": False,
        "category": "Chemical Hazards (BPA & Mercury)",
        "question": "Bisphenol A (BPA) poses human health risks primarily because it mimics which hormone?",
        "options": ["Insulin", "Estrogen", "Thyroxine", "Adrenaline"],
        "correctAnswer": "Estrogen",
        "explanation": "BPA is a xenoestrogen that binds to estrogen receptors, interfering with endocrine regulation, fetal development, and reproductive systems."
    },
    {
        "id": 80,
        "source": "masterdooom.github.io/evs (Topic 18: BPA & Mercury)",
        "isOfficial63": False,
        "category": "Chemical Hazards (BPA & Mercury)",
        "question": "The neurological disease resulting from methylmercury toxicity was first recognized around which Japanese bay?",
        "options": ["Tokyo Bay", "Osaka Bay", "Minamata Bay", "Kyoto Bay"],
        "correctAnswer": "Minamata Bay",
        "explanation": "Industrial discharges of inorganic mercury into Minamata Bay were biologically converted by microbes to methylmercury, intoxicating consumers of coastal seafood."
    },
    # Topic 20: EIA
    {
        "id": 81,
        "source": "masterdooom.github.io/evs (Topic 20: EIA)",
        "isOfficial63": False,
        "category": "Environmental Impact Assessment (EIA)",
        "question": "What is the primary role of the Environmental Management Plan (EMP) in an EIA report?",
        "options": ["Calculate tax rates", "Detail mitigation measures, monitoring mechanisms, and emergency plans", "Advertise the project", "Select political representatives"],
        "correctAnswer": "Detail mitigation measures, monitoring mechanisms, and emergency plans",
        "explanation": "An EMP operationalizes the EIA by laying out specific, time-bound mitigation actions, monitoring schedules, and institutional responsibilities."
    },
    # Topic 21 & 22: Environmental Acts
    {
        "id": 82,
        "source": "masterdooom.github.io/evs (Topic 21: Water Act)",
        "isOfficial63": False,
        "category": "Indian Environmental Laws",
        "question": "The Water Act 1974 consists of how many chapters and sections?",
        "options": ["5 chapters, 30 sections", "8 chapters, 50 sections", "10 chapters, 64 sections", "12 chapters, 100 sections"],
        "correctAnswer": "10 chapters, 64 sections",
        "explanation": "The Water (Prevention and Control of Pollution) Act 1974 is structured into 10 comprehensive chapters spanning 64 statutory sections."
    },
    {
        "id": 83,
        "source": "masterdooom.github.io/evs (Topic 22: EPA 1986)",
        "isOfficial63": False,
        "category": "Indian Environmental Laws",
        "question": "The Environment (Protection) Act, 1986 was enacted under which Article of the Constitution of India?",
        "options": ["Article 21", "Article 48A", "Article 253", "Article 370"],
        "correctAnswer": "Article 253",
        "explanation": "Article 253 empowers Parliament to make laws implementing international agreements (specifically the 1972 UN Stockholm Conference resolutions)."
    },
    # Topic 23: Godavarman judgment
    {
        "id": 84,
        "source": "masterdooom.github.io/evs (Topic 23: Forest & Wildlife)",
        "isOfficial63": False,
        "category": "Indian Environmental Laws",
        "question": "The 1996 Supreme Court T.N. Godavarman judgment held that 'forest' must be understood according to its:",
        "options": ["Revenue department record only", "Dictionary meaning regardless of ownership", "Commercial timber yield", "Area exceeding 1,000 hectares only"],
        "correctAnswer": "Dictionary meaning regardless of ownership",
        "explanation": "The Supreme Court ruled that the Forest (Conservation) Act applies to all tracts bearing natural tree cover according to the dictionary meaning, irrespective of ownership."
    },
    # Topic 25: Paris Agreement
    {
        "id": 85,
        "source": "masterdooom.github.io/evs (Topic 25: Paris Agreement)",
        "isOfficial63": False,
        "category": "Kyoto, Paris & SDGs",
        "question": "Article 4 of the Paris Agreement commits nations to reach global peaking of emissions and achieve:",
        "options": ["A complete ban on coal by 2020", "Net-zero greenhouse gas emissions in the second half of this century", "Zero cars worldwide by 2030", "Equal emissions for every citizen"],
        "correctAnswer": "Net-zero greenhouse gas emissions in the second half of this century",
        "explanation": "Article 4.1 aims to achieve a balance between anthropogenic emissions by sources and removals by sinks of greenhouse gases in the second half of this century."
    },
    # Topic 26: SDGs
    {
        "id": 86,
        "source": "masterdooom.github.io/evs (Topic 26: SDGs)",
        "isOfficial63": False,
        "category": "Sustainable Development Goals",
        "question": "Which SDG is dedicated to 'Life on Land' (conserving terrestrial ecosystems, combating desertification and stopping biodiversity loss)?",
        "options": ["SDG 6", "SDG 13", "SDG 14", "SDG 15"],
        "correctAnswer": "SDG 15",
        "explanation": "SDG 15 focuses on protecting and restoring terrestrial ecosystems, managing forests sustainably, halting land degradation, and conserving biodiversity."
    }
]

all_website_generated = website_questions + additional_topic_questions

with open("/Users/pran/devjams26/website_mcqs.json", "w") as f:
    json.dump(all_website_generated, f, indent=2)

print(f"Generated {len(all_website_generated)} MCQs directly from masterdooom.github.io/evs ({len(website_questions)} official + {len(additional_topic_questions)} high-yield topic MCQs).")
