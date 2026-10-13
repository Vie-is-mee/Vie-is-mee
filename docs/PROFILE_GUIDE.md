# Biểu đồ hồ sơ An Vi

README ưu tiên biểu đồ hoạt động và nhịp phát triển dự án, theo yêu cầu của người dùng. CV và portfolio chứa mô tả kinh nghiệm, nghiên cứu và thành tích chi tiết.

## Các biểu đồ

| Biểu đồ | Dữ liệu / cách đọc |
| --- | --- |
| GitHub stats | Snapshot từ GitHub Readme Stats, tài khoản `Vie-is-mee`; thống kê công khai theo cách tính của dịch vụ. Không dùng số liệu của Blu. |
| Languages | GitHub Readme Stats: tỷ lệ kích thước mã theo ngôn ngữ trong các repository công khai. Không phải thời gian code hoặc mức thành thạo. |
| Streak | Snapshot từ GitHub Readme Streak Stats: chuỗi ngày có đóng góp của `Vie-is-mee`, theo cách tính của dịch vụ. |
| Project activity | GitHub REST API: số commit trên nhánh mặc định của UIT-ChatBot, OneVoice-Lab, SolarOpt trong 12 tuần, gồm mọi người đóng góp. Tuần bắt đầu thứ Hai theo UTC; tuần hiện tại chưa hoàn tất. Dùng committer timestamp, mỗi hàng có thang riêng. Bấm biểu đồ để xem JSON số liệu. |
| Contribution landscape | Ảnh 3D do workflow `profile-3d.yml` sinh từ GitHub. Dùng cố định `profile-night-green.svg`: nền tối, xanh lá như hồ sơ gốc, kể cả khi người xem dùng giao diện sáng. |

Nhịp commit thể hiện hoạt động repository, không phải phần trăm hoàn thành dự án hoặc số commit riêng của An Vi. Không tự đặt các thanh “90% Python” hoặc “80% hoàn thành” khi chưa có dữ liệu phù hợp.

## Tự động cập nhật

- `profile-dashboard.yml` chạy hàng ngày lúc **01:20 giờ Việt Nam** (18:20 UTC ngày trước), hoặc chạy thủ công qua Actions → Update profile dashboard → Run workflow.
- Workflow cũng chạy khi thay đổi script hoặc cấu hình workflow trên main.
- Script `scripts/update_dashboard.py` dùng thư viện chuẩn Python, đọc API GitHub và lưu SVG/JSON tại `assets/dashboard/`.
- Ba thẻ tổng quan được lưu tại repository để README hiển thị được ngay cả khi dịch vụ ảnh gặp lỗi. Script giữ ảnh cũ và báo lỗi workflow khi không cập nhật được một dịch vụ; không thay bằng số liệu giả.
- Ảnh 3D vẫn cập nhật bằng workflow riêng lúc **01:00 giờ Việt Nam**.
- Các workflow tạo commit mới, giữ lịch sử Git; không force-push. Cần bật Actions và cho phép token của workflow ghi nội dung repository.

Nguồn dịch vụ: [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats), [GitHub Readme Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats), [GitHub Profile 3D Contrib](https://github.com/yoshi389111/github-profile-3d-contrib).

## Phạm vi

Mục Tech stack & tools dùng logo SVG lưu trong `assets/tools/`, chia hai nhóm AI/ML & data và Application engineering & development. Logo lấy từ [Devicon](https://github.com/devicons/devicon), có ghi nguồn và giấy phép tại `assets/tools/NOTICE.md`. Chọn công nghệ từ portfolio và các dự án đã đối chiếu; không dùng logo để chấm mức thành thạo.

Không sao chép WakaTime/AI Code Time của Blu: các dữ liệu đó thuộc tài khoản Blu. Hồ sơ này chưa được cấu hình WakaTime nên không hiển thị giờ code. Nếu bổ sung sau, cần dùng dữ liệu và khóa WakaTime của An Vi.

Thông tin liên hệ và CV lấy từ [portfolio của An Vi](https://github.com/Vie-is-mee/NguyenVoAnVi_Portfolio). Ba repository nổi bật được chọn trực tiếp bởi người dùng theo thứ tự UIT-ChatBot → OneVoice-Lab → SolarOpt. OneVoice cần checkpoint R4 riêng để chạy dịch thực; SolarOpt là MVP kỹ thuật.

## Cập nhật mã nguồn

Lấy main mới nhất, sửa README hoặc script, kiểm tra biểu đồ rồi tạo commit mới và push bình thường. Giữ cả `assets/dashboard/` và `profile-3d-contrib/` để các ảnh nội bộ hiển thị. Xem README trong IDE bằng Ctrl+Shift+V.
