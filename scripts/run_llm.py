"""
run_llm.py — Dual LLM summarizer (Claude + OpenAI)
Usage:
    python scripts/run_llm.py --provider claude
    python scripts/run_llm.py --provider openai
    python scripts/run_llm.py --provider both
"""
import os
import argparse
from pathlib import Path
from datetime import datetime

# ── Lecture du fichier d'entrée ──────────────────────────────────────────────
INPUT_FILE  = Path("inputs/sample.txt")
OUTPUT_DIR  = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def read_input() -> str:
    return INPUT_FILE.read_text(encoding="utf-8")

def save_output(provider: str, content: str):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out = OUTPUT_DIR / f"summary_{provider}_{ts}.txt"
    out.write_text(content, encoding="utf-8")
    print(f"[{provider}] Sauvegardé → {out}")

# ── Claude (Anthropic) ───────────────────────────────────────────────────────
def call_claude(text: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model="claude-opus-4-20250514",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"Résume ce texte en 3 points clés:\n\n{text}"
        }]
    )
    return msg.content[0].text

# ── OpenAI ───────────────────────────────────────────────────────────────────
def call_openai(text: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"Résume ce texte en 3 points clés:\n\n{text}"
        }]
    )
    return resp.choices[0].message.content

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["claude", "openai", "both"], default="both")
    args = parser.parse_args()

    text = read_input()
    print(f"[info] Texte lu : {len(text)} caractères")

    if args.provider in ("claude", "both"):
        result = call_claude(text)
        save_output("claude", result)

    if args.provider in ("openai", "both"):
        result = call_openai(text)
        save_output("openai", result)

if __name__ == "__main__":
    main()