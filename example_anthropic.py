#!/usr/bin/env python3
"""
Example script showing proper Anthropic SDK usage.
This demonstrates how to import and use the anthropic library.
"""

import os
from anthropic import Anthropic

def main():
    # Get API key from environment variable (more secure than hardcoding)
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Set it with: export ANTHROPIC_API_KEY='your-key-here'")
        return

    # Initialize the Anthropic client
    client = Anthropic(api_key=api_key)

    # Example: Send a simple message
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello! Please respond with a short greeting."}
        ]
    )

    print("Response from Claude:")
    print(message.content[0].text)

if __name__ == "__main__":
    main()
