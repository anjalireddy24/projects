import argparse
from analyzer import analyze_password
from wordlist_generator import generate_from_password, export_wordlist

def run_cli():
    parser = argparse.ArgumentParser(description="Password Analyzer + Wordlist Generator")
    parser.add_argument("--password", required=True, help="Password to analyze")
    parser.add_argument("--output", default="password_based_wordlist.txt", help="Output filename")

    args = parser.parse_args()

    print("\n🔍 Password Analysis:")
    result = analyze_password(args.password)
    print(f"Score: {result['score']}/4")
    print("Feedback:", result['feedback'])
    print("Crack Times:", result['crack_times'])

    print("\n🧪 Generating Wordlist...")
    wordlist = generate_from_password(args.password)
    export_wordlist(wordlist, args.output)
    print(f"✅ Wordlist saved to {args.output}")