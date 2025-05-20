from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, 
            template_folder='../../frontend/src/html',
            static_folder='../../frontend/src'
            )
app.config['SECRET_KEY'] = '987654321123456789987654321123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


courses = {
    "python-co-ban": {
        "title": "Lập trình Python cơ bản",
        "instructor": "K team",
        "rating": 4.3,
        "price": 200000,
        "old_price": 300000,
        "description": " Học Python từ cơ bản đến thực hành ứng dụng.",
        "lectures": [
            {"title":"Bài 1: Giới thiệu ngôn ngữ lập trình Python", "video_url": "https://www.youtube.com/watch?v=NZj6LI5a9vc&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg"},
            {"title":"Bài 2: Cài đặt môi trường Python", "video_url":"https://www.youtube.com/watch?v=jf-q_dG8WzI&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=2"}, 
            {"title":"Bài 3: Chạy file Python", "video_url":"https://www.youtube.com/watch?v=QFxqY8qv42E&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=3"}, 
            {"title":"Bài 4: Comment trong Python","video_url":"https://www.youtube.com/watch?v=t3dERE9T5yg&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=4"}, 
            {"title":"Bài 5: Biến(Variable) trong Python","video_url":"https://www.youtube.com/watch?v=nclE18Yl-kA&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=5"}, 
            {"title":"Bài 6: Kiểu số trong Python","video_url":"https://www.youtube.com/watch?v=IAVvgqDBiv0&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=6"},
            {"title":"Bài 7: Kiểu chuỗi trong Python - Phần 1","video_url":"https://www.youtube.com/watch?v=Vb6XWSLPQfg&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=7"},
            {"title":"Bài 8: Kiểu chuỗi trong Python - Phần 2","video_url":"https://www.youtube.com/watch?v=gzWriEOVjU0&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=8"},
            {"title":"Bài 9: Kiểu chuỗi trong Python - Phần 3","video_url":"https://www.youtube.com/watch?v=LRUHnuHljPQ&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=9"},
            {"title":"Bài 10: Kiểu chuỗi trong Python - Phần 4","video_url":"https://www.youtube.com/watch?v=q2TNJMBx6GE&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=10"},
            {"title":"Bài 11: Kiểu chuỗi trong Python - Phần 5","video_url":"https://www.youtube.com/watch?v=u2Kd3weqPZE&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=11"},
            {"title":"Bài 12: List trong Python - Phần 1","video_url":"https://www.youtube.com/watch?v=UzTE665WXb8&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=12"},
            {"title":"Bài 13: List trong Python - Phần 2","video_url":"https://www.youtube.com/watch?v=9IH3EynbcpU&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=13"},
            {"title": "Bài 14: Tuple trong Python", "video_url": "https://www.youtube.com/watch?v=dDFFCbRGm3o&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=14"},
            {"title": "Bài 15: Hashable và Unhashable trong Python", "video_url": "https://www.youtube.com/watch?v=gw9zbl2Q7r4&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=15"},
            {"title": "Bài 16: Set trong Python", "video_url": "https://www.youtube.com/watch?v=S-CWHkKiOBs&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=16"},
            {"title": "Bài 17: Dict trong Python - Phần 1", "video_url": "https://www.youtube.com/watch?v=zFDTmZjJFws&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=17"},
            {"title": "Bài 18: Dict trong Python - Phần 2", "video_url": "https://www.youtube.com/watch?v=jmwBKuJl2Zg&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=18"},
            {"title": "Bài 19: Xử lý File trong Python", "video_url": "https://www.youtube.com/watch?v=6J8-jkoRBXw&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=19"},
            {"title": "Bài 20: Iteration trong Python", "video_url": "https://www.youtube.com/watch?v=GSUwh958k_A&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=20"},
            {"title": "Bài 21: Hàm xuất trong Python", "video_url": "https://www.youtube.com/watch?v=rhOyCSIf1is&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=21"},
            {"title": "Bài 22: Hàm nhập trong Python", "video_url": "https://www.youtube.com/watch?v=rK4MphZVhDM&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=22"},
            {"title": "Bài 23: Kiểu Boolean trong python", "video_url": "https://www.youtube.com/watch?v=iB9EhSZvfFk&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=23"},
            {"title": "Bài 24: Cấu trúc rẽ nhánh trong Python", "video_url": "https://www.youtube.com/watch?v=4_Jb1xZsDJ8&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=24"},
            {"title": "Bài 25: While Loop trong Python", "video_url": "https://www.youtube.com/watch?v=wq7Th3nXyCQ&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=25"},
            {"title": "Bài 26: For Loop trong Python - Phần 1", "video_url": "https://www.youtube.com/watch?v=9TxJ71NNO64&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=26"},
            {"title": "Bài 27: For Loop trong Python - Phần 2", "video_url": "https://www.youtube.com/watch?v=LwC0n2A6QRQ&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=27"},
            {"title": "Bài 28: Function trong python - Sơ lược về hàm", "video_url": "https://www.youtube.com/watch?v=a6FnNvt3Fw4&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=28"},
            {"title": "Bài 29: Function trong python - Positional", "video_url": "https://www.youtube.com/watch?v=M77p3PB-qzM&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=29"},
            {"title": "Bài 30: Function trong Python - Packing và unpacking", "video_url": "https://www.youtube.com/watch?v=0Gf5MVTWuCY&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=30"},
            {"title": "Bài 31: Function trong Python - Locals và globals", "video_url": "https://www.youtube.com/watch?v=w7qnt6iIakM&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=31"},
            {"title": "Bài 32: Function trong Python - Return", "video_url": "https://www.youtube.com/watch?v=3bdMH8z50zE&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=32"},
            {"title": "Bài 33: Function trong Python - Yield", "video_url": "https://www.youtube.com/watch?v=aChGfj5h3UQ&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=33"},
            {"title": "Bài 34: Function trong Python - Lambda", "video_url": "https://www.youtube.com/watch?v=7YTL1u5Ja5A&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=34"},
            {"title": "Bài 35: Function trong Python - Functional tools", "video_url": "https://www.youtube.com/watch?v=W5Xvw_2WPeg&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=35"},
            {"title": "Bài 36: Function trong Python - Đệ Quy", "video_url": "https://www.youtube.com/watch?v=AFNMgGmWcdQ&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=36"}
            ],
        "instructor_bio": "K team là nhóm chuyên đào tạo lập trình thực chiến.",
        "image": "assets/Python.png"
    },
    "csharp-co-ban": {
        "title": "Lập trình C# cơ bản",
        "instructor": "K Team",
        "rating": 4.5,
        "price": 300000,
        "old_price": 450000,
        "description": "Học lập trình cơ bản với C#.",
        "lectures": [
            {"title":"Bài 1: C# là gì","video_url":"https://www.youtube.com/watch?v=9kohr6pMwag&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=1"}, 
            {"title": "Bài 2: Cấu trúc lệnh cơ bản", "video_url": "https://www.youtube.com/watch?v=FhAIc0tlyaQ&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=2"},
            {"title": "Bài 3: Nhập xuất cơ bản", "video_url": "https://www.youtube.com/watch?v=BAscPWPtCD8&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=3"},
            {"title": "Bài 4: Biến trong C#", "video_url": "https://www.youtube.com/watch?v=IEz7uMSHitM&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=4"},
            {"title": "Bài 5: Kiểu dữ liệu trong C#", "video_url": "https://www.youtube.com/watch?v=yrH7Qe8FXqE&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=5"},
            {"title": "Bài 6: Toán tử trong C#", "video_url": "https://www.youtube.com/watch?v=niz7Gg8uB-k&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=6"},
            {"title": "Bài 7: Hằng", "video_url": "https://www.youtube.com/watch?v=13NRSYgKh0o&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=7"},
            {"title": "Bài 8: Ép kiểu trong C#", "video_url": "https://www.youtube.com/watch?v=YmF2kTg0ajU&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=8"},
            {"title": "Bài 9: If else trong C#", "video_url": "https://www.youtube.com/watch?v=O3ijcGpEgSY&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=9"},
            {"title": "Bài 10: Switch case trong C#", "video_url": "https://www.youtube.com/watch?v=0NYj4QkJx4U&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=10"},
            {"title": "Bài 11: Kiểu dữ liệu object và từ khóa var", "video_url": "https://www.youtube.com/watch?v=SkxQlfdhVko&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=11"},
            {"title": "Bài 12: Kiểu dữ liệu dynamic", "video_url": "https://www.youtube.com/watch?v=lM-7tv768XA&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=12"},
            {"title": "Bài 13: Giới thiệu cấu trúc lặp", "video_url": "https://www.youtube.com/watch?v=mKLRETK9slQ&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=13"},
            {"title": "Bài 14: Goto", "video_url": "https://www.youtube.com/watch?v=4yVPY-Hyg1o&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=14"},
            {"title": "Bài 15: Vòng lặp For", "video_url": "https://www.youtube.com/watch?v=QW-1sWoK3Bo&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=15"},
            {"title": "Bài 16: Vòng lặp while", "video_url": "https://www.youtube.com/watch?v=06rWN7e55Ic&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=16"},
            {"title": "Bài 17: Vòng lặp do - while", "video_url": "https://www.youtube.com/watch?v=0YzMWQ_Tgyw&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=17"},
            {"title": "Bài 18: Cấu trúc của hàm cơ bản", "video_url": "https://www.youtube.com/watch?v=EJWEUUNtC4c&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=18"},
            {"title": "Bài 19: Biến toàn cục và biến cục bộ", "video_url": "https://www.youtube.com/watch?v=RhVa3B0hFI0&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=19"},
            {"title": "Bài 20: Từ khóa ref và out", "video_url": "https://www.youtube.com/watch?v=ciY7Ge4klYE&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=20"},
            {"title": "Bài 21: Mảng 1 chiều", "video_url": "https://www.youtube.com/watch?v=UHs1GJ-Ms0k&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=21"},
            {"title": "Bài 22: Mảng 2 chiều trong C#", "video_url": "https://www.youtube.com/watch?v=4IRA9t1cyWQ&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=22"},
            {"title": "Bài 23: Mảng nhiều chiều trong C#", "video_url": "https://www.youtube.com/watch?v=bPFa4PHrhaE&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=23"},
            {"title": "Bài 24: Vòng lặp foreach trong C#", "video_url": "https://www.youtube.com/watch?v=M-pJz3jhioU&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=24"},
            {"title": "Bài 25: Lớp String trong C#", "video_url": "https://www.youtube.com/watch?v=Eizo3hFDAcw&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=25"},
            {"title": "Bài 26: Struct trong C#", "video_url": "https://www.youtube.com/watch?v=QwzOHtuFuIQ&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=26"},
            {"title": "Bài 27: enum trong C#", "video_url": "https://www.youtube.com/watch?v=PU3wuEM3tH8&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=27"},
            {"title": "Bài 28: Regular Expression trong C#", "video_url": "https://www.youtube.com/watch?v=bEVigTm5dAo&list=PL33lvabfss1wUj15ea6W0A-TtDOrWWSRK&index=28"}
                     ],
        "instructor_bio": "K team là nhóm chuyên đào tạo lập trình thực chiến.",
        "image": "assets/C#.jpg"
    },
     "hoc-excel-co-ban": {
        "title": "Học Excel cơ bản",
        "instructor": "Đỗ Bảo Nam",
        "rating": 4.7,
        "price": 150000,
        "old_price": 250000,
        "description": " Học Excel cơ bản cùng giảng viên Đỗ Bảo Nam.",
        "lectures": [
                    {"title": "Bài 1: Các thao tác cơ bản trong Excel", "video_url": "https://www.youtube.com/watch?v=vTFix82TIdA&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=1"},
                    {"title": "Bài 2: Cách tạo bảng trong Excel", "video_url": "https://www.youtube.com/watch?v=SGZ3jqsW_3E&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=2"},
                    {"title": "Bài 3: Hướng dẫn cách giãn dòng trong Excel", "video_url": "https://www.youtube.com/watch?v=leFxzUQsGTY&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=3"},
                    {"title": "Bài 4: Cách gộp ô trong Excel không mất dữ liệu", "video_url": "https://www.youtube.com/watch?v=Qzy8qA5774s&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=4"},
                    {"title": "Bài 5: Cách chèn thêm cột, thêm dòng trong Excel", "video_url": "https://www.youtube.com/watch?v=cYdGgfFuqsA&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=5"},
                    {"title": "Bài 6: Cách ẩn/hiện thanh công cụ trong Excel", "video_url": "https://www.youtube.com/watch?v=jRsfzxWL3ns&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=6"},
                    {"title": "Bài 7: Các thao tác định dạng trong Excel cơ bản", "video_url": "https://www.youtube.com/watch?v=umnMtOhI2t8&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=7"},
                    {"title": "Bài 8: Cách đánh số thứ tự trong Excel, đánh số có điều kiện trong Excel", "video_url": "https://www.youtube.com/watch?v=yh5mOo_O8U0&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=8"},
                    {"title": "Bài 9: Cách xóa cột, xóa dòng trong Excel, xóa dòng trống trong Excel", "video_url": "https://www.youtube.com/watch?v=v5aQ2lbwmVc&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=9"},
                    {"title": "Bài 10: Cách xuống dòng trong Excel, xuống dòng trong 1 ô Excel tự động", "video_url": "https://www.youtube.com/watch?v=NId2onepFCI&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=10"},
                    {"title": "Bài 11: Cách viết số điện thoại trong Excel, cách hiện số 0 trong Excel", "video_url": "https://www.youtube.com/watch?v=XxwwoaHZ27U&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=11"},
                    {"title": "Bài 12: Cách viết số mũ trong Excel, cách viết chỉ số dưới trong Excel", "video_url": "https://www.youtube.com/watch?v=vQDtoLLPr3o&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=12"},
                    {"title": "Bài 13: Cách xoay chữ trong Excel, xoay chữ ngang, xoay dọc trong Excel", "video_url": "https://www.youtube.com/watch?v=SFLFPg1ghL8&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=13"},
                    {"title": "Bài 14: Cách bôi đen nhanh trong Excel", "video_url": "https://www.youtube.com/watch?v=LT8j5FOpdOA&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=14"},
                    {"title": "Bài 15: Cách cố định dòng trong Excel, cố định cột & tiêu đề trong Excel", "video_url": "https://www.youtube.com/watch?v=nBhHuuoL3qw&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=15"},
                    {"title": "Bài 16: Cách ẩn/hiện dòng và cột trong Excel", "video_url": "https://www.youtube.com/watch?v=VXc7U-HyA7g&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=16"},
                    {"title": "Bài 17: Cách chèn ký tự đặc biệt trong Excel, chèn icon Facebook vào Excel", "video_url": "https://www.youtube.com/watch?v=Bq7uptSntZY&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=17"},
                    {"title": "Bài 18: Cách xóa các dữ liệu trùng nhau trong Excel đơn giản & nhanh nhất", "video_url": "https://www.youtube.com/watch?v=IEPQwLMMpdo&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=18"},
                    {"title": "Bài 19: Cách tạo đường kẻ chéo trong Excel", "video_url": "https://www.youtube.com/watch?v=Qsio--tm3Ms&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=19"},
                    {"title": "Bài 20: Cách đặt mật khẩu cho file Excel, cài password cho file Excel", "video_url": "https://www.youtube.com/watch?v=ZaHwVBQjRv8&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=20"},
                    {"title": "Bài 21: Cách cài đặt font chữ mặc định trong Excel", "video_url": "https://www.youtube.com/watch?v=iwDs1LPRisQ&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=21"},
                    {"title": "Bài 22: Cách copy giữ nguyên định dạng trong Excel bằng Format Painter", "video_url": "https://www.youtube.com/watch?v=wUozv_565iM&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=22"},
                    {"title": "Bài 23: Cách sắp xếp tên theo ABC trong Excel đơn giản cho mọi phiên bản", "video_url": "https://www.youtube.com/watch?v=9JpQ9izqymM&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=23"},
                    {"title": "Bài 24: Cách sắp xếp theo thứ tự tăng dần trong Excel, giảm dần trong Excel", "video_url": "https://www.youtube.com/watch?v=E1Ycix_RCLY&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=24"},
                    {"title": "Bài 25: Cách chỉnh ngày tháng trong Excel, đổi định dạng mặc định trong Excel", "video_url": "https://www.youtube.com/watch?v=pQjWo_fQiaQ&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=25"},
                    {"title": "Bài 26: Cách chèn ảnh vào Excel, chèn hình ảnh 3D vào file Excel", "video_url": "https://www.youtube.com/watch?v=X8pTxsSP8yY&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=26"},
                    {"title": "Bài 27: Cách chèn video vào Excel", "video_url": "https://www.youtube.com/watch?v=ufP3T66ptxY&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=27"},
                    {"title": "Bài 28: Cách tìm kiếm trong Excel, tìm kiếm dữ liệu và thay thế trong Excel", "video_url": "https://www.youtube.com/watch?v=UBJGowkDz4U&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=28"},
                    {"title": "Bài 29: Cách đặt tên cột trong Excel, đổi hoặc xóa tên cột đã đặt trong Excel", "video_url": "https://www.youtube.com/watch?v=XxlC_vt5AVQ&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=29"},
                    {"title": "Bài 30: Cách thay số 0 bằng dấu gạch trong Excel, thay số 0 bằng - trong Excel", "video_url": "https://www.youtube.com/watch?v=_XEyHcNROiw&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=30"},
                    {"title": "Bài 31: Cách đếm số lần xuất hiện trong Excel bằng hàm COUNTIF", "video_url": "https://www.youtube.com/watch?v=2ywpjrt38Y8&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=31"},
                    {"title": "Bài 32: Cách in Excel vừa trang giấy A4, khắc phục in không hết trang trong Excel", "video_url": "https://www.youtube.com/watch?v=6aqBeYfPdVg&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=32"},
                    {"title": "Bài 33: Cách bỏ dấu trong Excel cực đơn giản không cần phải tạo hàm", "video_url": "https://www.youtube.com/watch?v=v1g728Bkusk&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=33"},
                    {"title": "Bài 34: Cách xóa khoảng trắng trong Excel bằng hàm TRIM trong Excel [đơn giản]", "video_url": "https://www.youtube.com/watch?v=0WorYE7vEAo&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=34"},
                    {"title": "Bài 35: Cách vẽ biểu đồ trong Excel như biểu đồ cột, đường, hình tròn", "video_url": "https://www.youtube.com/watch?v=RcG9v0Rq-OE&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=35"},
                    {"title": "Bài 36: Cách tính phần trăm trong Excel cực dễ hiểu qua các ví dụ minh họa", "video_url": "https://www.youtube.com/watch?v=C40RPU-C3nU&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=36"},
                    {"title": "Bài 37: Cách tắt Protected View, cách bỏ Enable Editing trong Excel", "video_url": "https://www.youtube.com/watch?v=C8kiGhaPz5M&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=37"},
                    {"title": "Bài 38: Cách khóa công thức trong Excel, ẩn công thức tính toán trong Excel", "video_url": "https://www.youtube.com/watch?v=SHDY404N9xg&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=38"},
                    {"title": "Bài 39: Cách mở khóa công thức trong Excel, mở khóa hàm trong Excel", "video_url": "https://www.youtube.com/watch?v=7LsgAG_YRzA&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=39"},
                    {"title": "Bài 40: Cách định dạng tiền tệ trong Excel, định dạng VND trong Excel", "video_url": "https://www.youtube.com/watch?v=k4tUjwdEhGc&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=40"},
                    {"title": "Bài 41: Cách tách ký tự trong Excel, cách lấy ký tự ở giữa, trái, phải trong Excel", "video_url": "https://www.youtube.com/watch?v=YjhViXs0FrU&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=41"},
                    {"title": "Bài 42: Cách lấy ký tự trong Excel, cắt chuỗi bằng hàm Left kết hợp Search", "video_url": "https://www.youtube.com/watch?v=LYyxZZlxCXs&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=42"},
                    {"title": "Bài 43: Cách cắt chuỗi trong Excel bằng hàm Right kết hợp Len và Search", "video_url": "https://www.youtube.com/watch?v=OQL13RcHjGo&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=43"},
                    {"title": "Bài 44: Cách dùng hàm RIGHT trong Excel từ cơ bản đến nâng cao qua ví dụ minh họa", "video_url": "https://www.youtube.com/watch?v=j8XHxfJAq5I&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=44"},
                    {"title": "Bài 45: Cách tách tên trong Excel, tách họ và tên trong Excel đơn giản nhất", "video_url": "https://www.youtube.com/watch?v=VB9sTpdKQtc&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=45"},
                    {"title": "Bài 46: Cách sắp xếp có điều kiện trong Excel theo nhiều tiêu chí khác nhau", "video_url": "https://www.youtube.com/watch?v=znirrmcRzPw&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=46"},
                    {"title": "Bài 47: Cách dùng hàm TRIM trong Excel, Cách xóa khoảng trắng trong Excel", "video_url": "https://www.youtube.com/watch?v=Fx7UGNnljU4&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=47"},
                    {"title": "Bài 48: Cách tạo file Excel trên Google Drive & chia sẻ file cho người khác", "video_url": "https://www.youtube.com/watch?v=Ulf6uPjBGpc&list=PLN3piE-wUotoIWAx8o5Gyg7a3jtseh_73&index=48"},
                     ],
        "instructor_bio": " Với nhiều năm kinh nghiệm trong việc tìm hiểu, áp dụng và hướng dẫn sử dụng công nghệ, anh đã giúp hàng triệu người dùng cải thiện kỹ năng tin học thông qua các bài viết và video hướng dẫn chi tiết, dễ hiểu.",
        "image": "assets/Excel.jpg"
    },
}
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Mật khẩu không khớp!")
            return redirect(url_for('register'))

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            flash("Tên đăng nhập hoặc email đã tồn tại!")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Đăng ký thành công! Mời bạn đăng nhập.")
        return redirect(url_for('loginpage'))

    return render_template('registerpage.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash,password):
        session['user_id'] = user.id
        session['username'] = user.username
        flash('Đăng nhập thành công!', 'success')
        return redirect(url_for('homepage'))
    else:
        flash('Tên đăng nhập hoặc mật khẩu không đúng.', 'error')
        return redirect(url_for('loginpage'))
@app.route('/logout')
def logout():
    session.clear()
    flash('Đã đăng xuất.', 'info')
    return redirect(url_for('homepage'))
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/coursepage')
def coursepage():
    if 'user_id' not in session:
        flash('Vui lòng đăng nhập.', 'warning')
        return redirect(url_for('loginpage'))
    return render_template('coursepage.html', username=session.get('username'))

@app.route('/dashboardpage')
def dashboardpage():
    return render_template('dashboardpage.html')

@app.route('/loginpage')
def loginpage():
    return render_template('loginpage.html')

@app.route('/mybasketpage')
def mybasketpage():
    return render_template('mybasketpage.html')

@app.route('/course/<course_id>')
def course_info(course_id):
    course = courses.get(course_id)
    if course:
        return render_template('courseinfo.html', course=course)
    return "Khóa học không tồn tại", 404


@app.route('/viewvideo')
def view_video():
    video_id = request.args.get('video_url')
    return render_template('viewvideopage.html', video_id=video_id)

if __name__ == '__main__':
    app.run(debug=True)
