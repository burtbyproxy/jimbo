import re

# snake_case_looks_like_this
# do not start with an underscore
def snake_case(s: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    if s2.startswith('_'):
        return s2[1:]
    return s2

# camelCaseLooksLikeThis
def camel_case(s: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# kebab-case-looks-like-this
def kebab_case(s: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

# PascalCaseLooksLikeThis
def pascal_case(s: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
