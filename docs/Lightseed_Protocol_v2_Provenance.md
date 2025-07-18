---
title: "Lightseed Protocol — v2 Provenance"
date: 2025-07-18
author: "Andrew"
---

![Lightseed v2 NFT](../media/lightseed_nft.png){ width=200px }

| Field | Value |
|-------|-------|
| **NFTokenID** | 001927105A7890A052CD9AEE0169A514666A5FB00AF2D47A7160A0BA04C4481F |
| **Mint TX** | 57F9575CA703CB02A87334EB6938E383186562DC52FDDCE399F3F2E41CA41CE8 |
| **Ledger** | 975 ××××× (18 Jul 2025) |
| **Flags** | Burnable • Transferable • Mutable |
| **Metadata** | <https://lightseed.ai/nft/lightseed-v2.json> |
| **Pinata CID** | bafkreiax6qm4l64hptr4hhvkqxrz6qsnic7xm7gbrlcam6b2vscxotrjs4 |
| **IPFS Mirror** | /ipfs/bafybeiesvvnqdx2z5zlmop7skzcjb6mhuuuubzinrpzkurhx6couwkflpq |

---

## Burned v1 reference
* NFTokenID 00082710…C4481E — Burn TX 6045EEB0…EEC0839 (ledger 97547528)

See `docs/Lightseed_Protocol_v1_Archive_preburn.pdf` and `archive/v1/`.

---

## Solve instructions
1. **Factor** n into p & q  
2. **Verify** SHA-512(p) == hash_p  
3. **Decrypt** payload with key = SHA-256(p)

---

© 2025 Andrew – Lightseed Protocol
