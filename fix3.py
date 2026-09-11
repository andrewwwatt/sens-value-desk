# -*- coding: utf-8 -*-
with open('/tmp/svd-fix/ratings.html') as f:
    c = f.read()

old_agree = '''27 reviews where SENS Value Desk and Ticker Talk agree: NRP (both bullish), BHG (both bullish), ABG (both bullish), TGA (both bullish), SPP (both bearish), RCL (both bearish), FFB (both neutral), DSY (both bullish), IMP (both bullish), SSW #1 (both bearish), WHL (both neutral), SOL (both bullish), BVT (both bullish), FSR (both bullish), SLM (both neutral), CPI (both neutral), OUT (both neutral), OMU (both bullish), AVI (both bullish), GRT (both neutral), SPG (both neutral), SSW #2 (both neutral), BWN (both neutral), SUI (both bullish), HYP (both bullish), LSK (both bullish), CLH (both neutral).'''

new_agree = '''26 reviews where SENS Value Desk and Ticker Talk agree: NRP (both bullish), BHG (both bullish), ABG (both bullish), TGA (both bullish), SPP (both bearish), RCL (both bearish), FFB (both neutral), DSY (both bullish), IMP (both bullish), SSW #1 (both bearish), WHL (both neutral), SOL (both bullish), BVT (both bullish), FSR (both bullish), SLM (both neutral), CPI (both neutral), OUT (both neutral), OMU (both bullish), AVI (both bullish), GRT (both neutral), SPG (both neutral), SSW #2 (both neutral), BWN (both neutral), SUI (both bullish), HYP (both bullish), LSK (both bullish).'''

assert old_agree in c
c = c.replace(old_agree, new_agree)

old_disagree_end = '''<div class="disagree-item">
<b>PAN (Pan African Resources):</b> SENS Value Desk BULLISH vs Ticker Talk BEARISH. Ticker Talk read the post-results 6% share-price sell-off as the market signalling disappointment with management's operational execution. This desk read the same sell-off as profit-taking after a huge 52-week run rather than a fundamental red flag — production, pricing and cost metrics all came in consistent with or ahead of prior guidance, and a self-calculated ~8x multiple on disclosed HEPS looks statistically cheap for the growth delivered. The disagreement is really about how much weight to put on one day's price reaction versus the disclosed operational detail.
</div>
</div>'''

new_disagree_end = '''<div class="disagree-item">
<b>PAN (Pan African Resources):</b> SENS Value Desk BULLISH vs Ticker Talk BEARISH. Ticker Talk read the post-results 6% share-price sell-off as the market signalling disappointment with management's operational execution. This desk read the same sell-off as profit-taking after a huge 52-week run rather than a fundamental red flag — production, pricing and cost metrics all came in consistent with or ahead of prior guidance, and a self-calculated ~8x multiple on disclosed HEPS looks statistically cheap for the growth delivered. The disagreement is really about how much weight to put on one day's price reaction versus the disclosed operational detail.
</div>
<div class="disagree-item">
<b>CLH (City Lodge Hotels):</b> SENS Value Desk BULLISH vs Ticker Talk NEUTRAL. This desk's own first-pass review also read NEUTRAL before a same-day correction: the initial writeup relied on a pre-results guided HEPS range and missed that a 5% statutory profit decline was entirely an impairment/FX item, not operating weakness, and that management backed 20% adjusted HEPS growth with a R153m buyback (6.4% of shares in issue) and a 27% dividend increase. On the corrected facts, this desk rates it Bullish; Ticker Talk's Neutral call was made on the same information and reasonable people can weigh the buyback-vs-fair-multiple trade-off differently, but the corrected version is what's reflected in the rating above.
</div>
</div>'''

assert old_disagree_end in c
c = c.replace(old_disagree_end, new_disagree_end)

with open('/tmp/svd-fix/ratings.html', 'w') as f:
    f.write(c)
print("comparison section updated, len", len(c))
