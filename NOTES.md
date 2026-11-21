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
