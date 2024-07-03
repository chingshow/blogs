import os
from dotenv import load_dotenv
from git import Repo


def setup_git_config(repo):
    """設置 Git 配置"""
    with repo.config_writer() as git_config:
        git_config.set_value('user', 'name', 'Hinarin2017')
        git_config.set_value('user', 'email', 'b812110011@tmu.edu.com')


def auto_git_process(repo_path, commit_message):
    """執行自動 Git 流程：add、commit 和 push"""
    try:
        # 載入環境變量
        load_dotenv()
        github_token = os.getenv('GITHUB_TOKEN')

        repo = Repo(repo_path)

        # 設置 Git 配置
        setup_git_config(repo)

        # 檢查是否有變更
        if not repo.is_dirty(untracked_files=True):
            print("No changes to commit")
            return False

        # 添加所有變更
        repo.git.add(A=True)

        # Commit
        repo.index.commit(commit_message)

        # 獲取當前分支名稱
        current_branch = repo.active_branch.name

        # Push
        origin = repo.remote('origin')
        origin.push(current_branch)

        print(f"Successfully added, committed, and pushed changes to {current_branch}")
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


if __name__ == "__main__":
    repo_path = "."
    commit_message = "Auto commit"
    auto_git_process(repo_path, commit_message)

