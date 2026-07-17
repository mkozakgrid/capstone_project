import re

def is_http_domain(domain: str) -> bool:
    return re.match(fr"(https?:\/\/)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/)?", domain) is not None