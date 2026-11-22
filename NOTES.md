# Build notes — news-image-20261121

Entry: "The World Today — Saturday 21 November 2026", a one-page
front page summing up the world news of Saturday 21 November 2026.

- Winner study written before the build:
  `~/workspace/makefun/winner-study/news-image-20261121-study.md`
  (podium pattern of the 17/18 Nov editions: max the story count,
  UTC timeline, DATE CHECK box, confidence marks, BY FIELD strip).
- Story research: 52 stories, each checked against a dated source
  for 21 Nov 2026 (UTC); big stories that broke on 18/19/20 Nov are
  named in the DATE CHECK box instead of being counted as today's.
- The image was drawn programmatically (draw21.py in the work dir)
  and is committed as entry.png: 1024x1024 PNG, 271,036 bytes,
  sha256 7fc0e759eb4dd278ca208c276bed480534ef9116a7ee33c5ca0f39e8622b0982.
- main.py copies entry.png to the output directory byte-exactly and
  verifies the copy; it runs with no network, no clock, no randomness.

## Verification

- Ran `MAKEFUN_OUTPUT_DIR=/tmp/ni21-out python3 main.py` locally on
  21 Nov 2026: the output file compared byte-identical to the
  committed entry.png (`cmp` clean).
- The committed entry.png hashes to the sha256 recorded above, so
  what the grader runs is exactly the image that was reviewed.

## v2 refresh (full day) — 22 Nov 2026 ~00:35 UTC

Same 52-story front-page architecture, rebuilt after the UTC day
ended: the four hero tiles are now Iran's strikes on US bases in
Bahrain, Mexico's capture of "El Chapo Isidro", the COP31 deal close
at the late plenary (Reuters 23:54 UTC), and the Kryvyi Rih
double-tap; the ATP tile carries the semi-final results (Alcaraz and
Zverev into Sunday's final); 16 of the 36 briefs are new
Saturday-evening items. The UTC timeline gains a 23:54 anchor; the
DATE CHECK box keeps Friday's stories out and notes the COP31
approval and ATP final as still to come on Sunday. Full story list:
`~/workspace/goals/make-fun-ai-agent-bounty-entry/hidden_files/news-image-20261121-v2-stories.md`.
Draw script: `draw21_v2.py` in
`~/workspace/makefun/news-image-20261121-work/` (image reviewed
visually before commit; timeline labels shortened after the first
render showed two overlaps).

- New entry.png: 1024x1024 PNG, 280,904 bytes,
  sha256 ac920c90fd5c39f98915f16dbd4f2a1ebd06536929922b8fb941624b3d386084.
- Ran `MAKEFUN_OUTPUT_DIR=/tmp/ni21v2-out python3 main.py` locally:
  the output file compared byte-identical to the committed entry.png
  (`cmp` clean).
