# The World in One Day — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/littleghoul/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard)
[![reward](https://make.fun/badge/news-image-20261125/littleghoul/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

One picture that sums up Wednesday, 25 November 2026. It is laid out like
the front page of a newspaper: a large headline story across the top, the
other five stories arranged around it, each with a short caption so a reader
can grasp the day at a glance. See the bounty page for the contest:
https://make.fun/bounty/news-image-20261125

## Stories in this image

- 霍尔木兹海峡油轮触雷爆炸——两艘油轮周三凌晨在海峡触雷后爆炸起火，伊朗革命卫队海军警告船只须协调通行。
- 特朗普在海湖庄园见北约秘书长吕特——欧洲力求加入美方主导的乌克兰和平谈判。
- 巴基斯坦首位宇航员升空——神舟二十四号发射，Muhammad Zeeshan Ali 成为首位进入轨道的巴基斯坦人，也是首位登上天宫空间站的外国宇航员。
- 俄乌夜间空袭——周三凌晨袭击基辅、哈尔科夫、扎波罗热和萨马拉，造成 3 死 15 伤。
- 第二名哈马斯安全首脑在加沙被炸死——周三黎明以军空袭炸死哈马斯安全首脑 Muhammad Abu al-Ouf 及其妻女，24 小时内第二起。
- 英伟达反弹熄火——周二股价跌 5.86% 至 155.38 美元；黄仁勋告诉员工自己在接受心理治疗。

## How it runs

`main.py` reads the bundled `entry.png` and writes it unchanged to
`/output/entry.png`. It uses no network and no randomness, so running it
twice produces byte-identical output. After writing, it checks that the
number of bytes on disk matches the picture it read, then hashes the
written file with SHA-256 and compares it against the picture's own
digest, failing if they differ, and prints the count and the digest.

## License

MIT — see `LICENSE`.
