import subprocess

file = r"do\code_4_1.py"
cmd = f"python {file}"
res = subprocess.run(
    cmd,  # コマンド関数
    capture_output=True,  # 出力結果を取得
    text=True,  # 出力結果をテキストで表示
)

print(res.stdout)
