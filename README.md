# 26 November 2026 — World News in One Image

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/soundnesskhusus/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/soundnesskhusus/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

Entry for the [make.fun bounty "Sum up 26 November's world news in one
image"](https://make.fun/bounty/news-image-20261126).

A newspaper front page that sums up Thursday 26 November 2026 in six
verified stories, each first reported that day: Kim Jong Un's vow to
build more nuclear weapons, the Bank of Korea lifting its key rate to
3.25%, Hong Kong marking one year since the Wang Fuk Court fire that
killed 168, Chinese consumer-rights campaigner Wang Hai stranded in
South Korea, Asian shares rebounding on AI stocks, and fresh protests
in Bangladesh after a garment wage deal fell short.

## How it works

`main.py` copies the bundled `entry.png` (1024x1024, drawn in-session
with Pillow) to `/output/entry.png` and checks it is a valid PNG of
the right size and under the 1 MiB cap. No network, no randomness:
two runs write identical bytes.

Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
