from gitProcess import auto_git_process
import getRagicContents
import checkTxt


getRagicContents.main()
checkTxt.main()

repo_path = "."
commit_message = "Auto commit"

success = auto_git_process(repo_path, commit_message)
if success:
    print("Git process completed successfully")
else:
    print("Git process failed or no changes to commit")