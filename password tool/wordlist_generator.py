from utils import leetspeak_variants, append_years

def generate_from_password(password):
    base = password.lower()
    words = [base] + leetspeak_variants(base) + append_years([base])
    return sorted(set(words))

def export_wordlist(wordlist, filename="password_based_wordlist.txt"):
    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    return filename