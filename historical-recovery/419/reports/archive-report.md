# Holotable archival investigation â€” Story #419

## Findings established by recovered sources

The old Players Committee host preserved **454 distinct Original Virtual card GIF URLs**, all with earliest successful captures in November/December 2007, under `http://www.swccgpc.com/cards/vN/{ls,ds}/`. This is a much stronger historical source than today's PC card list. `original-virtual-cdx.json` retains exact capture timestamp, URL, MIME, CDX digest and compressed-record length. These are original-era reconstructed full-card faces, not proof of first release text and not publisher slip PDFs.

Set counts: OVS1 11; OVS2 46; OVS3 48; OVS4 49; OVS5 46; OVS6 45; OVS7 21; OVS8 48; OVS9 50; OVS10 14; OVS11 30; OVS12 46. Missing cards/sets are not inferred nonexistent. OVS13â€“17 and the original shields may survive elsewhere or in later Holotable distributions (other research lane).

Validated pilot images are 350Ã—490 GIFs. SHA-1 in Base32 was compared to the historical CDX digest, in addition to calculating SHA-256. `recovered-all-manifest.json` is the authoritative per-file recovery status; indexed/candidate URLs are not counted as recovered images. Source URL, exact replay URL, capture date, retrieval timestamp, dimensions and hashes travel with each successful file. A historic capture timestamp does not establish the publication or errata date.

## Primary historical Holotable pages recovered

- Old News: https://web.archive.org/web/20071124031903id_/http://www.holotable.com:80/oldnews.php
- Interim Updates: https://web.archive.org/web/20071124041653id_/http://www.holotable.com:80/updates.php

Sanitized readable copies are `oldnews-2007-sanitized.txt` and `updates-2007-sanitized.txt`. Raw source HTML is research scratch and contains a personal contact address; do not publish raw HTML without sanitization.

Old News supplies precise contemporary chronology:
- 24 December 2005: OVS11 CDFs updated, images still forthcoming.
- 31 December 2005: OVS11 images released; new full large pack through OVS11 announced, plus separate V11 update.
- 19 July 2005: V10 update described as including small/large images and updated CDFs, about1.6MB; Leia(V) and Han's Heavy Blaster Pistol(V) corrected against changed PC text.
- 24 June 2006: newly errataed virtual-card images available.
- 18 July 2006: redux CDFs available while images still forthcoming.
- 2 September 2006: full redux images forthcoming, credited to Psychobabble.
- 6 January 2007: virtual-card re-edit text included in Holotable0.8.0 but images not yet fixed.

Interim Updates documents historically important image errors:
- OVS3 Leia and Tarkin carried preliminary text.
- OVS12 Debnoli and Mara Jade carried the original white-border preview versions.
- OVS12 Daultay Dofine used the wrong base card (Captain Daultay Dofine, Theed Palace instead of Daultay Dofine, Coruscant), affecting both image and CDF.
- OVS11 I've Lost Artoo incorrectly carried re-edit I Want That Ship text.
- OVS9 Chewie's AT-ST incorrectly retained the nonvirtual base-card text.
- OVS8 The Time For Our Attack Has Come was rendered Effect instead of Immediate Effect; page says Premium PDF also wrong.
These facts make provenance/version comparison necessary even for real historical Holotable files.

The same page supplies direct update filenames: `reduxcdfs.zip`, `june06errata.zip`, `leia.gif`, `tarkin.gif`, `debnoli.gif`, `marajadetheemperorshand.gif`, `daultaydofine.gif`, `ivelostartoo.gif`, `tuskenbreathmask.gif`, `chewiesatst.gif`, `denofthieves.gif`, `thetimeforourattackhascome.gif`, `iwonderwhotheyfound.gif`, `allwrappedup.gif`, `huttbounty.gif`, `jabbasinfluence.gif`, `urorrurrr.gif`, under `/download/downloads/`. Distribution lane has been sent the older download IDs70â€“79 for fullV12/re-edit/update packages.

## Search coverage and negative results

- Archive.org advanced search `holotable`: four unrelated3D-model items, no indexed Holotable software item.
- Broader `(swccg OR "star wars ccg" OR holotable OR starwarsccg) AND (mediatype:software OR mediatype:data)`: ten items, mostly3Dmodels/unrelatedsoftware plus two Yahoo-group WARC collections. Metadata checked; relevant WARC/CDX payloads require authorization (HTTP401). No private messages or personal contacts copied into evidence.
- `holodeck AND (swccg OR starwarsccg OR "card game")`: five unrelated historical broadcast items.
- Wayback successful pre2010 Holotable host index: twelve HTML/robots URLs, no binaries. All-years successful index:169 URLs, including modernpostreset large image packs and a0.9.9Linuxinstall, but no oldV17 or V12 binary URL discovered. Full raw indexes retained.
- `holotable.theforce.net/*` CDX: empty. `holotable.org/*`: unrelated parked-domain pages from2011onward.
- Historical downloads.php first captures verified in CDX for20070211033040,20080217154307,20090414045927; replay repeatedly returned429. Old News and Updates did return real pages.
- TFN domain-wide Holotable URL-filter query returned502; liveTFN existing links are assigned to distribution lane.
- VPS first narrowCDX query succeeded, then the host refused connections. manpc worked intermittently; separate errors retained in receipts.

## Limits, retry discipline, next actions

The bulk pilot uses two workers and0.5second pauses with per-file checkpoints. After repeated429 bot-throttle messages and connection refusals, the owned batch was explicitly stopped and its checkpoint materialized. Do not launch unbounded parallel Wayback crawlers or repeatedly retry blocked captures. Resume after a cooldown with one worker and stop promptly on429; recovered distribution packs may already cover manyfaces. No historical installers were executed, no livewiki pages changed, no publicoutreach sent, no new infrastructure created, and no FlareSolverr sessions opened by this lane.

Use current manifests for exact recovered counts. The remaining indexed-but-unretrieved faces stay explicitly pending; priority He Is Not Ready and other gaps should be retried after service recovers. Additional older exactfilenames from distribution lane can be queried in CDX after cooldown, but repeated throttling is an external source limit rather than a reason to misreport image recovery.


## Final checked state — 14 November 2026

-454 historical candidate URLs catalogued;7 actualGIFs recovered, image-decoded and exactCDX SHA-1 verified;447 remain pending/external-blocked rather than recovered.
-Validated files: OVS1 Assault Rifle(V), Black2(V), Blaster Rack(V); OVS11 Deep Hatred; OVS6 Jabba's Influence; OVS8 Tusken Breath Mask; OVS9 I'm With You Too.
-Visual inspection: I'm With You Too is a full-card LightEffect with footer card10; Tusken Breath Mask is a full-card LightEffect with footer22; Deep Hatred is a full-card DarkEffect. All are350×490 contemporary GIF faces. These checks establish actual card payloads, not an engine/rules interpretation or a complete transcription certification.
-Priority He Is Not Ready retry at14:12:20UTC still returned429; it is not recovered in this lane. Wayback's body reports suspected abusive bottraffic and supplies no Retry-After header. Parent has the exact failure receipt and should resume only after source service recovers.
-All owned processes finished or explicitly stopped: initial archive probe54724 exited0; round2 session56937 exited0; round3 session47914 exited0; pilot75980 exited0; bulk18324 stopped after throttling (ownedPID10612,28ledgerattempts); priorityretry exited0 with429 recorded. No activeFlareSolverr session, tunnel or backgroundjob remains.

Safe publication allowlist: `report.md`, `search-ledger.json`, `original-virtual-cdx.json`, `recovered-all-manifest.json`, `recover-all-ledger.jsonl`, `pilot-manifest.json`, `priority-retry.json`, `round2-receipts.json`, `round3-receipts.json`, `oldnews-2007-sanitized.txt`, `updates-2007-sanitized.txt`, plus the seven validated GIFs. Raw HTML files are intentionally outside this allowlist because historical footer contact details need redaction. Large rawCDX inventories are optional evidence; the454-row OriginalVirtual subset is the useful version inventory.
