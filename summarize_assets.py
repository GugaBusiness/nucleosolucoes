import json

with open(r"C:\Users\Guga\.gemini\antigravity\brain\2a810790-998b-47b9-939d-f8e7df06013a\scratch\assets_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

mappings = data["assets_mapping"]

only_asset_map = []
html_refs = []
unused = []

for asset, refs in mappings.items():
    if not refs:
        unused.append(asset)
    else:
        # Check if all refs are in the ASSET_MAP declaration
        decls = [r for r in refs if r["is_asset_map_decl"]]
        others = [r for r in refs if not r["is_asset_map_decl"]]
        if others:
            html_refs.append((asset, others, decls))
        else:
            only_asset_map.append((asset, decls))

print(f"Unused assets in index.html: {len(unused)}")
print(f"Assets referenced in HTML (outside mapping decl): {len(html_refs)}")
print(f"Assets referenced ONLY in ASSET_MAP: {len(only_asset_map)}")

print("\n--- HTML REFERENCES (LINK, SCRIPT, IMG, ETC.) ---")
for asset, others, decls in sorted(html_refs):
    print(f"\nAsset: {asset}")
    for ref in others:
        print(f"  Line {ref['line']}: {ref['context']}")

print("\n--- ONLY IN ASSET_MAP ---")
for asset, decls in sorted(only_asset_map):
    print(f"Asset: {asset} (Line {decls[0]['line']})")

if unused:
    print("\n--- UNUSED ---")
    for asset in sorted(unused):
        print(asset)
