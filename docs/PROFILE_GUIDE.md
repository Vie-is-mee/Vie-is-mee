# Hướng dẫn duy trì hồ sơ An Vi

README định hướng AI Engineer Intern, dùng tiếng Anh để đồng nhất với portfolio/CV hiện tại.

## Cách sắp xếp

1. Tên, vị trí mục tiêu và đường dẫn CV/liên hệ.
2. Chuyên môn: retrieval/RAG, machine learning và tích hợp hệ thống AI.
3. Ba dự án theo thứ tự người dùng chọn: **UIT-ChatBot → OneVoice-Lab → SolarOpt**. Nêu bài toán, phương pháp, sản phẩm và liên kết kiểm tra; chỉ ghi vai trò cá nhân khi có nguồn xác nhận.
4. Nghiên cứu/cuộc thi có metric và bối cảnh thứ hạng; giữ thành tích Hedge Fund ở đây thay vì phần dự án nổi bật.
5. Công nghệ theo nhóm, học vấn và liên hệ.
6. Biểu đồ đóng góp trong mục thu gọn cuối trang.

Không đưa streak, số lượt xem, giờ code, số dòng code, snake/pacman hoặc danh sách logo dài từ Blu vào hồ sơ. Các phần này không giải thích được đóng góp kỹ thuật.

## Nguồn nội dung

Đối chiếu ngày 13/10/2026. Đây là nguồn công khai do chủ hồ sơ cung cấp, không phải một đợt xác minh độc lập mọi thành tích.

| Nội dung | Nguồn |
| --- | --- |
| Tên An Vi và vị trí AI Engineer | Người dùng xác nhận trong cuộc trò chuyện. |
| Học vấn, thời gian học, email, LinkedIn, CV | [Portfolio nguồn](https://github.com/Vie-is-mee/NguyenVoAnVi_Portfolio/blob/main/index.html). |
| Vai trò, 274 chunks / 84 webpages, đóng góp UIT Chatbot | Phần dự án trong portfolio; [repository](https://github.com/Vie-is-mee/UIT-ChatBot), `backend/requirements.txt` và `frontend/package.json` xác nhận cấu trúc/công nghệ. |
| LightGBM, walk-forward, 1.45 triệu dòng, 7/982 | [README dự án](https://github.com/Vie-is-mee/Hedge-fund_Time-series-forecasting). Giữ cách diễn đạt “reported” và ghi rõ kết quả đội. |
| OneVoice-Lab | [README](https://github.com/Vie-is-mee/OneVoice-Lab), `onevoice_runtime_bridge.py`, `requirements-runtime.txt`, `backend/requirements.txt` và [CLAIM_BOUNDARY.md](https://github.com/Vie-is-mee/OneVoice-Lab/blob/main/CLAIM_BOUNDARY.md). Mô tả chức năng hệ thống, không tự nhận vai trò cá nhân, huấn luyện mô hình, độ chính xác hoặc tốc độ chưa được xác nhận. Ghi rõ cần checkpoint R4 riêng và trạng thái thử nghiệm local. |
| CLEF và EXACT | Phần nghiên cứu trong portfolio. Giữ nhãn kết quả được công bố trên hồ sơ, liên kết paper/leaderboard và bối cảnh “Round 2 snapshot”; chưa xác minh độc lập paper/leaderboard. |
| SolarOpt | [README dự án](https://github.com/Vie-is-mee/SolarOpt); giữ trạng thái MVP kỹ thuật. |

## Cập nhật trước khi ứng tuyển

- Kiểm tra CV, email, LinkedIn và demo; xác nhận CV công khai là bản muốn gửi.
- Với dự án nhóm, chỉ giữ công việc bản thân thực hiện. Bổ sung PR/commit khi có để đối chiếu vai trò.
- Khi có số liệu mới, ghi tập dữ liệu, metric và điều kiện đo. Tách kiểm thử phần mềm khỏi chất lượng mô hình.
- Ưu tiên repository có hướng dẫn chạy, đánh giá, kết quả và giới hạn rõ ràng.
- Không thêm mức tăng accuracy, giảm latency, số người dùng, giải thưởng hoặc trạng thái production khi chưa có bằng chứng.

## Đưa lên GitHub

Khi cập nhật tiếp, sử dụng checkout Git của repository **Vie-is-mee/Vie-is-mee**, lấy thay đổi mới nhất rồi commit/push các tệp `README.md`, `docs/PROFILE_GUIDE.md` và `.github/workflows/profile-3d.yml` theo nhu cầu. Tạo commit mới trên lịch sử hiện có, không force-push. Giữ thư mục `profile-3d-contrib/` để ảnh hiển thị.

Xem trước README trong IDE bằng **Markdown: Open Preview to the Side**. Không cần web server hoặc cài package.

Workflow chỉ cập nhật ảnh đóng góp, không sửa README. Để ảnh tự cập nhật, bật GitHub Actions và bảo đảm chính sách repository cho phép `GITHUB_TOKEN` ghi nội dung. Có thể chạy thủ công qua `workflow_dispatch`.
