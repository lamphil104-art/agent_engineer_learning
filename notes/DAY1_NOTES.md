# DAY1 NOTES

Hôm nay tôi đã hoàn thành mini project tóm tắt văn bản ra JSON.

Những gì tôi làm được:
- Tạo môi trường Python
- Kết nối model API
- Thiết kế prompt để ép output về JSON
- Dùng Pydantic để kiểm tra schema
- Lưu kết quả ra file JSON

Điểm tôi học được:
- Prompt rõ schema giúp output ổn định hơn
- Cần parse và validate thay vì tin hoàn toàn vào model
- Đây là bước nền tảng để sau này build RAG và AI agent

- Khi dùng VS Code PowerShell, cần kiểm tra python và pip có thật sự trỏ vào .venv hay không
- Nên dùng python -m pip thay vì chỉ dùng pip
- Nếu bị lệch interpreter, có thể gọi trực tiếp .\.venv\Scripts\python.exe


Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py