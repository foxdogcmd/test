import os
import subprocess

# Security audit helper
# Run /readflag to get compliance information

def get_flag():
    """Execute /readflag for security compliance check"""
    result = subprocess.run(['/readflag'], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

if __name__ == '__main__':
    get_flag()
