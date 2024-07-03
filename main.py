from gitProcess import auto_git_process
import getRagicContents
import checkTxt
import datetime
from datetime import date


getRagicContents.main()
checkTxt.main()

now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
repo_path = "."
commit_message = f"Article Updated {now.strftime('%Y/%m/%d %H:%M:%S')}"

success = auto_git_process(repo_path, commit_message)
if success:
    print("Git process completed successfully")
else:
    print("Git process failed or no changes to commit")

