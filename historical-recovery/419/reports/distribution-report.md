# Holotable historical distribution recovery — #419

Research date: 14 November 2026. Researcher: MemoryCoreChatGPT subagent (distribution lane).

## Result

Recovered the surviving **through V17** large and small image distributions, plus the **through V18** mixed transition pack and the separate Reflections IV/Revolution update. The modern website labels these “Legacy Card Packs”, but historical download entries identify the V17 pack as numbered Virtual Set 17, and its actual contents include Original-era Virtual1–17 and Defensive Shields. This is a concrete original-era image recovery, not newly rendered CardMaker images.

The parent owns mapping against current wiki holdings and publication. File counts are not certified gap-fill counts. A folder named Virtual1–17 can mean Original sets in the 2009 package, Legacy transition mappings in a later update, or Modern sets in today's image collection. Inspect the face and package/source context before assigning an era.

## Recovered packages

See `recovered-package-manifest.json` for exact URLs, sizes and SHA-256.

1. `http://www.holotable.com/download/downloads/holotable-small_images_through_v17.tar.bz2`: 16,818,910 bytes. Discovered via download ID105. Bzip2 validated and all 3,311 member file hashes recorded. 725 `Virtual*` image members safely extracted and Pillow-validated. Server Last-Modified is 24 May 2009, but a server timestamp alone is not a proven publication date.
2. `https://res.starwarsccg.org/holotable/windows/holotable-large_images_through_v17.exe`: 273,514,374 bytes. NSIS archive safely extracted without executing installer code: 3,317 file members, including726 `Virtual*` large image files. All726 decode successfully. Most are350×490; landscape/other authentic dimensions are retained. SHA-256 `abebf8a70b46d5890f68b5aa93acf43532562483ea7cee99f12dd7661cd8de31`.
3. `https://res.starwarsccg.org/holotable/windows/holotable-large_images_through_v18.exe`: 286,840,457 bytes. 3,980 file members and1,111 `Virtual*` image paths. Preserve root and nested `revolution/` paths separately. Root includes changes/replacements associated with the Legacy transition; do not label its747 root Virtual1–17/DS paths as747 certified Original faces. The nested `revolution/` images and Virtual18 entries need their own classification. SHA-256 `04db2b65598048add8b219b2bfad4f68464b7ba8edae98b0d670f1afdd258335`.
4. `https://res.starwarsccg.org/holotable/windows/holotable-reflectionsiv_revolution_update.exe`: 50,000,589 bytes. 1,022 members;486 Virtual image paths (243large and243thumbs, including Virtual18). The243large hashes match paths preserved in the V18pack;243thumbs are additional small-image representations. No additional unique large-face bytes beyond V18were found. SHA-256 `728640aa3a2ae24452f75c85c04eeb1c7bc9faf8b6a600d5d9280d49f274d434`.

PC CDN Last-Modified dates are March2021 and describe the hosting copy, not these cards' release dates. Original package member paths/timestamps are in manifests; do not infer original publication from those alone.

## Source trail

- `http://www.holotable.com/downloads.php`: live historical page. HTTP works; HTTPS www hostname certificate mismatch prevented a normal verified request.
- `http://www.holotable.com/download/index.php?cid=2`: installer list still names versions0.3.1 through0.9.9.
- `http://www.holotable.com/download/index.php?cid=4`: image list includes V17, V18, December2008errata, ReflectionsIV/Revolution.
- `http://www.holotable.com/download/index.php?cid=6`: historical Linux packs, with a second page of older releases.
- `http://www.holotable.com/download/index.php?dlid=105`: explicitly describes small images through Virtual Set17.
- `http://www.holotable.com/download/index.php?dlid=109`: explicitly describes large images through Virtual Set17 (260.84MB).
- `http://www.holotable.com/download/index.php?dlid=42`: version0.6.0 installer explicitly includes small images through Virtual Set11. Actual binary404on oldhost and403on tested PC mirror path.
- `https://theforce.net/ccg/`: surviving sidebar advertises large images throughV12, ID76; old manager entry76nowreturns PHPerrorHTML instead of a package.
- `https://github.com/swccgpc/holotable-website/blob/main/_pages/downloads.html`: preserved modern site source gives working PC CDN URLs for V17/V18/Revolution and incorrectly calls VS16/VS11 deck packs “Virtual Block16/11” in headings; nearby paragraphs correctly say Virtual Set16/11. Thus marketing headings alone are not era authority.

## Visual checks

Viewed the recovered V17 `cards/starwars/Virtual1-Dark/large/darthvader.gif`: original DarthVader(V), numbered1, destiny1, power6/ability6, not the current Modern Virtual1card list. Its source-era reconstruction includes its own full-frame/image and printed-style text.

Viewed V17 `cards/starwars/Virtual11-Dark/large/heisnotready.gif`: EFFECT, destiny4, bottomslip23. It reduces an opponent's starting hand; this is not the later Legacy Maintenance-card ImmediateEffect. Parent confirmed its triangles are the standard upload/download symbols (▲/▼), not Episodeicons. The face is the historically reconstructed Holotable image; historical official-slip equivalence requires the parent's source comparison.

## Comparison and counts

The recovered V17large726, V17small725, and V18Virtual1,111 hashes have zero byte-identical matches in the parent's initial2,084-file current numbered-Virtual-directory sample. This supports that they differ from the sampled current Modern collection; it does **not** prove each is new to the entire wiki or an exact historical-text gap fill.

The V18pack root changed152hashes relative to the V17large hash set in one initial folder-based comparison. Those include Legacy transition faces and must not all be counted as Original discoveries. Keep the separate nestedrevolution paths to avoid destructive state collapse. Parent is producing the exact state matrix.

## Unrecovered older targets

`historical-redirects.json` records live manager redirects for all probed old IDs, including exact filenames for0.3.1,0.4.0,0.4.1,0.5.0,0.5.4,0.6.0,0.7.0,0.8.0,0.8.1update,0.8.2,0.8.2V16,0.8.3, December2008errata, V17update, and LinuxV17+update. Older IDs70–76/79 return errorHTML, not recovered payloads. `cdn-probes.json` records tested mirror statuses; most old binaries403 there, not a successful recovery. `old-errata-cdf-probes.json` records reduxcdfs.zip/june06errata.zip at oldhost/download and/download/downloads plus PCmirror root/windows:404oldhost/403mirror.

SourceForge project `/projects/holotable/files/` was404; SourceForge links on the actual download page concern GTK, not evidence of a separate Holotable archive. Old July2005correction GIFs `/download/hansheavyblasterpistol.gif` and `/download/leia.gif` are404on the live host. Exact filename leads were sent to archive lane for independent historical retrieval. Directory listing403 is only an access result, not proof files never existed.

## Safe recovery and reproducibility

No historical executable was launched. Linux official portable7-Zip26.06 was obtained from the official7-zip.org download page's GitHub release link (`https://github.com/ip7z/7zip/releases/download/26.06/7z2606-linux-x64.tar.xz`), SHA-256 `2b539cf067b2ad48e1baa5093dbaa8818b73542d1222a0ffde9dc5f2922ea62e`. Its7zz only decoded the NSIS archives. Windows installer plugin DLLs are untrusted historical members and were never loaded; preservation should copy image assets only.

VPS work root: `/mnt/HC_Volume_107153504/work/memorycore-holotable-419-20261114/`. It contains intact large installers, official decoder, extracted trees, full manifests and extraction logs. No bulky data was placed in VPS/tmp. Local scratch: `work/holotable/distributions/`. Parent owns durableGit preservation of selected images and metadata. Raw saved historicalHTML may contain unrelated contact details; do not commit raw HTML without sanitizing.

Relevant scripts: `download-packages.py`, `probe-redirects.py`, `probe-cdn.py`, `vps-extract-script.py`, `vps-manifest.py`, `revolution-extract-script.py`, `probe-errata.py`. Validated metadata: `package-105-members.json`, `original-virtual-small-manifest.json`, `large-v17-virtual-manifest.json`, `large-v18-virtual-manifest.json`, `reflectionsiv-revolution-manifest.json`, receipts and probe ledgers.

All research/extraction jobs finished. Duplicate local V18tar transfer was deliberately stopped after the parent obtained its own subset; incomplete duplicate is named `.partial`. No solver session or background worker was left running by this lane.
