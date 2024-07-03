from gitProcess import auto_git_process
import getRagicContents
import checkTxt
import datetime
from datetime import date


getRagicContents.main()
checkTxt.main()


repo_path = "."
commit_message = f"Article Updated {date.today()}"

success = auto_git_process(repo_path, commit_message)
if success:
    print("Git process completed successfully")
else:
    print("Git process failed or no changes to commit")

