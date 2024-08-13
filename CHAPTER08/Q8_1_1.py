import os
def pr_dir(dir_name="save_dir"):
    if os.path.exists(dir_name):
        print("ディレクトリ '{}' が存在します。".format(dir_name))
    else:
        os.mkdir(dir_name)
        print("ディレクトリ '{}' を作成しました。".format(dir_name))

pr_dir()

pr_dir()
