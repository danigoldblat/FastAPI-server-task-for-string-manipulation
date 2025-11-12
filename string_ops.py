def reverse_str(s: str) -> str:
    return s[::-1]
def to_upper(s: str) -> str:
    return s.upper
def remove_vowels(s: str) -> str:
    vowels=["a","e","i","o","u"]
    for i in s:
        if i == vowels:
            s=s.replace(i,"")
    return s 
def remove_every_third(s: str) -> tuple[str, list[int], list[str]]:
    