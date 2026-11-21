# Alobo — thư mục web riêng để ghi kiểm thử bằng Selenium IDE

Thư mục này chứa mã web và chương trình mở web. Không cần pytest, Selenium Python hoặc môi trường .venv. Cần Python 3 đã cài trên máy.

## Chạy trong Terminal VS Code và tự mở web

1. Giải nén toàn bộ ZIP. Mở đúng thư mục **alobo-web-ide** bằng File → Open Folder. Phải thấy run_web.py và index.html ngay trong thư mục này.
2. Chọn Terminal → New Terminal.
3. Chạy một dòng:

```powershell
python run_web.py
```

Nếu lệnh python không được nhận, dùng `py -3 run_web.py`.

Web tự mở tại **http://localhost:8000/**. Nhật ký server hiện ngay trong Terminal VS Code, không mở thêm cửa sổ Terminal. Giữ Terminal mở trong khi ghi và chạy lại kiểm thử. Ctrl+C để dừng.

Có thể nhấp đúp MO-WEB.bat để mở nhanh ngoài VS Code; cách đó sẽ mở cửa sổ Terminal riêng.

## Dùng với Selenium IDE

- Mở trình duyệt đã cài Selenium IDE.
- Dùng **http://localhost:8000/** làm Base URL / địa chỉ bắt đầu của dự án kiểm thử.
- Bắt đầu ghi và thực hiện thao tác trên web: đăng ký, đăng nhập, tìm sân, đặt lịch, thanh toán.
- Giữ web server hoạt động khi chạy lại bài kiểm thử.
- Nếu trình duyệt mặc định tự mở không phải trình duyệt có IDE, mở địa chỉ trên trong đúng trình duyệt bạn dùng.

## Dữ liệu và các chức năng

- Đề xuất mặc định 9 sân Hà Nội; có thể tìm HCM / Sài Gòn / Đà Nẵng.
- Đăng ký bằng họ tên, số điện thoại 10 chữ số bắt đầu bằng 0, mật khẩu tối thiểu 6 ký tự và xác nhận khớp.
- Không có tài khoản mặc định. Bạn tự đăng ký một tài khoản trước khi ghi ca đăng nhập. Không dùng mật khẩu thật.
- Ghi ca đăng nhập thì đăng xuất trước khi bắt đầu. Ca đặt lịch cần tài khoản đang đăng nhập. Ca thanh toán cần có lịch chưa thanh toán.
- Thanh toán chỉ cần bấm nút; không chuyển tiền thật.
- Lịch sân có ô bận cố định để kiểm tra. Chọn ngày mai và ô trống khi ghi luồng thành công.
- Bản đồ cần Internet để tải nền; các ghim sân là vị trí khu vực mô phỏng.

Dữ liệu lưu trong localStorage của trình duyệt. Tải lại trang không xóa tài khoản/lịch. Vì vậy chạy lại ca đăng ký bằng cùng một số sẽ báo trùng; dùng số mới cho mỗi lần hoặc xóa dữ liệu alobo_ của web test trước khi thử lại. Chỉ xóa dữ liệu khi bạn muốn làm mới môi trường kiểm thử.

Luôn dùng cùng địa chỉ **localhost:8000**. Đổi sang 127.0.0.1 hoặc đổi cổng sẽ có vùng dữ liệu khác.

## Khi cổng 8000 đang được sử dụng

Nếu server Alobo cũ vẫn chạy, dừng bằng Ctrl+C tại Terminal cũ. Hoặc chạy:

```powershell
python run_web.py --port 8080
```

Khi đó cập nhật Base URL trong Selenium IDE thành **http://localhost:8080/**.

## File để sửa web

- index.html: trang khởi đầu.
- app.js: dữ liệu sân và chức năng web.
- style.css: bố cục, màu sắc, hiệu ứng.
- header-pattern.svg: họa tiết nền đầu trang.
- vendor/: thư viện bản đồ.
- run_web.py: khởi động server và mở trình duyệt; chỉ dùng thư viện chuẩn Python.

Không có các bước tự động đăng ký/đăng nhập hoặc lớp khoanh nút của bộ Selenium Python. Bạn điều khiển và ghi thao tác từ Selenium IDE.
