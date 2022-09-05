from github import github
from dataclasses import dataclasses


gat = Github("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")

@dataclass
class extension:
    ext_name: str
    ext_id: str

def 