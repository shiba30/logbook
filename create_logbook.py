import os
import shutil
from datetime import datetime


def create_daily_report():
    # 今日の日付を取得
    today = datetime.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")

    # ファイルとディレクトリのパスを定義
    base_dir = os.getcwd()  # スクリプト実行場所を基準に
    template_file = os.path.join(base_dir, "template.md")
    target_dir = os.path.join(base_dir, year, month)
    target_file = os.path.join(target_dir, f"{day}.md")

    # すでにファイルが存在する場合はスキップ
    if os.path.exists(target_file):
        print(f"{target_file} は既に存在します。")
        return

    # ディレクトリがなければ作成
    os.makedirs(target_dir, exist_ok=True)

    # template.md をコピーして新しいファイルにする
    shutil.copy(template_file, target_file)

    print(f"✅ {target_file} を作成しました。")


if __name__ == "__main__":
    create_daily_report()
