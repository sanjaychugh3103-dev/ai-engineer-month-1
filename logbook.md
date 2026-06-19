## Day 1 — [date] — Environment + repo
Clicked: Repo + venv + pytest scaffold up cleanly.
Fuzzy: nothing
Surprised me: nothing

## Day 2 — [date] — Hello, deployed
Clicked: FastAPI + Render deploy worked.
Fuzzy: nothing
Surprised me: nothing

## Day 3 — [date] — Comprehensions and generators
Clicked: All good — the memory diff was real.
Fuzzy: nothing
Surprised me: nothing

## Day 4 — [date] — Coding muscle
Clicked: Used Counter on Contains Duplicate.
Fuzzy: When to reach for set vs Counter — Claude pointed out a set would have been simpler.
Surprised me: That my "correct" solution was already over-engineered.

## Day 5 — [date] — Tokenisation
Clicked: tiktoken script ran, saw the ratio differences.
Fuzzy: Got the Japanese-vs-English direction right but undershot the size — it's 5-10x, not 1.5x. Worked through it back to: tokenisers trained mostly on English, Japanese falls back to UTF-8 bytes.
Surprised me: That a single emoji can cost 3-5 tokens.

## Day 6 — [date] — From logits to a word
Clicked: Watched temperature 0 vs 0.7 vs 1.5 produce visibly different outputs.
Fuzzy: nothing
Surprised me: nothing

## Day 7 — [date] — Attention, conceptually + repo reorganisation
Clicked: Query/key/value as roles each token plays — looking up vs offering vs delivering. Repo restructure into src/tests/warmups feels right.
Fuzzy: Why three roles instead of one — still a bit abstract. Will revisit in Month 2 when building retrieval.
Surprised me: Why long context windows are computationally expensive — the n² in attention. That's a real constraint not a vague one.

## Day 8 — [date] — The API surface, formalised
Clicked: The second algorithm was tricky but I got there
Fuzzy:Fuzzy: The "why was this designed this way" framing is still developing — I can recite features but the design-rationale framing takes a moment. Lock-in points: choices is a list because of the `n` parameter for multiple completions; the whole point of the wrapper is that swapping providers is a one-file change; system/user separation isn't cosmetic, it's structural in how the model weights them.
Surprised me: Nothing