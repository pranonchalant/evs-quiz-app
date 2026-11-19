import json
import re

# ── 1. COMPILE VIT VELLORE FAT SHORT NOTES (PARTS A - G) ───────────────────
fat_notes = [
    {
        "id": "part-a",
        "part": "PART A",
        "title": "Numbers to Memorise (FAT Cheat Sheet)",
        "badge": "Cheat Sheet",
        "intro": "One-page number cheat sheet covering key statistics, temperatures, capacities, targets, and Indian government schemes. Note: quote the topic-specific value in case of minor variations across modules.",
        "type": "table",
        "tableHeaders": ["Topic / Concept", "Key Fact / Numerical Value"],
        "tableRows": [
            ["Earth temp without greenhouse effect", "-18 °C (with natural greenhouse: ~15 °C)"],
            ["Warming so far", "~1.1 °C above pre-industrial baseline (before 1850)"],
            ["CO2 atmospheric concentration", "280 ppm (pre-industrial) -> over 420 ppm currently (highest in 800,000 to 3M years)"],
            ["Methane warming potency", "~80–84x CO2 over 20-year horizon; GWP100 = 28–34"],
            ["Nitrous oxide (N2O) potency", "~265x CO2 over 100-year horizon (GWP100 = 265–298)"],
            ["Sea level rise", "~20 cm rise since 1900; projected 0.3 to 1.0 m by 2100 (IPCC)"],
            ["Arctic summer sea ice loss", "Declining ~13% per decade since satellite records began in 1979"],
            ["Ocean absorption", "~90% of excess heat trapped; ~25–30% of anthropogenic CO2"],
            ["Ocean pH drop", "Dropped ~0.1 units since industrial era = ~26% increase in acidity"],
            ["Coral reef degradation", "Support ~25% of marine life; bleach at +1 °C; >99% severely degraded at +2 °C"],
            ["Warmer air moisture capacity", "~7% more water vapor per 1 °C of warming (Clausius-Clapeyron relation)"],
            ["Global emission shares", "Fossil fuels ~75%; Deforestation 10–15%; Agriculture 10–12%; Cement ~8%"],
            ["Sectoral emission shares", "Electricity & heat ~34%; Industry ~24%; Agri & land use ~22%; Transport ~16%; Buildings 17–19% (incl. Scope 2)"],
            ["Cement production footprint", "~0.8 t CO2 per tonne of cement; roughly half from calcination of limestone (CaCO3 -> CaO + CO2)"],
            ["Per capita carbon footprint", "Global average ~4 t CO2e/yr; USA 14–16 t; India ~2 t CO2e/yr"],
            ["Peak solar irradiance", "~1000 W/m² at solar noon on a clear day (standard test conditions)"],
            ["Solar PV efficiencies", "Monocrystalline: 20–22%; Polycrystalline: 15–17%; Thin-film: 10–13%; Perovskite tandem: >30%"],
            ["Solar degradation & tracking", "~0.5%/year degradation (80–85% after 25 yrs); single/dual-axis trackers add 15–35% yield"],
            ["Capacity factors by tech", "Wind: 35–50% onshore, 50–60% offshore; Geothermal: 80–95% (baseload); Solar: 20–25%"],
            ["India renewable & climate targets", "500 GW non-fossil capacity by 2030; 50% electric power from non-fossil by 2030; Net-Zero by 2070"],
            ["Hydropower global share & efficiency", "15–16% of global electricity; efficiency above 90%; dam lifespan 50–100+ years"],
            ["Geothermal global leaders", "Kenya generates 47% of its electricity from geothermal; Iceland over 20% (nearly 100% building heat)"],
            ["Geothermal plant operating temps", "Flash steam: >180 °C; Binary cycle: 100–180 °C (uses isobutane/pentane)"],
            ["Prominent Indian hydro plants", "Tehri Dam (1000 MW, Uttarakhand - Storage); Srinagar (330 MW - Run-of-river); Kadamparai (400 MW, TN - Pumped storage)"],
            ["Sardar Sarovar displacement", "Displaced ~320,000 people (major social/ecological controversy)"],
            ["Cost reductions in renewables", "Solar PV and wind capital costs down over 80% in a decade; solar LCOE down >90% since 2010"],
            ["WHO climate mortality estimate", "~250,000 additional deaths per year (2030–2050) from malnutrition, malaria, diarrhoea & heat stress"],
            ["Recycled aluminium savings", "~95% less energy required compared to smelting primary bauxite ore"],
            ["Global food waste", "~1/3 of all food produced for human consumption is lost or wasted globally"]
        ]
    },
    {
        "id": "part-b",
        "part": "PART B",
        "title": "Climate Change Science & Global Warming (W5S1, W5S2)",
        "badge": "Core Theory",
        "intro": "Physics of the greenhouse effect, atmospheric drivers, 4 pillars of empirical evidence, causes vs natural factors, consequences, and mitigation vs adaptation.",
        "type": "sections",
        "sections": [
            {
                "heading": "1. Greenhouse Effect Fundamentals",
                "content": "• Natural greenhouse effect = beneficial heat trapping keeping Earth's mean temperature at ~15 °C (without it: -18 °C).<br>• Enhanced greenhouse effect = excessive anthropogenic radiative forcing caused by elevated GHG concentrations from fossil fuel burning, deforestation, and industrial processes.<br>• Radiation physics: Sun emits short-wave radiation (visible, UV) which penetrates the atmosphere and heats Earth's surface. The warmed surface re-emits thermal radiation as long-wave infrared. Greenhouse gases absorb this infrared radiation and re-radiate it in all directions, trapping heat in the lower troposphere."
            },
            {
                "heading": "2. Key Greenhouse Gases Table",
                "tableHeaders": ["Greenhouse Gas", "Main Anthropogenic Sources", "Atmospheric Lifespan & Potency"],
                "tableRows": [
                    ["Carbon Dioxide (CO2)", "Fossil fuel combustion (coal, oil, gas), cement production, deforestation", "Stays centuries to millennia; baseline reference (GWP = 1)"],
                    ["Methane (CH4)", "Enteric fermentation (cattle), rice paddies, landfills, fossil fuel leaks", "Short-lived (~12 yrs) but 80–84x more potent than CO2 over 20 yrs (GWP100 = 28–34)"],
                    ["Nitrous Oxide (N2O)", "Synthetic nitrogen fertilisers, manure management, nylon/chemical industry", "~114 yrs lifespan; ~265x more potent than CO2 (GWP100 = 265–298)"],
                    ["Water Vapour (H2O)", "Natural hydrological evaporation (amplified by warming air)", "Most abundant GHG by volume; acts as a powerful positive feedback amplifier"],
                    ["Fluorinated Gases (HFCs, PFCs, SF6)", "Refrigeration, AC, semiconductor manufacturing, electrical switchgear", "Synthetic gases; GWPs thousands to tens of thousands; persist centuries"]
                ]
            },
            {
                "heading": "3. Four Independent Pillars of Evidence",
                "content": "1. Rising Surface Temperatures: Global mean temp up ~1.1 °C; 19 of the 20 hottest years on record have occurred since 2000 (NASA, NOAA, UK Met Office, JMA).<br>2. Rising Atmospheric CO2: Surged from 280 ppm pre-industrial to >420 ppm; confirmed by Antarctic ice core bubbles dating back 800,000 years.<br>3. Melting Cryosphere & Sea Level Rise: Arctic summer sea ice extent shrinking ~13%/decade; Antarctic and Greenland ice sheets losing mass; global mean sea level up ~20 cm since 1900.<br>4. Ocean Warming & Acidification: Oceans have absorbed >90% of excess heat and 25–30% of anthropogenic CO2; dissolving CO2 forms carbonic acid (H2CO3), dropping pH by 0.1 units (~26% acidity surge)."
            },
            {
                "heading": "4. Why Natural Factors Do NOT Explain Warming",
                "content": "• Volcanic Eruptions: Eject sulfate aerosols into the stratosphere that reflect sunlight, causing short-term cooling (1–3 years), not warming.<br>• Solar Output: Satellite observations confirm solar irradiance has slightly decreased since the 1980s while Earth's surface warmed rapidly.<br>• Milankovitch Orbital Cycles: Operate on timescales of 20,000 to 100,000 years — incapable of driving century-scale rapid warming."
            },
            {
                "heading": "5. Mitigation vs Adaptation",
                "tableHeaders": ["Parameter", "Mitigation (Root Cause)", "Adaptation (Managing Symptoms)"],
                "tableRows": [
                    ["Objective", "Reduce or prevent greenhouse gas emissions; enhance carbon sinks", "Adjust ecological, social, or economic systems to cope with unavoidable impacts"],
                    ["Examples", "Renewable energy (solar, wind), energy efficiency, reforestation, Carbon Capture & Storage (CCS), electric vehicles", "Sea walls, flood barriers, drought-resistant crop varieties, early warning systems, rainwater harvesting, elevated roadways"],
                    ["Timing & Scale", "Global benefit with long-term atmospheric delay", "Local/regional benefit with immediate protective effect"]
                ]
            },
            {
                "heading": "6. Policy Frameworks & Indian Commitments",
                "content": "• Paris Agreement (2015): Legally binding treaty aiming to hold global warming well below 2 °C and pursue efforts to cap warming at 1.5 °C above pre-industrial baselines.<br>• Nationally Determined Contributions (NDCs): National climate pledges updated every 5 years.<br>• India's NDC & Glasgow COP26 Commitments: Net-Zero by 2070; 500 GW non-fossil capacity by 2030; 50% cumulative electric power from non-fossil sources by 2030; carbon intensity reduction of 45% by 2030.<br>• National Action Plan on Climate Change (NAPCC, 2008): 8 National Missions — Solar Mission, Enhanced Energy Efficiency, Sustainable Habitat, Water Mission, Sustaining Himalayan Ecosystem, Green India Mission (afforestation), Sustainable Agriculture, Strategic Knowledge for Climate Change."
            }
        ]
    },
    {
        "id": "part-c",
        "part": "PART C",
        "title": "Carbon Footprint & Mitigation Strategies (W5S3)",
        "badge": "Accounting & Policy",
        "intro": "Standardized GHG quantification (Scopes 1, 2, 3), Life Cycle Assessment (LCA), sectoral emission breakdowns, mitigation pillars, and carbon offsets.",
        "type": "sections",
        "sections": [
            {
                "heading": "1. Scopes of Carbon Footprint (Greenhouse Gas Protocol)",
                "tableHeaders": ["Scope", "Classification", "Definition & Industrial Examples"],
                "tableRows": [
                    ["Scope 1", "Direct Emissions", "GHG emissions directly from owned or company-controlled sources (boilers, furnaces, company-owned vehicles, chemical reaction vessels)."],
                    ["Scope 2", "Indirect Energy Emissions", "Emissions from the generation of purchased electricity, steam, heating, or cooling consumed by the organization."],
                    ["Scope 3", "Indirect Value-Chain Emissions", "All other indirect emissions throughout the upstream and downstream supply chain (raw materials extraction, transport, customer product use, end-of-life disposal). Frequently accounts for >70% of a company's total footprint."]
                ]
            },
            {
                "heading": "2. Carbon Accounting Standards & LCA",
                "content": "• Life Cycle Assessment (LCA): Primary engineering tool assessing cumulative environmental impacts from 'cradle' (raw material extraction) to 'grave' (disposal). 'Cradle to cradle' closes the loop through repair, remanufacture, and recycling.<br>• Standards to Memorise:<br>  - GHG Protocol: Most widely used global corporate accounting standard.<br>  - ISO 14064: International standard for organizational GHG inventories and verification.<br>  - PAS 2050: Standard specifically measuring life cycle GHG emissions of goods and services."
            },
            {
                "heading": "3. Global Sectoral Breakdown",
                "tableHeaders": ["Sector", "Share of Global Emissions", "Key Decarbonization Levers"],
                "tableRows": [
                    ["Electricity & Heat Generation", "~34% of global CO2", "Phase out coal (emits ~2x CO2/MWh vs natural gas); rapid buildout of solar PV, wind, hydro, and nuclear baseload."],
                    ["Industry & Manufacturing", "~24% of global GHGs", "Iron & steel (green hydrogen direct reduction), cement (clinker substitution, CCS), circular aluminium."],
                    ["Agriculture & Land Use", "~22% of global GHGs", "Methane capture from manure, precision nitrogen fertilisation, agroforestry, alternate wetting/drying in rice."],
                    ["Transport", "~16% of global GHGs", "Fleet electrification (EVs), modal shift from road/air to electrified rail, Sustainable Aviation Fuel (SAF)."],
                    ["Buildings", "6% direct (~17–19% with Scope 2)", "Heat pumps, building envelope insulation, LED retrofits, passive solar design."]
                ]
            },
            {
                "heading": "4. Key Mitigation Technologies",
                "content": "• Energy Efficiency: Designated by the IEA as the 'first fuel' — cleanest and cheapest decarbonization mechanism.<br>• Carbon Capture & Storage (CCS): Capturing industrial flue gas CO2 and sequestering it securely deep underground in saline aquifers or depleted oil fields.<br>• Carbon Capture & Utilisation (CCU): Transforming captured CO2 into commercial building aggregates, synthetic fuels, or chemicals.<br>• Direct Air Capture (DAC): Scrubbing dilute CO2 directly from ambient air using chemical contactors.<br>• Carbon Offsets: High-integrity credits must satisfy 4 criteria: Additional (would not happen without finance), Measurable, Permanent (non-reversal), and Independently Verified."
            }
        ]
    },
    {
        "id": "part-d",
        "part": "PART D",
        "title": "Solar & Wind Energy (W6S1 Part 1)",
        "badge": "Renewable Tech",
        "intro": "Engineering principles of photovoltaic cells, Concentrated Solar Power (CSP), wind turbine mechanics, HAWT vs VAWT, Betz limit, and Indian renewable policies.",
        "type": "sections",
        "sections": [
            {
                "heading": "1. Solar Photovoltaic (PV) Technology",
                "content": "• Photovoltaic Effect: Incident photons knock valence electrons loose in a semiconductor (crystalline silicon); an internal electric field at the p-n junction sweeps free electrons, generating direct current (DC).<br>• Core Components: Solar PV array, Inverter (converts DC into grid-synchronized AC), Charge controller, Battery storage (optional), Mounting racks/trackers.<br>• Solar Output Equation: Power (W) = Irradiance (W/m²) × Panel Area (m²) × Module Efficiency (η).<br>• Temperature Coefficient: Solar PV efficiency decreases as temperature rises (negative coefficient, typically -0.35% to -0.45% per °C above 25 °C)."
            },
            {
                "heading": "2. PV Cell Types Comparison",
                "tableHeaders": ["Cell Technology", "Efficiency Range", "Key Engineering Features"],
                "tableRows": [
                    ["Monocrystalline Silicon", "20–22%", "Single continuous crystal (Czochralski process); highest commercial efficiency; uniform dark black appearance; higher cost."],
                    ["Polycrystalline Silicon", "15–17%", "Multiple silicon fragments melted together; blue speckled look; lower manufacturing cost; grain boundaries slightly reduce efficiency."],
                    ["Thin-Film (CdTe, a-Si)", "10–13%", "Semiconductor deposited in microscopic layers on glass/metal; flexible, lightweight, excellent low-light response; requires larger land area."],
                    ["Perovskite Tandem (Emerging)", ">30% (lab)", "Tandem layer on silicon tuning solar absorption bands; low production cost; currently hindered by moisture/UV degradation."]
                ]
            },
            {
                "heading": "3. Concentrated Solar Power (CSP) & Key Indian Schemes",
                "content": "• Concentrated Solar Power (CSP): Utilizes tracking heliostat mirrors to focus sunlight onto a central receiver tower, heating molten salt to >550 °C to generate superheated steam for conventional turbines with dispatchable thermal energy storage.<br>• Key Indian Solar Schemes:<br>  - PM Surya Ghar Muft Bijli Yojana: Rooftop solar for 1 crore households with subsidies up to ₹78,000.<br>  - PM-KUSUM: Solarization of agricultural pump sets (up to 60% subsidy to replace diesel pumps).<br>  - Bhadla Solar Park (Rajasthan): World's largest operational solar park (~2,245 MW).<br>  - International Solar Alliance (ISA): Co-founded by India and France; headquarters in Gurugram, India."
            },
            {
                "heading": "4. Wind Turbine Mechanics & Betz Limit",
                "content": "• Wind Power Physics: Kinetic energy of moving air converted to electricity. Power Equation: P = 0.5 × ρ × A × v³ (Power is proportional to the cube of wind speed — doubling wind speed yields 8x power).<br>• Betz Limit: Theoretical aerodynamic ceiling proving no wind turbine can extract more than 59.3% (16/27) of kinetic energy from wind.<br>• Turbine Speeds: Cut-in speed (3–4 m/s, blades begin rotating); Rated wind speed (12–15 m/s, maximum generator output); Cut-out speed (~25 m/s, pitch brakes activate to prevent mechanical failure).<br>• HAWT vs VAWT: Horizontal Axis Wind Turbines (HAWT) dominate commercial power due to superior aerodynamic efficiency; Vertical Axis Wind Turbines (VAWT) accept wind from any direction, ideal for turbulent urban settings.<br>• Indian Geography: Western coast (Gujarat, Maharashtra) is preferred due to consistent winds; Eastern coast is cyclone-prone. National Institute of Wind Energy (NIWE) is headquartered in Chennai. Muppandal Wind Farm (Tamil Nadu) is one of the world's largest."
            }
        ]
    },
    {
        "id": "part-e",
        "part": "PART E",
        "title": "Hydroelectric & Geothermal Energy (W6S1 Part 2)",
        "badge": "Baseload Renewables",
        "intro": "Hydraulic head and penstocks, pumped storage, dam impacts, geothermal enthalpy classification, flash vs binary plants, and tectonic sites.",
        "type": "sections",
        "sections": [
            {
                "heading": "1. Hydroelectric Power Generation",
                "content": "• Energy Conversion Chain: Potential Energy (water head in reservoir) -> Kinetic Energy (rushing through penstock) -> Mechanical Energy (turbine rotation) -> Electrical Energy (generator).<br>• Power Equation: P = ρ × g × Q × H × η (where ρ = water density, g = 9.81 m/s², Q = volumetric discharge in m³/s, H = effective hydraulic head in metres, η = turbine-generator efficiency >90%).<br>• Hydropower Classifications:<br>  - Storage / Impoundment: Large dam reservoir storing seasonal discharge (e.g., Tehri Dam, 1000 MW, Uttarakhand - highest in India).<br>  - Run-of-the-River: Diverts natural river flow through tunnels/canals with minimal reservoir flooding (e.g., Srinagar Hydro, 330 MW, Alaknanda).<br>  - Pumped Storage Hydro (PSH): Acts as a giant rechargeable grid battery; pumps water uphill during off-peak hours and discharges downhill during peak demand (e.g., Kadamparai, 400 MW, Tamil Nadu).<br>• Environmental Trade-offs: Zero direct operating stack emissions, but decaying submerged biomass in tropical reservoirs emits biogenic methane (CH4); blocks fish migration; causes reservoir-induced seismicity and downstream silt deprivation."
            },
            {
                "heading": "2. Geothermal Energy & Plant Architectures",
                "content": "• Geothermal Gradient: Normal continental temperature rise of 25–30 °C per kilometre of depth into Earth's crust.<br>• Geothermal Plant Thermodynamic Cycles:<br>  - Dry Steam Plants: Directly exploits rare natural dry underground steam (>200 °C) to drive turbines (e.g., The Geysers, California).<br>  - Flash Steam Plants: High-pressure deep water (>180 °C) is sprayed into lower-pressure flash tanks, instantaneously boiling ('flashing') into steam. Most prevalent global technology.<br>  - Binary Cycle Plants: Utilizes moderate geothermal fluid temperatures (100–180 °C) to heat a secondary organic working fluid with a lower boiling point (isobutane or pentane) in a closed heat exchanger. Geothermal water is 100% re-injected without atmospheric release.<br>• Indian Geothermal Prospects: Puga Valley (Ladakh - highest enthalpy in India), Tattapani (Chhattisgarh), Manikaran (Himachal Pradesh), Cambay Basin (Gujarat)."
            }
        ]
    },
    {
        "id": "part-f",
        "part": "PART F",
        "title": "AI & IoT in Environmental Monitoring",
        "badge": "Emerging Tech",
        "intro": "Sensors (NPK, optical dust, gas arrays), telemetry protocols, edge AI, LSTM pollution forecasting, digital twins, and case studies.",
        "type": "sections",
        "sections": [
            {
                "heading": "1. IoT Sensor Matrix for Environmental Telemetry",
                "tableHeaders": ["Domain / Medium", "Sensors & Detectors", "Monitored Environmental Parameters"],
                "tableRows": [
                    ["Air Quality", "Optical light scattering, MQ-135, electrochemical sensors", "PM2.5, PM10, CO, SO2, NOx, ground-level O3, volatile organic compounds (VOCs)"],
                    ["Water Quality", "Ion-selective electrodes, optical dissolved oxygen probes, turbidity meters", "pH, Dissolved Oxygen (DO), Electrical Conductivity (EC), Biochemical Oxygen Demand (BOD), turbidity"],
                    ["Soil & Precision Agri", "Capacitive probes, optical NPK spectrophotometers", "Volumetric soil moisture, soil temperature, Nitrogen (N), Phosphorus (P), Potassium (K) levels"],
                    ["Biodiversity & Wildlife", "Bioacoustic microphones, PIR motion camera traps", "Ultrasonic bat calls, illegal chain-saw logging sounds, wildlife poaching identification"],
                    ["Urban Waste", "Ultrasonic level sensors inside smart dumpsters", "Trash bin fill percentage, automated route optimization for municipal compactor trucks"]
                ]
            },
            {
                "heading": "2. Artificial Intelligence in Environmental Protection",
                "content": "• Long Short-Term Memory (LSTM) Networks: Recurrent neural networks ideal for processing temporal atmospheric time-series data to forecast air quality (AQI) 24–72 hours in advance.<br>• Digital Twins: Real-time physics-grounded 3D computational replicas of water treatment plants, urban airsheds, or river basins continuously updated by IoT telemetry to simulate failure scenarios.<br>• Computer Vision: Convolutional Neural Networks (CNNs) analyzing multi-spectral drone and satellite imagery to calculate NDVI (vegetation index) and map illegal deforestation.<br>• Landmark Indian AI Case Study: IIT Kharagpur researchers developed an AI geospatial machine learning framework predicting high-risk arsenic contamination in groundwater across the Ganga delta."
            }
        ]
    },
    {
        "id": "part-g",
        "part": "PART G",
        "title": "Last-Minute Exam Tips & VIT Marking Guide",
        "badge": "Exam Strategy",
        "intro": "High-frequency 2-mark definitions, 5/10-mark structures, and examiners' preferred keywords.",
        "type": "bullets",
        "bullets": [
            "Frequent 2-Mark Definitions to Memorise verbatim: Carbon footprint (CO2e), Global Warming Potential (GWP100), Scope 1 vs Scope 2 vs Scope 3, Betz limit (59.3%), Photovoltaic effect (p-n junction), Flash vs Binary geothermal cycles, Run-of-river vs Pumped storage hydro, Digital Twin.",
            "Frequent 5/10-Mark Question Frameworks: When asked for working principles of Solar PV / Wind / Hydro / Geothermal, ALWAYS draw the labelled block diagram showing the energy conversion chain.",
            "Always include Indian context: Mention 500 GW by 2030, Net-Zero 2070, PM Surya Ghar, Bhadla Solar Park (Rajasthan), Muppandal (Tamil Nadu), Tehri Dam (Uttarakhand), Puga Valley (Ladakh).",
            "Marking Scheme Tip: VIT examiners heavily reward technical terms (Clausius-Clapeyron, calcination, Betz limit, isobutane, enthalpy, LSTM, ISO 14064, CPCB under Water Act 1974)."
        ]
    }
]

# ── 2. COMPILE MASTERDOOOM EVS MODULES (ALL 26 TOPICS) ────────────────────
with open("/Users/pran/devjams26/website_dump.json") as f:
    dump = json.load(f)

# Extract topic definitions from topic1.js through topic5.js
# We can evaluate the array inside JS or parse with python regex
masterdooom_topics = []
for k in ["topic1.js", "topic2.js", "topic3.js", "topic4.js", "topic5.js"]:
    raw = dump[k]
    # Find all object boundaries
    # Each object has group, title, sub, p, must
    matches = re.finditer(r"group:\s*[\x27\"]([^\x27\"]+)[\x27\"].*?title:\s*[\x27\"]([^\x27\"]+)[\x27\"].*?sub:\s*[\x27\"]([^\x27\"]+)[\x27\"].*?p:\s*[\x27\"]([^\x27\"]+)[\x27\"].*?must:\s*\[(.*?)\]", raw, re.DOTALL)
    for m in matches:
        grp = m.group(1).strip()
        title = m.group(2).strip()
        sub = m.group(3).strip()
        pri = m.group(4).strip()
        must_raw = m.group(5)
        # Parse items inside must
        items = re.findall(r"[\x27\"]([^\x27\"]+)[\x27\"]", must_raw)
        
        masterdooom_topics.append({
            "group": grp,
            "title": title,
            "sub": sub,
            "priority": pri,
            "must": items
        })

print(f"Loaded {len(fat_notes)} FAT note sections.")
print(f"Loaded {len(masterdooom_topics)} Masterdooom syllabus modules.")

all_notes_data = {
    "fatNotes": fat_notes,
    "masterdooomTopics": masterdooom_topics
}

with open("/Users/pran/devjams26/notes_data.json", "w", encoding="utf-8") as f:
    json.dump(all_notes_data, f, indent=2, ensure_ascii=False)

print("Saved notes_data.json successfully!")
