# Historical Holotable and vKit recovery — Story #419

Recovered on 14 November 2026 for [Story #419](https://github.com/swccg-guild/work/issues/419). These are preserved source assets, not new CardMaker renders. Existing active image paths are unchanged.

## Collection

- `large-v17/`: 726 original-era full-card image paths from the through-Virtual-Set-17 installer; mostly 350×490 GIFs, including sets 1–17 and original Defensive Shields. Counts include alternative/back images and are not a count of distinct card identities.
- `small-v17/`: 725 original-era thumbnail paths. `packages/` retains the complete untouched small-image archive as well.
- `transition-content/`: additional unique content from the through-V18 mixed transition pack, stored by SHA-256. `metadata/large-v18-path-to-content.json` reconstructs all 1,111 package Virtual-image paths using these files or the identical V17 bytes. Root and nested revolution paths remain separate.
- `revolution-thumbnails/`: additional small representations from the Reflections IV/Revolution update. Its large faces duplicate V18 content; `metadata/revolution-path-to-content.json` reconstructs all 486 Virtual-image paths.
- `vkit-legacy/`: 857 PNG source assets from ledwards/swccgvkit-legacy, fixed commit b91efe46d4603d36ab975f4f2346059b4de17dd3. These are predominantly slip overlays/partial faces, sometimes with blank art masks. There are 838 distinct PNG hashes. Original-numbered folders, Virtual6.2 and Virtual18 remain separate; source labels do not certify era. Application configs and SVN duplicate files are not republished.
- `archive-2007/`: seven full-card GIFs retrieved from 2007 Wayback captures. Each payload's SHA-1 matches the archive CDX digest, with a separately recorded SHA-256.
- `reports/`: primary-source excerpts and three search reports. Contact addresses have been removed from historical excerpts; image originals remain byte-identical.

## Provenance and use

[Large V17 source](https://res.starwarsccg.org/holotable/windows/holotable-large_images_through_v17.exe), [V18 source](https://res.starwarsccg.org/holotable/windows/holotable-large_images_through_v18.exe), [Revolution update](https://res.starwarsccg.org/holotable/windows/holotable-reflectionsiv_revolution_update.exe), [small V17 source](http://www.holotable.com/download/downloads/holotable-small_images_through_v17.tar.bz2), [vKit source commit](https://github.com/ledwards/swccgvkit-legacy/tree/b91efe46d4603d36ab975f4f2346059b4de17dd3).

Source URLs, retrieval receipts, package SHA-256, per-image hashes/dimensions, member paths and mixed-era warnings are under `metadata/`. Complete large installers and extraction logs are also retained in the existing volume-backed research storage; the installers were decoded with official 7-Zip, never executed. Source application code/configs are not needed to use these images. All copyright/credit markings in recovered images remain intact; no ownership or new licence is asserted.

## Important historical differences

The 2007 archived Tusken Breath Mask face (slip22) deploys on table and has an alternative battle-damage function. The V17 face22E uses a restricted Tatooine site and additive total ability. The vKit22E overlay has yet another wording (omitting total). The archived I'm With You Too face differs from the later V17/vKit face. These are historical reconstruction states; they do not by themselves authenticate the missing first-release publisher PDFs or date an official errata.

The historical Holotable Updates page explicitly documents preliminary text, a wrong host card, and other reconstruction errors. Match actual face and source before assigning a wiki version. Today's Modern folders reuse Virtual-set numbers; V18 transition directories also contain later cards under old-numbered paths. Do not bulk overwrite wiki images from filenames.

## Archive reconciliation and remaining limits

454 distinct old PC Original Virtual GIF URLs were indexed from 2007 captures. Seven replay payloads were downloaded and digest-verified. Independently comparing the saved assets' SHA-1 against the CDX digests identifies matching bytes for **427 of the 454 indexed faces** (425 already in the distributions plus two different recovered archive faces). This is a digest-backed recovery of historical content, **not** a claim that 427 Wayback replays were fetched or that each is new to the wiki. The remaining 27 distinct indexed payloads have no exact match in this collection and remain research targets. `archive-digest-reconciliation.json` records the distinction.

447 replay requests remain unverified/pending in the archive retrieval ledger, many of which are now available as byte-identical distribution content. Wayback throttled further requests with HTTP429; restricted Yahoo-group WARC payloads returned401. Failed/throttled entries never count as downloaded or verified replays. Earlier VS6/9/10/11/12 PDFs remain missing unless independently found elsewhere; this recovery does not silently close those gaps.

## Verification

Run `python verify.py` from this directory with Pillow installed. `asset-inventory.json` binds every stored binary to bytes and SHA-256; every image must decode, and both source-path mapping manifests must resolve to the recorded bytes. The same checks were run before publication.
