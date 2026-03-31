# Chapter 6 — Using Primary Islamic Sources

Part I gave you the legal architecture. This chapter teaches you how to use the **primary sources** that the BOL itself recognizes: the Qur'an, the Sunnah (Hadith collections), and the scholarly tradition built on them.

BOL Art. X, Sec. 3 names four sources of Shari'ah: the Qur'an and Sunnah as principal sources, and Ijma' (consensus) and Qiyas (analogy) as secondary sources.[^1] If you are going to research Shari'ah topics, draft legislation with Islamic references, or produce legal analysis that cites scriptural authority, you need to know how to find, verify, and cite these sources.

This chapter shows you how.

---

## 6.1 Why Practitioners Need Access to Primary Sources

Three situations require you to work with primary Islamic sources:

**Legislative drafting.** When a bill has a Shari'ah dimension, the explanatory note or WHEREAS clauses may cite Qur'anic verses or Hadith narrations as the scriptural basis for the legislation. These citations must be exact — the Arabic text and its English translation, with a proper source reference.

**Legal analysis.** When producing a Shari'ah legal opinion (Chapter 7), you need to trace the scriptural basis for a legal position. "Islamic law prohibits interest" is a claim. The Qur'anic verse that supports it — Surah Al-Baqarah (2):275 — is the evidence.

**Policy work.** When writing a legislative briefer's Shari'ah analysis section or a policy recommendation that invokes Islamic principles, sourcing those principles from the primary texts gives the analysis authority. An unsourced claim about "what Islam says" has no weight in a professional document.

---

## 6.2 Building Your Own Islamic Source Library

You need two categories of sources: the Qur'an and the major Hadith collections.

### The Qur'an

The Qur'an has **114 surahs** (chapters) containing over 6,200 ayat (verses). For legislative and legal research, you need a searchable text with both Arabic and English.

**Recommended translations:**
- **Sahih International** — the most widely used English translation for legal and academic purposes. Clear, literal, with minimal interpretation.
- **Muhammad Muhsin Khan** — used alongside Sahih al-Bukhari translations. More interpretive, includes parenthetical explanations.

**Digital sources:**
- **quran.com** — free, searchable, multiple translations. Provides API access for bulk download.
- **Tanzil.net** — plain-text Quran in multiple scripts and translations. Designed for data use.

**What to look for:** A format where each ayah is individually addressable (you can find Surah 2, Ayah 282 directly), with Arabic text and English translation side by side. This is essential for accurate citation.

**Tafsir (Commentary):** Classical Qur'anic commentary helps you understand the context and scholarly interpretation of verses. The most widely referenced is **Tafsir Ibn Kathir (Abridged)** — a standard reference across the Sunni schools. It is available digitally through quran.com and other platforms.

### The Kutub al-Sittah (Six Major Hadith Collections)

The Hadith collections preserve the sayings, actions, and approvals of Prophet Muhammad (SAW). Six collections are recognized as the most authoritative in Sunni Islam:

| # | Collection | Arabic | Compiler | Books | Authority |
|---|-----------|--------|----------|-------|-----------|
| 1 | **Sahih al-Bukhari** | صحيح البخاري | Imam al-Bukhari (d. 870 CE) | 97 | Highest — most rigorously authenticated |
| 2 | **Sahih Muslim** | صحيح مسلم | Imam Muslim (d. 875 CE) | 57 | Second highest — paired with Bukhari as the "Two Sahihs" |
| 3 | **Sunan Abu Dawud** | سنن أبي داود | Imam Abu Dawud (d. 889 CE) | 43 | Strong on legal rulings (*ahkam*) |
| 4 | **Jami' at-Tirmidhi** | جامع الترمذي | Imam at-Tirmidhi (d. 892 CE) | 49 | Includes hadith grading commentary |
| 5 | **Sunan an-Nasa'i** | سنن النسائي | Imam an-Nasa'i (d. 915 CE) | 51 | Detailed on worship and transactions |
| 6 | **Sunan Ibn Majah** | سنن ابن ماجه | Imam Ibn Majah (d. 887 CE) | 38 | Broadest coverage; some unique narrations |

**Digital sources:**
- **sunnah.com** — free, searchable, Arabic + English. The standard digital reference for all six collections.
- **hadith-api** (fawazahmed0 on GitHub) — JSON API for bulk download. Enables building your own searchable local library.

**Format:** Each collection is organized by *kitab* (book) and individual hadith number. A citation reads: "Sahih al-Bukhari, Book 34, Hadith 19." You need a format where each hadith has the Arabic text and English translation with this numbering.

### Organizing Your Sources

For effective research, organize your source library so you can **search by keyword** across collections. The ideal setup:
- One file per book within each collection (e.g., "01-Revelation.md" through "97-Tawhid.md" for Bukhari)
- Arabic text in blockquotes, English translation below
- Consistent heading format (`### Hadith N`) so you can grep across files
- An INDEX.md for each collection listing all books with hadith ranges

This structure lets you search for a topic (e.g., "debt" or "marriage") across all collections and find every relevant narration with its exact text.

---

## 6.3 Hierarchy of Authority

When you find relevant sources, their weight depends on their position in the hierarchy:

**Tier 1: Qur'an** — the highest authority. A clear Qur'anic verse on a subject settles the matter unless scholarly interpretation (*tafsir*) indicates otherwise.

**Tier 2: Sahih al-Bukhari and Sahih Muslim** — a hadith found in both collections is called *muttafaq 'alayh* (agreed upon) and carries the strongest hadith authority. A hadith in Bukhari alone is still very strong; Muslim alone slightly less so.

**Tier 3: Sunan collections** (Abu Dawud, Tirmidhi, Nasa'i, Ibn Majah) — authoritative, but individual narrations must be assessed for authentication grade. Tirmidhi helpfully includes his own grading for many hadith.

**For practitioners:** Search Bukhari and Muslim first. If you find the narration there, you have the strongest possible hadith evidence. Then search the Sunan collections for additional narrations or for topics that the Two Sahihs do not cover.[^2]

---

## 6.4 Research Methodology: Finding Relevant Scriptural Sources

When you need to find what the Qur'an and Hadith say about a topic, follow this method:

**Step 1: Identify search terms.** Start with the obvious English keyword. Then add synonyms and related concepts. For "trade," also search "commerce," "buying," "selling," "merchant," "market."

**Step 2: Search the Qur'an.** Search your Qur'an files by English keyword. When you find a match, read the full ayah — the surrounding verses often provide context. Check whether the surah is Makki (revealed in Makkah — typically theological) or Madani (revealed in Madinah — often contains legal provisions). Madani verses are more likely to contain provisions relevant to legislation.

**Step 3: Check the Tafsir.** For each relevant verse, read the classical commentary. Ibn Kathir provides the scholarly context: why the verse was revealed, how the early community understood it, and how scholars have applied it.

**Step 4: Search the Hadith collections.** Start with Bukhari and Muslim. Search by keyword in the English translations. When you find a relevant narration, note the book name and hadith number.

**Step 5: Cross-collection verification.** When you find a hadith in one collection, search the others for the same narration. A hadith reported in multiple collections is stronger. Note all occurrences.

---

## 6.5 Cross-Collection Verification and *Muttafaq 'Alayh*

A hadith reported in both Sahih al-Bukhari and Sahih Muslim is called ***muttafaq 'alayh*** — agreed upon by the two most rigorous compilers. This status carries special weight.

**How to verify:** When you find a hadith in Bukhari, search Muslim for the same narration (it may use slightly different wording but convey the same meaning). If found in both, cite the Bukhari version as primary and note "Also reported in Sahih Muslim, Book [N], Hadith [N]."

**Why this matters for legislation:** When citing a hadith as the scriptural basis for a bill or resolution, a *muttafaq 'alayh* narration is practically unchallengeable on grounds of authenticity. A hadith from a single Sunan collection may face questions about its authentication grade.

---

## 6.6 The Madhhab Dimension: Shafi'i/Hanafi Practice in the Philippines

PD 1083 predominantly reflects the Hanafi and Shafi'i schools of jurisprudence as practiced by Filipino Muslims. The Shafi'i school is dominant in maritime Southeast Asia — including the Bangsamoro region.

**Practical implications:**
- When multiple *madhhab* positions exist on a subject, note which school's position is most relevant to the Philippine context
- When PD 1083 codifies a position, that position becomes enacted law regardless of which school it originates from
- For matters beyond PD 1083, present the Shafi'i/Hanafi position as the default with other school positions noted where they differ materially

**When to present all four schools:** If you are drafting a bill on a subject where the schools disagree and the disagreement affects the legal outcome (e.g., the rules for *waqf* irrevocability), present all four positions so Parliament can make an informed legislative choice.[^3]

---

## 6.7 Worked Example: Researching a Shari'ah Topic from Scratch

> **Scenario:** You are asked to find the scriptural basis for *waqf* (Islamic endowment) to support a proposed "Bangsamoro Waqf Act."
>
> **Step 1: Search terms.** "Endowment," "waqf," "charity," "sadaqah jariyah" (ongoing charity).
>
> **Step 2: Qur'an search.** Search for "charity" and "spend" in the Qur'an files. Key finds:
> - Surah Al-Baqarah (2):261 — "The example of those who spend their wealth in the way of Allah is like a seed of grain that sprouts seven ears..."
> - Surah Al-Imran (3):92 — "Never will you attain the good until you spend from that which you love."
>
> **Step 3: Hadith search.** Search Bukhari and Muslim for "endowment" and "charity":
> - Sahih Muslim — narration of 'Umar ibn al-Khattab endowing land in Khaybar: the Prophet (SAW) advised him to "give it in charity with the condition that it not be sold, gifted, or inherited" — widely considered the foundational hadith for *waqf*.
>
> **Step 4: Cross-collection.** The Khaybar endowment hadith appears in multiple collections — verify in Bukhari, Abu Dawud, and others.
>
> **Step 5: Compile results.** Present the Qur'anic verses and the foundational hadith with exact Arabic text and English translation. Note that all four Sunni schools recognize *waqf*, though they differ on irrevocability (Hanafi allows revocation under certain conditions; Shafi'i holds waqf is irrevocable).
>
> **Step 6: Cite.** Format citations per the footnote protocol (Chapter 7, Section 7.1).

---

## Common Pitfalls

- **Citing from memory.** Never cite a Qur'anic verse or Hadith from memory. Always verify against the source text. Misquoting scripture in an official document is a serious error.
- **Using only one collection.** If a hadith exists in Bukhari, check Muslim too. Cross-collection verification strengthens the citation and may reveal additional relevant narrations.
- **Ignoring the Makki/Madani distinction.** A Makki verse about general principles may be less directly applicable to legislation than a Madani verse about specific legal provisions.
- **Presenting one school's position as universal.** If the Shafi'i school holds a position, say "the Shafi'i school holds..." — not "Islamic law requires..."
- **Skipping the Tafsir.** A verse read in isolation can be misunderstood. The classical commentary provides the scholarly context that practitioners need.

---

## Quality Checklist

Before submitting any work product with scriptural citations:

- [ ] Have you verified every Qur'anic verse against the source text (Arabic + translation)?
- [ ] Have you verified every Hadith against the source text with collection, book, and hadith number?
- [ ] Have you checked whether the Hadith appears in multiple collections (*muttafaq 'alayh*)?
- [ ] Have you noted which *madhhab* position you are presenting?
- [ ] Have you checked the Tafsir for context on Qur'anic verses?
- [ ] Have you used the correct citation format (Surah name, number:ayah for Qur'an; Collection, Book, Hadith for Hadith)?

---

[^1]: Rep. Act No. 11054, art. X, sec. 3.
[^2]: The hierarchical ranking of Hadith collections (Bukhari highest, followed by Muslim, then the four Sunan) is the standard classification in Sunni Hadith scholarship. A narration found in both Bukhari and Muslim (*muttafaq 'alayh*) carries the strongest possible Hadith authority.
[^3]: The predominance of Shafi'i jurisprudence in maritime Southeast Asia, including the Bangsamoro, is documented in scholarship on Islam in the Philippines. PD 1083's provisions on marriage, divorce, and inheritance reflect Hanafi and Shafi'i positions.
