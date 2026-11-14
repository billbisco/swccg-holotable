# Holotable forum/source-history investigation — Story #419

Researcher: MemoryCoreChatGPT subagent `holotable_forums_git`, 14 November 2026. No live wiki/board edits, messages to outsiders, installer execution, infrastructure changes or detached jobs.

## Findings

### 1. Preserved historical vkit image collection: 857 PNGs

Public repository: https://github.com/ledwards/swccgvkit-legacy

Fixed commit: `b91efe46d4603d36ab975f4f2346059b4de17dd3`, 28 May 2010 06:04:01 UTC, “Removed old svn directories”. Predecessor `81e004826e5697f45d10c4330f78ff8136dae46f`, same day 05:53:57, “First commit (migrated from svn to git)”. Only two commits are listed. The final tree still retains `.svn` content under `public/images/vslips/`.

Original downloaded source ZIP: https://codeload.github.com/ledwards/swccgvkit-legacy/zip/b91efe46d4603d36ab975f4f2346059b4de17dd3

- ZIP bytes: 178,215,741; SHA-256 `de71edb61391a1e40edb1e02073e05247a4f2dc5c1a1a20016163eefd4ca5671`.
- 2,649 extracted vslip subtree files including SVN metadata and duplicated text bases.
- 857 actual PNGs, 92,680,885 bytes, 838 distinct PNG SHA-256 hashes.
- 722 PNGs in folders labelled Virtual1–17, 26 in Virtual6.2 folders and 109 in Virtual18 folders. These are source folder labels, not independently verified era classifications. Virtual18/6.2 must be separated during exact identity mapping.
- All 857 PNGs opened and verified with Pillow. 645 are shorter than250px,192 taller than400px; others have intermediate heights. The tallest files often have white masks over artwork or only partial graphics: **do not call these857full-card reconstructions**.
- `.svn/entries` timestamps span9–10December2009, not the original2002–2009 release dates. They provide retained source-working-copy metadata, not independent authentication of each text state’s release day.
- Every `.svn/text-base/*.png.svn-base` is byte-identical to its working PNG. No additional text states were recovered from SVN backups.
- Baseline manifest: `vkit-recovered-manifest.json`, per-directory totals `vkit-counts.json`; original Git tree `vkit-legacy-tree.json`; PNG inventory `vkit-legacy-image-inventory.json`; SVN comparison `svn-content-comparison.json`.
- Extracted image subtree: `vkit-recovered/public/images/vslips/`. Preserve this asset subtree and metadata; the complete downloaded application ZIP is scratch/source retrieval material, not a request to republish old application configs.

Important identity warning: `virtual11-light/marajadetheemperorshand.png` visibly carries the title Mara Jade With Lightsaber and an art mask. Filename, title and set attribution must be checked against the actual face; filename matching alone is insufficient.

### 2. Historical announcement trail in the current Holotable website source

Repository: https://github.com/swccgpc/holotable-website at `661f2690f60695cedc52d4dfac4a6be14679696e`. Preserved posts were migrated to Git in2021; their displayed dates are historical news headings, not2005Git commits. Earliest Git commit `4b6b1af94afc7d6beb46c5f9b2fba8faf2c2953b` is24Jan2021.

Primary paths under `_posts/` establish where to search for historical packs:

| Displayed date | Post | Evidence/lead |
|---|---|---|
|25Jan2005|2005-01-25-news.html|Installer included Virtual Set8 definitions; mixing different image/CDF packages could cause missing images.|
|8Feb2005|2005-02-08-news.html|Holotable withdrew its own corrected premium-set versions after PC versions appeared; confirms these are not automatically publisher-authoritative faces.|
|26May2005|2005-05-26-news.html|Virtual Set9 update included large images, thanking multiple volunteers.|
|19Jul2005|2005-07-19-news.html|V10 installer included small/large images and CDFs, approximately1.6MB.|
|31Dec2005|2005-12-31-news.html|V11 image update and full through-V11 large pack.|
|24Jun2006|2006-06-24-news.html|Interim Updates ZIP supplied newly errataed Virtual card images.|
|18Jul2006|2006-07-18-news.html|Redux CDFs preceded nearly50pending image changes.|
|6Jan2007|2007-01-06-news.html|Re-edit CDFs released; images lagging.|
|9Jan2007|2007-01-09-news.html|Psychobabble’s re-edit images and revised CDFs available.|
|12–13Jan2007|2007-01-12/13-news.html|V12 images/CDFs released and consolidated through-V12 packs, approximately240MB.|
|27–30Jan2007|2007-01-27/30-news.html|TheForce.net hosting replaced old IP-address/holotable paths.|
|29Sep2007|2007-09-29-news.html|V13, current errata and V14 previews update.|
|27Jan2008|2008-01-27-news.html|Interim fixes for rotated V13smallimages, old Oh SwitchOff errata and three grabber shields.|
|11Jul2009|2009-07-11-news.html|V18 preview cards available, thanks to Mark VanDriel.|

Source link example: https://github.com/swccgpc/holotable-website/blob/661f2690f60695cedc52d4dfac4a6be14679696e/_posts/2005-05-26-news.html

**Migration trap:** inline old-news image links were rewritten to current `res.starwarsccg.org/.../Virtual0-*` paths. Those current destinations must not be interpreted as Original-era evidence. Retrieve historical faces separately.

The current `_pages/downloads.html` has a misleading “Legacy Card Packs” heading but points to original-numbered through-v17/v18 installers. Those concrete URLs were passed to the distributions agent, who owns their recovery:
- https://res.starwarsccg.org/holotable/windows/holotable-large_images_through_v17.exe
- https://res.starwarsccg.org/holotable/windows/holotable-large_images_through_v18.exe
- https://res.starwarsccg.org/holotable/windows/holotable-reflectionsiv_revolution_update.exe

TheForce.net’s live CCG sidebar also advertises the through-V12 large image pack: https://theforce.net/ccg/. Distributions agent was notified. The contemporary TFN repost of the6Jan2007 announcement is https://www.theforce.net/latestnews/story/New_Version_of_Holotable_Available_102851.asp .

### 3. PC forum and repository limits

`https://forum.starwarsccg.org/viewtopic.php?t=25909` was the25Feb2009Advocate Holotable thread in earlier saved board listings. Live retrieval on14Nov2026 via existing VPS FlareSolverr(no named session) returned genuine HTTP200forum information page: **“The requested topic does not exist.”** This is not a Cloudflare block. Raw scratch receipt `forum-25909-fetch.json`; script `forum_fetch.py`. Archive agent has the historical `/forums/viewtopic.php` lead. No credentials or contact details belong in published excerpts.

Searches for old Holotable image/update posts mostly returned modern Reset-era discussions, whose set numbers collide with Original numbers. Examples checked as search results, not evidence of Original images:
- https://forum.starwarsccg.org/viewtopic.php?t=54289 (status thread from2014, edited modern install instructions).
- https://forum.starwarsccg.org/viewtopic.php?p=1304091 (Set12update in2020, Modern era).
- https://forum.starwarsccg.org/viewtopic.php?t=65510 (2017higher-resolution scans, post-Reset).

`swccgpc/holotable` currently has1,478commits. Earliest commit `022435b7929e4de26dafbcb1de2ec1d6d04d2153` is8Jul2018, labelled Set9load. Its6330-entry tree has Modern Virtual0–9 directories, not pre2009history. Seven public forks were enumerated; earliest fork created20Aug2019. They cannot establish a pre2009commit history merely by being forks. Stored initial/current tree JSONs document this boundary.

Other pre2015repositories checked by API trees:
- `ledwards/swccgvkit`: later Rails app,2010CDF snapshots but no corresponding original image collection in current tree.
- `ledwards/swccgonline-legacy`:12,095tree entries;3,578image/binary entries approximately22.8MB including SVN duplicates. Its card tree retains Original-named thumbnail GIFs (e.g.Virtual1Dark/t_assaultrifle.gif), generally~5KB. Useful filename/image cross-check, lower recovery priority than full faces. Not downloaded wholesale because another agent already recovered Holotable thumbnail/full packs.
- `ledwards/swccgonline`:190entries,2010CDFs and UIimages, no large card collection.
- `annedlrseown/swccgdb`:16entries, one UIimperial image.
- `oglimmer/deckbuilderswccg`:48entries, UItheme images, no card-face collection.

## Priority text comparisons (visually inspected)

### I’m With You Too, OriginalVS9
Recovered vkit PNG: `virtual9-light/imwithyoutoo.png`, SHA256`13c81f8b86550b0e9be9d8acae900ee834307cd56ca1d05e6977dd14ae68a670`,350x164. Face has9seticon,10Eslipmark, with the familiar3Forcebattle-destiny cancellation wording. Compare wiki snapshot `wiki-imwithyoutoo.json`: same current recorded text. **This is a historical asset/provenance recovery, not a recovery of the missing pre17Sep2007 wording.** Icon is EpisodeI (not Scomp).

### Tusken Breath Mask, OriginalVS8: three distinct recovered renderings
All are evidence candidates; none should be called the recovered missing publisher PDF simply because wording differs.

| Source | Visual state | Key distinction |
|---|---|---|
|PC archived face recovered by archive agent|350x490; slip22withoutE;8seticon|Deployment anywhere on table; ability bonus at occupied location can last through turn, alternatively absorbs battle damage.|
|Holotable through-v17 pack|350x490;22E|Exterior Tatooine battleground-site restriction; applies an added total-ability bonus during battle.|
|vkit-legacy overlay|350x164;22E|Same restricted site, but the bonus clause omits the wordtotal.|
|Current wiki quote of Remaster/17Sep2007sheet|Snapshot`wiki-tuskenbreathmask.json`,rev284555|Expresses total ability as+X rather than an additive bonus; different wording from both recovered22Erenderings.|

vkit overlay SHA256`a0046786f6dc092174a436bb231f76d9c629920b649b697943d00bcbb1607a1f`. Cross-agent source hashes/paths in `tusken-source-comparison.json`. Need actual primary sheet/announcement dating before promoting these differences to dated official errata. The archive agent owns its capture timestamp; preserve its receipt. The2009SVNdates do not prove thevkitwordingwas the missingDecember2006state.

## Search ledger / reproducibility

Commands/scripts saved locally:
- `repo_inventory.py`: GitHub metadata/current trees.
- `vkit_inventory.py`: old vkit image inventory.
- `recover_vkit.py`: fixed-commitZIPretrieval, subtree-onlysafe extraction, SHA256 and Pillowverification (does not execute software).
- `pre2015repos.py`: alternative repository inventories.
- `samples.py`: priority raw PNG samples and SVNmetadata.
- `forum_fetch.py`: no-sessionVPSFlareSolverr forum retrieval.

Search phrases covered Holotable plus VirtualSet9/12/17, re-edit, Psychobabble,2006/2007/2009images, and GitHubholotable/SWCCG created before2015. Generalsearch results have substantial false positives from other games and currentModernsets; primary filenames/datednews were favored.

## Next steps and limits

1. Parent integrates image subtree + hashmanifest into the preservation branch; no new public outreach needed.
2. Map722Original1–17-labelledvkitPNGs, separately reviewVirtual6.2/18, and compare against the recoveredfullHolotablepacks. Whole-artmaskedoverlay crops are not substitutes for full-card scans.
3. Prioritize the threeTuskenrenderings and originalVS9–12 candidatefaces against actual PDFs. Record possible rendering/transcription discrepancies without inventing official dates.
4. Original2004–2007CDF/imageupdatepackages and gone2009forumthread may still hold earlier states; archiveagent handles checked archive paths. CurrentGit2018history alone cannot answer them.

All local processes launched by this agent have exited. FlareSolverr used without named session; no orphaned browser session/tunnel was created.
