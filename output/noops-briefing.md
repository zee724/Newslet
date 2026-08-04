# NOOPS Daily Briefing

- Generated at: 2026-08-04 03:35 UTC
- Feed: https://noops.au/rss
- Items: 8

## 1. [Signal] Qwen open-weights a Max-class model; is Opus 4.8 is now the low-end comparison?

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://qwen.ai/blog?id=qwen3.8

Alibaba released Qwen 3.8-Max on 3 August, describing it as the most capable model in the Qwen family to date and, more consequentially, the first time it will open-source the weights of a Qwen-Max-class model. Mark, who had spent the weekend building a distributed home inference rig, worked out wit

## 2. [Signal] SemiAnalysis publishes on Kimi K3 -- but has Qwen has already overtaken it?

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://www.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the

John shared SemiAnalysis's long-form treatment of Kimi K3 on 4 August and made the observation that matters more than the piece itself: by the time the definitive analysis of a Chinese open-weights release lands, the next one has already shipped and is likely swamping its capabilities. Qwen 3.8-Max

## 3. [Signal] There are no spoons: 20 tokens a second across three home GPUs

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://github.com/mpesce/netferencer

Mark spent the weekend building and then publishing netferencer, which runs a single GGUF model across NVIDIA GPUs sitting in separate Windows PCs using llama.cpp's RPC backend over a private Ethernet segment. One machine acts as coordinator and distributes model layers and KV cache across the avail

## 4. [Signal] The data-centre water argument moves upstream to the power plant

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://www.linkedin.com/posts/alex-de-vries-gao-a5b51349_ai-data-centers-use-far-more-water-than-most-share-7480994696224407552-fIiC

John flagged Alex de Vries-Gao's analysis, circulating on LinkedIn and picked up by the Wall Street Journal, arguing that AI data centres consume far more water than the standard accounts allow — because the water that matters is not only what runs through the cooling loop but what thermoelectric ge

## 5. [Signal] Fifteen hundred data centres meet the county zoning board

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://www.politico.com/news/2026/08/01/data-centers-have-a-politics-problem-and-industry-knows-it-01020412

John shared Politico's 1 August piece on the industry's politics problem, quoting its central passage: fears that the server-packed hubs will drive up electricity prices, deplete water supplies and consume farmland have prompted people across the United States to pack meetings of zoning boards and c

## 6. [Signal] Albanese moves AI oversight inside his own department

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://theconversation.com/view-from-the-hill-albanese-takes-oversight-of-governments-response-to-ai-under-his-own-wing-287494

John shared The Conversation's report that Anthony Albanese has established an Office of AI inside the Department of the Prime Minister and Cabinet, taking direct carriage of the government's response to AI. The office has commenced operations already and will be announced in a major speech on Wedne

## 7. [Signal] A deterministic oracle for agent code: 91.9% branch coverage on COBOL

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://arxiv.org/abs/2607.28271

Mark posted arXiv 2607.28271, which describes the "Locksmith Loop", an agentic test-synthesis method for validating COBOL-to-Java migrations. Both the COBOL source and the generated Java target are instrumented with mocks and executed off-mainframe on commodity hardware. An iterative agentic loop th

## 8. [Signal] Fifteen days into a single prompt, and it is still running

- Published: Tue, 04 Aug 2026 00:44:08 GMT
- Link: https://daringfireball.net/linked/2026/08/02/cherny-claude-swift

Mark shared Daring Fireball's link to Boris Cherny, who put the current state of the craft plainly: the skill now is less about prompt engineering and more about figuring out how to give Claude a hard task that seems a little bit too hard, and then how to make it possible for Claude to verify its wo
