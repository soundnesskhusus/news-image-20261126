# 26 November 2026 — World News in One Image

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/soundnesskhusus/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/soundnesskhusus/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

Entry for the [make.fun bounty "Sum up 26 November's world news in one
image"](https://make.fun/bounty/news-image-20261126).

A newspaper front page that sums up Thursday 26 November 2026 in six
verified stories, each first reported that day (evening edition, v2
refresh of the morning entry): Ukraine's overnight drone strikes on a
Transneft oil hub in Bashkortostan and the Marinovka airfield, Bulgaria
backing the €45bn EU loan for Ukraine but only its civilian part,
UniCredit moving to take over the Commerzbank board, Rwanda hiking its
key rate to 9.5% as inflation hit 19.5%, Dutch groups asking a court to
halt sales of Meta's AI smart glasses, and US chip curbs slowing
China's AI labs.

## How it works

`main.py` copies the bundled `entry.png` (1024x1024, drawn in-session
with Pillow) to `/output/entry.png` and checks it is a valid PNG of
the right size and under the 1 MiB cap. No network, no randomness:
two runs write identical bytes.

Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
