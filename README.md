# Alobo — Đặt lịch sân thể thao (Nhóm 11 - Kiểm thử phần mềm)

Website mô phỏng đặt lịch sân thể thao và bộ kịch bản kiểm thử tự động bằng **Selenium IDE** (45 test case).

- **Demo trực tuyến (Vercel):** https://alobo-gray.vercel.app
- **Lưu ý dữ liệu:** Toàn bộ tài khoản, sân yêu thích và lịch đặt được lưu trong `localStorage` của trình duyệt (không kết nối backend thật, không phát sinh thanh toán thật).

## Cấu trúc thư mục

```text
.
└── alobo-web-ide/
    ├── index.html          # Trang chính ứng dụng
    ├── app.js              # Logic tìm kiếm, đặt sân, thanh toán, bản đồ
    ├── style.css           # Giao diện & hiệu ứng
    ├── header-pattern.svg  # Họa tiết banner đầu trang
    ├── vendor/             # Thư viện Leaflet hiển thị bản đồ
    ├── run_web.py          # Web server nội bộ bằng Python 3
    ├── MO-WEB.bat          # Script mở nhanh web trên Windows
    └── 45 Test/            # Bộ 6 file kiểm thử Selenium IDE (.side)
```

## Chạy cục bộ để kiểm thử với Selenium IDE

Các file `.side` sử dụng Base URL mặc định là `http://localhost:8000/`.

1. Mở terminal tại thư mục `alobo-web-ide/`:
   ```powershell
   cd alobo-web-ide
   python run_web.py
   ```
   *(Hoặc chạy `py -3 run_web.py`, hoặc mở trực tiếp `MO-WEB.bat` trên Windows.)*
2. Truy cập `http://localhost:8000/` và mở các file `.side` trong thư mục `alobo-web-ide/45 Test/` bằng tiện ích **Selenium IDE**.

## Danh sách bộ kiểm thử (`alobo-web-ide/45 Test/`)

| File | Nội dung | Số test case |
| --- | --- | ---: |
| `Nhom11_kiemthu_dangki.side` | Kiểm thử đăng ký tài khoản | 9 |
| `Nhom11_kiemthu_dangnhap.side` | Kiểm thử đăng nhập | 7 |
| `Nhom11_kiemthu_timkiem.side` | Kiểm thử tìm kiếm & bộ lọc sân | 11 |
| `nhom11_kiemthu_datlich.side` | Kiểm thử đặt lịch sân | 11 |
| `nhom11_kiemthu_thanhtoan.side` | Kiểm thử thanh toán | 6 |
| `nhom11_kiemthu_full.side` | Luồng kiểm thử tổng hợp | 1 |
| **Tổng cộng** | | **45** |
