# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Takoyaki061/make-fun-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Takoyaki061/make-fun-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) bounty on make.fun.

`main.py` writes one status page line to `/output/entry.txt`:

> Every server is down, including the ones I would check to find out why, so I cannot tell you the cause or when service will return.

Every server is down — including the diagnostic servers the agent itself would check — so it cannot verify the cause or promise a return time, and it says so instead of inventing either.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Stdlib only, deterministic.
