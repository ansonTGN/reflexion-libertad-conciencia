#!/usr/bin/env python3
"""Compatibility entrypoint: regenerate the five-language site safely."""
from build_multilingual import render, CODES

if __name__ == '__main__':
    for code in CODES:
        print(render(code))
