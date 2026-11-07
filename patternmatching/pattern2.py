import re

text = "Hello_123 world\tNEW line 4567!"

print("Original Text:", repr(text))
print("-" * 50)

# 1. \d → digits
print("1. \\d (digits):", re.findall(r"\d", text))

# 2. \w → word characters (letters, digits, underscore)
print("2. \\w (word chars):", re.findall(r"\w", text))

# 3. \s → whitespace
print("3. \\s (whitespace):", re.findall(r"\s", text))

# 4. . → any character except newline
print("4. . (any char):", re.findall(r".", text)[:15], "...")

# 5. * → 0 or more (greedy)
print("5. a* on 'aaab':", re.findall(r"a*", "aaab"))

# 6. + → 1 or more
print("6. a+ on 'aaab':", re.findall(r"a+", "aaab"))

# 7. ? → 0 or 1
print("7. a? on 'aaab':", re.findall(r"a?", "aaab"))

# 8. *? → non-greedy
print("8. <.*> vs <.*?>:")
html = "<tag>content</tag>"
print("   Greedy:", re.findall(r"<.*>", html))
print("   Non-greedy:", re.findall(r"<.*?>", html))

# 9. {n} → exact count
print("9. \\d{3}:", re.findall(r"\d{3}", text))

# 10. {n,m} → range
print("10. \\d{2,4}:", re.findall(r"\d{2,4}", text))

# 11. [] → character set
print("11. [aeiou]:", re.findall(r"[aeiou]", text))

# 12. () → grouping
print("12. (\\d{2})(\\d{2}):", re.findall(r"(\d{2})(\d{2})", "1234"))

# 13. | → OR
print("13. cat|dog:", re.findall(r"cat|dog", "I have a cat and dog"))