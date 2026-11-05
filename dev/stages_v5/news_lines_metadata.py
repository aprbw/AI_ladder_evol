# -*- coding: utf-8 -*-
"""
stages_v5/news_lines_metadata.py
================================
Defines the 13 Horizontal Lines (6 Company Product Lines + 7 Tech-Transfer TRL Lines,
with dashed extensions into Gen 5 predictions), Standalone Event classification,
News Salience Scores S in [1.0, 5.0], and rich sources/causal links for all 199 atomic events.
"""

# 13 Connected Horizontal Lines (Top to Bottom on Plot 0B)
# Tuple: (line_id, line_type, short_badge_label, full_line_name, line_color, ev_ids_set)
HORIZONTAL_LINES_SPEC = [
    # --- 6 COMPANY & MODEL PRODUCT LINES ---
    (
        "COMP_OPENAI",
        "Company Product Line",
        "Product Line • OpenAI (GPT-2 → GPT-3 → ChatGPT → GPT-4 → GPT-4o → o1/o3 → GPT-5 → GPT-5.4 → Ambient OS)",
        "Product Line • OpenAI Models & Products",
        "#5B2C6F",
        {"EV_014", "EV_029", "EV_039", "EV_074", "EV_077", "EV_093", "EV_111", "EV_115", "EV_144", "EV_145", "EV_151", "EV_180", "EV_182"},
    ),
    (
        "COMP_ANTHROPIC",
        "Company Product Line",
        "Product Line • Anthropic (Constitutional AI → RSP → Claude 3.5 & Artifacts → MCP → Claude Code → Sonnet 4.5 → Opus 4.6 → >90% AI Code)",
        "Product Line • Anthropic Claude & Agent Stack",
        "#A04000",
        {"EV_064", "EV_095", "EV_112", "EV_116", "EV_129", "EV_142", "EV_146", "EV_165", "EV_150", "EV_181"},
    ),
    (
        "COMP_GOOGLE",
        "Company Product Line",
        "Product Line • Google & DeepMind (AutoML & Smart Compose → BERT Search → AlphaFold 2 → Chinchilla & TPU v4 → Gemini 2.5 → Gemini 3 → 2028 AGI)",
        "Product Line • Google & DeepMind",
        "#1F618D",
        {"EV_009", "EV_010", "EV_015", "EV_031", "EV_036", "EV_051", "EV_143", "EV_148", "EV_183"},
    ),
    (
        "COMP_META_OPEN",
        "Company Product Line",
        "Product Line • Meta & Open-Weight Local (spaCy → HuggingFace → LLaMA-1 → llama.cpp → Llama-2 & Ollama → Mixtral → Llama-3.1 405B → 3D World Sim)",
        "Product Line • Meta & Open-Weight Local Ecosystem",
        "#117A65",
        {"EV_008", "EV_011", "EV_075", "EV_076", "EV_079", "EV_080", "EV_081", "EV_113", "EV_178"},
    ),
    (
        "COMP_DEEPSEEK",
        "Company Product Line",
        "Product Line • DeepSeek (671B V3 $5.58M Pretraining → DeepSeek-R1 Paper & Open Weights → $593B Market Rout → DeepSeek-V3.2)",
        "Product Line • DeepSeek Open Frontier",
        "#005A9C",
        {"EV_126", "EV_135", "EV_140", "EV_161", "EV_149"},
    ),
    (
        "COMP_NVIDIA_INFRA",
        "Company Product Line",
        "Product Line • NVIDIA, AI Silicon & Capex (V100 → $1B MSFT → A100 → $10B MSFT → $1T NVIDIA → 100k H100 → $500B Stargate → Blackwell → $4T NVIDIA → Rubin & Feynman)",
        "Product Line • NVIDIA Silicon, Hyperscale Capex & Nuclear Power",
        "#196F3D",
        {"EV_016", "EV_018", "EV_019", "EV_092", "EV_094", "EV_123", "EV_124", "EV_125", "EV_160", "EV_162", "EV_163", "EV_166", "EV_188", "EV_189", "EV_190", "EV_191"},
    ),

    # --- 7 TRUE TECH-TRANSFER TRL LINES (Paper -> End-User Default -> Prediction) ---
    (
        "TRL_TRANSFORMER",
        "Tech-Transfer TRL Line",
        "TRL • Transformer & Sequence Architecture (Vaswani Paper → BERT Paper → Bitter Lesson → Scaling Laws → FlashAttention → Mamba SSM → DeltaNet → Continual Plasticity)",
        "TRL Line • Transformer & Sequence Scaling Architecture",
        "#6C3483",
        {"EV_001", "EV_004", "EV_005", "EV_007", "EV_037", "EV_071", "EV_138", "EV_176"},
    ),
    (
        "TRL_COT_RLVR",
        "Tech-Transfer TRL Line",
        "TRL • Chain-of-Thought to System-2 RLVR Default (Wei CoT Paper → Snell Test-Time Compute → Manual CoT Dies → o3 ARC-AGI 87.5% → IMO Gold → GPT-5 Router Default → Lean-4 Proofs)",
        "TRL Line • Chain-of-Thought Prompting to System-2 RLVR Default",
        "#2874A6",
        {"EV_035", "EV_108", "EV_132", "EV_130", "EV_137", "EV_174", "EV_177"},
    ),
    (
        "TRL_RLHF_ALIGN",
        "Tech-Transfer TRL Line",
        "TRL • RLHF, DPO & Mechanistic Interpretability (Mesa-Opt → InstructGPT RLHF → Closed-Form DPO → Sleeper Agents → Golden Gate SAE → Alignment Faking → Circuit Graphs → 'MRI for AI')",
        "TRL Line • RLHF, Preference Optimization & Mechanistic Interpretability",
        "#76448A",
        {"EV_006", "EV_034", "EV_067", "EV_072", "EV_107", "EV_110", "EV_136", "EV_139", "EV_179"},
    ),
    (
        "TRL_RAG_MEMORY",
        "Tech-Transfer TRL Line",
        "TRL • RAG, Embeddings & Grounded Search (Lewis Coins RAG → OpenAI Embeddings API → LangChain Framework → Deep Research Agent)",
        "TRL Line • Retrieval-Augmented Generation (RAG) & Grounded Search",
        "#0E6251",
        {"EV_030", "EV_042", "EV_073", "EV_141"},
    ),
    (
        "TRL_LORA_SERVING",
        "Tech-Transfer TRL Line",
        "TRL • LoRA, 4-Bit QLoRA & Serving Engines (Hu LoRA Paper → Dettmers 4-Bit QLoRA → vLLM PagedAttention → Open RLVR Cookbook)",
        "TRL Line • Parameter-Efficient LoRA/QLoRA & High-Throughput Serving",
        "#148F77",
        {"EV_033", "EV_066", "EV_078", "EV_171"},
    ),
    (
        "TRL_AGENT_CODING",
        "Tech-Transfer TRL Line",
        "TRL • Coding Agents, ReAct & METR Horizon (Software 2.0 → Copilot → Yao ReAct → SWE-bench → Cursor Composer → METR 7-Mo Law → Vibecoding → METR 2h → 8h & 168h Autonomy)",
        "TRL Line • AI Software Engineering, ReAct Loops & METR Autonomy Horizon",
        "#B9770E",
        {"EV_002", "EV_041", "EV_038", "EV_100", "EV_101", "EV_114", "EV_127", "EV_128", "EV_152", "EV_168", "EV_170", "EV_192", "EV_195"},
    ),
    (
        "TRL_MULTIMODAL",
        "Tech-Transfer TRL Line",
        "TRL • Multimodal Diffusion, Audio & Video (CLIP & DALL-E 1 → Craiyon → Midjourney Beta → Stable Diffusion → Sora Preview → Suno v3 → Sora 2 Audio-Video)",
        "TRL Line • Multimodal Latent Diffusion, Audio & Video Synthesis",
        "#884EA0",
        {"EV_040", "EV_046", "EV_043", "EV_044", "EV_082", "EV_083", "EV_147"},
    ),
]


# Top 6 Landmark Events at exact Title Font Size (S = 5.0),
# Intermediate Tiers (S in [1.4, 4.2]), and Smallest Events at < 0.25 * Title Font Size (S = 1.0)
EVENT_SALIENCE_MAP = {
    # --- TOP 6 GLOBAL LANDMARKS (S = 5.0 -> Rendered at exact `title_fs`!) ---
    "EV_001": 5.0,  # 2017-06: Vaswani 'Attention Is All You Need'
    "EV_029": 5.0,  # 2020-05: OpenAI Publishes GPT-3 175B Few-Shot Paper
    "EV_074": 5.0,  # 2022-11: OpenAI Launches ChatGPT (100M in 60d)
    "EV_077": 5.0,  # 2023-03: OpenAI Launches Multimodal GPT-4
    "EV_112": 5.0,  # 2024-06: Anthropic Ships Claude 3.5 Sonnet & Artifacts
    "EV_140": 5.0,  # 2025-01: DeepSeek Releases Open-Weight DeepSeek-R1

    # --- TIER 2: MAJOR HEADLINE SHOCKWAVES (S = 3.4 - 4.2) ---
    "EV_004": 4.1,  # Google Devlin Paper Introduces BERT
    "EV_039": 4.0,  # OpenAI GPT-3 API Playground Launches
    "EV_041": 4.1,  # GitHub Copilot Preview Brings AI to VS Code
    "EV_043": 3.9,  # Midjourney Launches Discord /imagine Beta
    "EV_044": 3.9,  # Stability AI Open-Sources Stable Diffusion
    "EV_075": 4.0,  # Meta Releases LLaMA-1 Open-Weight Models
    "EV_082": 3.9,  # OpenAI Previews Sora 60-Second Video Model
    "EV_089": 4.1,  # OpenAI Board Fires & Reinstates Sam Altman
    "EV_094": 4.1,  # NVIDIA Crosses $1T Market Cap on H100 Boom
    "EV_096": 3.8,  # The New York Times Sues OpenAI & Microsoft
    "EV_109": 3.9,  # Hinton, Hopfield, Hassabis & Jumper Win Nobels
    "EV_111": 4.2,  # OpenAI Launches Native Omni-Modal GPT-4o
    "EV_114": 4.0,  # Cursor Composer Ignites Multi-File Vibe Coding
    "EV_115": 4.1,  # OpenAI Launches o1 System-2 Reasoning Model
    "EV_135": 4.0,  # DeepSeek-R1 Paper Proves Pure RLVR Emergence
    "EV_142": 4.0,  # Anthropic Launches Claude Code CLI Agent
    "EV_145": 4.1,  # OpenAI Launches Unified Router Model GPT-5
    "EV_151": 4.0,  # OpenAI Releases GPT-5.4 Flagship Reasoner
    "EV_152": 3.9,  # Andrej Karpathy Coins 'Vibecoding'
    "EV_158": 3.9,  # Merriam-Webster & Economist Name 'Slop' WOTY
    "EV_160": 4.0,  # White House & OpenAI Announce $500B Stargate
    "EV_161": 4.2,  # DeepSeek-R1 Panic Wipes $593B Off NVIDIA Stock
    "EV_166": 4.1,  # NVIDIA Crosses $4T Market Cap on Inference Boom
    "EV_180": 3.8,  # Altman, Ive & Nadella Predict Ambient OS Daemons
    "EV_181": 3.8,  # Dario Amodei Predicts AI Agents Write >90% of Code
    "EV_183": 3.8,  # Demis Hassabis & Legg Predict 2028 AGI Arrival

    # --- TIER 3: SIGNIFICANT INDUSTRY & RESEARCH MILESTONES (S = 2.0 - 3.3) ---
    "EV_002": 3.0, "EV_005": 2.9, "EV_007": 3.2, "EV_010": 3.1, "EV_011": 3.1,
    "EV_014": 3.0, "EV_015": 3.1, "EV_016": 3.0, "EV_017": 2.9, "EV_018": 3.0,
    "EV_019": 3.0, "EV_020": 2.8, "EV_030": 3.1, "EV_031": 3.3, "EV_032": 2.9,
    "EV_033": 3.0, "EV_034": 3.2, "EV_035": 3.3, "EV_036": 3.1, "EV_037": 3.0,
    "EV_038": 2.9, "EV_040": 3.0, "EV_047": 3.1, "EV_048": 2.9, "EV_049": 2.8,
    "EV_052": 3.1, "EV_053": 3.1, "EV_054": 2.8, "EV_059": 2.9, "EV_064": 3.0,
    "EV_066": 3.1, "EV_067": 2.9, "EV_068": 2.8, "EV_069": 2.8, "EV_071": 2.8,
    "EV_072": 2.8, "EV_073": 3.1, "EV_076": 3.0, "EV_078": 3.0, "EV_079": 3.2,
    "EV_080": 2.9, "EV_081": 3.0, "EV_083": 2.8, "EV_084": 2.9, "EV_085": 3.0,
    "EV_086": 2.9, "EV_087": 3.1, "EV_088": 3.1, "EV_090": 2.9, "EV_091": 2.9,
    "EV_092": 3.3, "EV_095": 2.8, "EV_097": 3.2, "EV_098": 2.9, "EV_099": 2.8,
    "EV_101": 3.0, "EV_104": 2.9, "EV_107": 3.0, "EV_108": 2.9, "EV_110": 3.0,
    "EV_113": 3.2, "EV_116": 3.3, "EV_117": 3.1, "EV_118": 3.1, "EV_119": 2.8,
    "EV_120": 2.8, "EV_121": 3.1, "EV_122": 3.0, "EV_123": 3.2, "EV_124": 3.1,
    "EV_125": 3.1, "EV_126": 3.2, "EV_128": 3.0, "EV_130": 3.2, "EV_136": 2.9,
    "EV_137": 3.1, "EV_141": 3.1, "EV_143": 3.1, "EV_144": 3.2, "EV_146": 3.2,
    "EV_147": 3.1, "EV_148": 3.2, "EV_149": 3.0, "EV_150": 3.2, "EV_153": 2.9,
    "EV_154": 3.0, "EV_155": 3.2, "EV_156": 2.9, "EV_157": 3.0, "EV_162": 3.2,
    "EV_163": 3.0, "EV_165": 3.0, "EV_170": 3.1, "EV_176": 3.0, "EV_177": 3.0,
    "EV_178": 3.1, "EV_179": 3.0, "EV_182": 3.1, "EV_184": 2.8, "EV_186": 2.8,
    "EV_188": 3.1, "EV_190": 3.1, "EV_191": 3.1, "EV_192": 3.0, "EV_195": 3.1,
    "EV_199": 2.9,
}


def get_event_salience_score(ev_id: str, is_flagship: bool) -> float:
    """Return S in [1.0, 5.0]. Unlisted non-flagship events get S = 1.0 (< 0.25 * title_fs)."""
    if ev_id in EVENT_SALIENCE_MAP:
        return float(EVENT_SALIENCE_MAP[ev_id])
    if is_flagship:
        return 2.1
    return 1.0

