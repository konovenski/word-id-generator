#!/usr/bin/env python3
from word_id_generator import generate_id

print("Press Enter to generate a new ID (Ctrl+C to exit)")
while True:
    try:
        input()
        print(generate_id())
    except KeyboardInterrupt:
        break