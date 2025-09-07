from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    return {
        'score': result['score'],
        'feedback': result['feedback'],
        'crack_times': result['crack_times_display'],
        'sequence': result['sequence']
    }
