def leetspeak_variants(word):
    substitutions = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7']
    }
    variants = set([word])
    for i in range(len(word)):
        char = word[i].lower()
        if char in substitutions:
            for sub in substitutions[char]:
                variant = word[:i] + sub + word[i+1:]
                variants.add(variant)
    return list(variants)

def append_years(words, years=[2023, 2024, 2025]):
    return [f"{word}{year}" for word in words for year in years]