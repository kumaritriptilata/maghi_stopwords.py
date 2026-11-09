# -*- coding: utf-8 -*-
"""
Magahi (मगही) stop words, 200 entries.

Magahi has no standardized orthography or published stop word list, so this
list is compiled from common function words, and spellings vary by region.
Validate against a native speaker or a Magahi corpus frequency count before
using it for anything graded or published.
"""

PRONOUNS = [
    "हम", "हमनी", "हमरा", "हमर", "हमन",
    "तू", "तूँ", "तोहर", "तोरा", "तोहनी", "तोहरा", "तोहन",
    "ऊ", "उ", "ओकर", "ओकरा", "ओकन्हीं", "ओहे",
    "ई", "इ", "एकर", "एकरा", "एहे",
    "आप", "आपन", "अपन", "अपना", "अपने", "खुद", "जे",
]

POSTPOSITIONS = [
    "के", "केर", "कर", "कऽ", "में", "मे", "से", "सँ", "पर", "पे",
    "ला", "लगी", "लागी", "खातिर", "तक", "ले", "संगे", "साथे", "साथ",
    "बिना", "बगैर", "बिन", "सिवाय", "अलावा", "द्वारा", "बारे", "तरफ",
]

CONJUNCTIONS_PARTICLES = [
    "आउ", "आ", "अउर", "और", "आर", "मगर", "लेकिन", "बाकि", "बाकी",
    "कि", "त", "तो", "तऽ", "भी", "भि", "ही", "हीं", "या", "चाहे",
    "अगर", "जउ", "जब", "तब", "तउ", "तइयो", "फेर", "फिन", "फिर",
    "काहेकि", "ताकि", "जइसे",
]

INTERROGATIVES = [
    "का", "काहे", "कउन", "कौन", "केकरा", "केकर", "कहाँ", "कब",
    "कइसे", "कैसे", "केतना", "कतना", "कइसन", "केन्ने", "कथी", "कन्ने", "कते",
]

DEMONSTRATIVES_ADVERBS = [
    "एतना", "ओतना", "जेतना", "तेतना", "एहाँ", "ओहाँ", "इहाँ", "उहाँ",
    "जहाँ", "तहाँ", "एन्ने", "ओन्ने", "जन्ने", "अइसन", "ऐसन", "ओइसन",
    "जइसन", "तइसन", "ऐसे", "वइसे", "एजा", "ओजा", "अब", "अभी", "अबहीं",
    "तुरंत", "हमेशा", "कखनो", "कभी", "कहियो",
]

QUANTIFIERS = [
    "सब", "सभे", "सब्भे", "सभ", "कुछ", "कुच्छो", "कोई", "कोनो", "केकरो",
    "हर", "हरेक", "एक", "दू", "दुन्नो", "दोनों", "ढेर", "बहुत",
    "थोड़ा", "कम", "बेसी", "जादा",
]

POSITION_TIME = [
    "पहिले", "पाछे", "पीछे", "बाद", "बादे", "सामने", "ऊपर", "उप्पर",
    "नीचे", "तर", "भीतर", "भित्तर", "बाहर", "बहरा", "बीच", "बिचे",
    "आगू", "आगे", "नगीच", "दूर",
]

NEGATION = [
    "नञ", "नय", "नइ", "न", "नहिं", "नै", "नहीं", "मत",
]

AUXILIARY_VERBS = [
    "हइ", "हे", "हय", "हथ", "हथिन", "हल", "हलइ", "हलन", "हो",
    "होवे", "होल", "गेल", "गेलइ", "रहल", "रहे", "सकऽ",
]

MAGAHI_STOPWORDS = frozenset(
    PRONOUNS
    + POSTPOSITIONS
    + CONJUNCTIONS_PARTICLES
    + INTERROGATIVES
    + DEMONSTRATIVES_ADVERBS
    + QUANTIFIERS
    + POSITION_TIME
    + NEGATION
    + AUXILIARY_VERBS
)


def remove_stopwords(text: str) -> list[str]:
    """Whitespace-tokenize `text` and drop Magahi stop words."""
    tokens = text.replace("।", " ").split()
    return [t for t in tokens if t not in MAGAHI_STOPWORDS]


if __name__ == "__main__":
    print(f"{len(MAGAHI_STOPWORDS)} unique stop words loaded")
    sample = "हम बजार जा रहल ही आउ तू घर में हा"
    print(remove_stopwords(sample))
