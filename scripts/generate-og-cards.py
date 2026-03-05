#!/usr/bin/env python3
"""Generate blog-card-style OG images for posts. Run before Jekyll build."""

import os
import re
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    import yaml
except ImportError as e:
    print("pip install Pillow PyYAML")
    raise

POSTS_DIR = Path(__file__).parent.parent / "_posts"
ASSETS = Path(__file__).parent.parent / "assets" / "images" / "posts"
# OG image size (Twitter/FB recommended)
W, H = 1200, 628
OVERLAY_H = 220  # dark bar height at bottom
BODY_PADDING = 32
OVERLAY_COLOR = (0, 0, 0, 180)  # semi-transparent black
TITLE_COLOR = "#ffffff"
META_COLOR = "#b8c4c2"


def load_post(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    if not raw.startswith("---"):
        return None
    parts = raw.split("---", 2)  # Only split at first two --- to preserve body (may contain ---)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    if not data:
        return None
    cover = data.get("cover")
    image = data.get("image")
    if isinstance(image, dict):
        image = image.get("path")
    img_path = cover or image
    if not img_path:
        return None
    title = data.get("title_en") or data.get("title", "")
    excerpt = data.get("excerpt_en") or data.get("excerpt", "")
    excerpt = re.sub(r"<[^>]+>", "", excerpt or "")
    date = data.get("date")
    if date:
        s = str(date)[:10]  # 2026-03-05
        if len(s) >= 10:
            date = f"{s[5:7]}/{s[8:10]}/{s[2:4]}"  # 03/05/26
        else:
            date = ""
    # Extract dir from image path: /assets/images/posts/2026-03-05-virallab/cover.jpg
    m = re.search(r"posts/([^/]+)/", img_path)
    post_dir = m.group(1) if m else None
    if not post_dir:
        return None
    full_img = Path(__file__).parent.parent / img_path.lstrip("/")
    if not full_img.exists() or "og-card" in str(img_path):
        return None
    return {
        "path": path,
        "raw": raw,
        "parts": parts,
        "data": data,
        "img_path": full_img,
        "out_dir": ASSETS / post_dir,
        "og_path": f"/assets/images/posts/{post_dir}/og-card.png",
        "orig_img_path": img_path,
        "title": title,
        "excerpt": (excerpt or "")[:140],
        "date": date or "",
    }


def draw_card(data):
    out_path = data["out_dir"] / "og-card.png"
    data["out_dir"].mkdir(parents=True, exist_ok=True)

    # Load and crop cover to fill full card (1200x628)
    img = Image.open(data["img_path"]).convert("RGB")
    iw, ih = img.size
    scale = max(W / iw, H / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    x = (nw - W) // 2
    y = (nh - H) // 2
    card = img.crop((x, y, x + W, y + H))

    # Semi-transparent overlay bar at bottom
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    draw_overlay.rectangle([0, H - OVERLAY_H, W, H], fill=OVERLAY_COLOR)
    card = card.convert("RGBA")
    card = Image.alpha_composite(card, overlay)
    card = card.convert("RGB")
    draw = ImageDraw.Draw(card)

    # Fonts (macOS, Linux CI, fallback)
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    title_font = meta_font = None
    for fp in font_paths:
        if Path(fp).exists():
            try:
                title_font = ImageFont.truetype(fp, 38)
                meta_font = ImageFont.truetype(fp, 22)
                break
            except Exception:
                pass
    if not title_font:
        title_font = meta_font = ImageFont.load_default()

    base_y = H - OVERLAY_H + 24

    # Title (white)
    title = data["title"]
    if len(title) > 50:
        title = title[:47] + "..."
    draw.text((BODY_PADDING, base_y), title, fill=TITLE_COLOR, font=title_font)

    # Date and excerpt row
    if data["date"]:
        bbox = draw.textbbox((0, 0), data["date"], font=meta_font)
        tw = bbox[2] - bbox[0]
        draw.text((W - BODY_PADDING - tw, base_y + 4), data["date"], fill=META_COLOR, font=meta_font)

    excerpt = data["excerpt"]
    if excerpt:
        if len(excerpt) > 90:
            excerpt = excerpt[:87] + "..."
        draw.text((BODY_PADDING, base_y + 56), excerpt, fill=META_COLOR, font=meta_font)

    card.save(out_path, "PNG", optimize=True)
    return out_path


def update_front_matter(data):
    """Set image.path to og-card.png for social cards; preserve cover for in-post display."""
    orig = data.get("orig_img_path")
    if orig and not data["data"].get("cover"):
        data["data"]["cover"] = orig
    data["data"]["image"] = {
        "path": data["og_path"],
        "alt": data.get("title", "")[:80],
    }
    new_fm = yaml.dump(data["data"], allow_unicode=True, default_flow_style=False, sort_keys=False)
    new_content = "---\n" + new_fm.rstrip() + "\n---\n" + data["parts"][2]
    data["path"].write_text(new_content, encoding="utf-8")


def main():
    for path in sorted(POSTS_DIR.glob("*.md")):
        data = load_post(path)
        if not data:
            continue
        try:
            out = draw_card(data)
            update_front_matter(data)
            print(f"Generated {out}")
        except Exception as e:
            print(f"Skip {path.name}: {e}")


if __name__ == "__main__":
    main()
