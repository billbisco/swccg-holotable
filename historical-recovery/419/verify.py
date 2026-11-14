"""Verify preserved source bytes and deduplicated package path reconstruction."""
from pathlib import Path
import json, hashlib, base64, io
from PIL import Image
root = Path(__file__).resolve().parent
load = lambda p: json.loads((root/p).read_text(encoding="utf-8"))
assets = load("asset-inventory.json")
images = 0
for row in assets:
    data = (root/row["path"]).read_bytes()
    assert len(data) == row["bytes"], row["path"]
    assert hashlib.sha256(data).hexdigest() == row["sha256"], row["path"]
    if Path(row["path"]).suffix.lower() in (".gif", ".png", ".jpg", ".jpeg"):
        with Image.open(io.BytesIO(data)) as im: im.verify()
        images += 1
for manifest in ("metadata/large-v18-path-to-content.json", "metadata/revolution-path-to-content.json", "metadata/vkit-image-provenance.json", "metadata/archive-recovered-images.json"):
    for row in load(manifest):
        data = (root/row["stored_path"]).read_bytes()
        assert len(data) == row["bytes"], (manifest, row.get("path"))
        assert hashlib.sha256(data).hexdigest() == row["sha256"], (manifest, row.get("path"))
        if row.get("cdx_digest_matches"):
            assert base64.b32encode(hashlib.sha1(data).digest()).decode() == row["cdx_digest"]
reconciliation = load("metadata/archive-digest-reconciliation.json")
for row in reconciliation:
    if match := row["distribution_content_match"]:
        data = (root/match["stored_path"]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == match["sha256"]
        assert base64.b32encode(hashlib.sha1(data).digest()).decode() == row["cdx_digest"]
# Guard the acquisition check against successful HTTP error-page payloads.
try:
    with Image.open(io.BytesIO(b"<html>200 OK: challenge page</html>")) as im: im.verify()
except Exception:
    pass
else:
    raise AssertionError("HTML error incorrectly accepted as image")
print(json.dumps({"result":"PASS", "stored_assets":len(assets), "decoded_images":images,
    "unique_stored_binary_hashes":len({r["sha256"] for r in assets}),
    "verified_replay_payloads":len(load("metadata/archive-recovered-images.json")),
    "indexed_archive_faces":len(reconciliation),
    "archive_digests_matched_to_preserved_bytes":sum(bool(r["distribution_content_match"]) for r in reconciliation),
    "archive_distinct_payloads_unrecovered":sum(not r["distribution_content_match"] for r in reconciliation)}, indent=2))
