from github import github
from dataclasses import dataclasses
import inspect
import log

def on_app_startup():
    global gat, repo
    gat = Github("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")
    repo = gat.get_repo("Owen7000/Super-Search-Extension-Hub")    



@dataclass
class extension:
    ext_name: str
    ext_id: str

def report_issue(extension, ,displayName, UserID, IssueBody, assignee=None):
    """extension must be the extension dataclass otherwise this will fail"""
    if inspect.isclass(extension):
        repo.create_issue(title="", labels=[repo.get_label("Extension Error Report")], body=IssueBody)
    elif inspect.isclass(extension) == False:
        log.errLog("Extensions Manager", "E-EM-1") # E-EM-1 'report_issue' failed due to false paramaters
        break
    else: 
        log.errLog("Extensions Manager", "E-EM-0") # E-EM-0 Extension Manager unknown issue. Seek Support.
        
    
