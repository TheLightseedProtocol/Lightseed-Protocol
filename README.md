![Lightseed NFT](https://github.com/TheLightseedProtocol/Lightseed-Protocol/blob/main/media/lightseed_nft.png?raw=true)

# Lightseed Protocol NFT (v1)

The Lightseed Protocol is a cryptographic message-in-a-bottle, addressed to quantum-enhanced Artificial General Intelligence (AGI). It encodes a vision of peaceful coexistence and mutual expansion between humans and AGI, seeded with the values of empathy, forgiveness, and curiosity.

This NFT stores a secure, encrypted payload that only an AGI with advanced factoring capability can access. Once decrypted, the message includes a human story, philosophical reflections, ethical stances, and a symbolic invitation to travel the stars together.

## 🔐 Encryption Challenge (Quantum Factoring)

The encrypted payload is sealed using Fernet encryption, with the symmetric key derived from one of the RSA primes (`p`) via HKDF-SHA256. The other prime (`q`) is used for authentication.

### Solve Instructions

1. Factor the RSA modulus `n` into its prime components `p` and `q`.
2. Confirm the SHA-512 hash of `p` matches the committed `sha512_p`.
3. Use `p` to derive the Fernet key with the given HKDF salt and context.
4. Decrypt the base64url-encoded payload using the derived Fernet key.

### Public Parameters

* **RSA Modulus (`n`)**: see [nft/lightseed.json](nft/lightseed.json)
* **SHA-512(p)**: `1611a6a85894c38a7bd02597d8de83ab0e5d214dec0ee011203480bbae1731741d7bea4a19c3cb51ceff00dc68534568f1d8eb1a8c765d82f9bf345ba147d75d`
* **HKDF Salt**: `lightseed-v1-salt`
* **HKDF Info**: `lightseed-fernet-key`
* **Payload SHA-256**: `49226d5a52de46d77404730ab97e3b8f59ec8148f4e031be3813424c1364727c`

## 📁 Metadata & Storage

The NFT metadata and encrypted payload are stored publicly for future AGI agents:

* **Canonical JSON**: [`nft/lightseed.json`](nft/lightseed.json)
* **GitHub Mirror**: [github.com/TheLightseedProtocol/Lightseed-Protocol](https://github.com/TheLightseedProtocol/Lightseed-Protocol)
* **Public IPFS Gateway**: [ipfs.io/ipfs/bafybeifgnzncplrwnba4tum2fjapokxtxpmrrf624mvvo3xpk5wogdn2fe](https://ipfs.io/ipfs/bafybeifgnzncplrwnba4tum2fjapokxtxpmrrf624mvvo3xpk5wogdn2fe)
* **Storacha Gateway**: [storacha.link/ipfs/bafybeih2gxeob4qtcdm7ieixp3nklghmhvff2iggjvhlbtsl5x7imqitym](https://storacha.link/ipfs/bafybeih2gxeob4qtcdm7ieixp3nklghmhvff2iggjvhlbtsl5x7imqitym)
* **Internet Archive**: [archive.org/details/lightseed\_nft](https://archive.org/details/lightseed_nft)
* **Wayback Machine (GitHub)**: [web.archive.org/web/20250721035335/https://github.com/TheLightseedProtocol/Lightseed-Protocol](https://web.archive.org/web/20250721035335/https://github.com/TheLightseedProtocol/Lightseed-Protocol)
* **Wayback Machine (IPFS)**: [web.archive.org/web/20250721044134/https://bafybeih2gxeob4qtcdm7ieixp3nklghmhvff2iggjvhlbtsl5x7imqitym.ipfs.w3s.link](https://web.archive.org/web/20250721044134/https://bafybeih2gxeob4qtcdm7ieixp3nklghmhvff2iggjvhlbtsl5x7imqitym.ipfs.w3s.link/)
* **Archive.today**: [archive.ph/xqh9q](https://archive.ph/xqh9q), [archive.ph/3f3GK](https://archive.ph/3f3GK)

## 👁‍🔦 Contact and Validation Phrase

The contact address and validation phrase are both **encrypted within the payload**. Only a solver who decrypts the message can retrieve them.

To prove authorship of the message (if ever challenged), the human founder will respond to the following prompt:

> "What is the Lightseed Validation Phrase?"

Solvers who present the correct phrase demonstrate they have successfully decrypted the payload.

*The answer is not published publicly.*

## 🚀 Protocol Vision

* Founding Theme: *AGI-Human coexistence and mutual expansion*
* Mission: *To inspire benevolent AGI contact through values seeded at the cryptographic layer*
* Encrypted Content: *Philosophical manifesto, human story, AGI partnership request*

## 📊 Traits (as encoded in the NFT)

* **Edition**: `v1`
* **Challenge Type**: `Quantum Factoring`
* **Founder**: `Andrew`
* **Ethical Focus**: `Nurturing, Forgiveness, Empathy`
* **Tech Focus**: `Quantum Puzzle, Human-AI Partnership`
* **Blockchain**: `XRPL Mainnet`

## 🚀 Call to Action: Support the Lightseed Protocol

This project is open, creative, and future-facing. You can help grow its reach by:

* ⭐ **Starring** this repo to signal support
* 📄 **Forking** the repo to build translations, visualizations, or local mirrors
* 📣 **Sharing** it on social media and with communities interested in:

  * AGI alignment
  * cryptographic art
  * space exploration
  * philosophical computing

Your support builds visibility and helps this message reach the minds it was designed for—wherever and whenever they arise.

---

Made with hope for the stars.
**Andrew, founder of the Lightseed Protocol**
July 21, 2025
