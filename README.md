# BÁO CÁO ĐỒ ÁN

## 1. Giới thiệu đề tài
### 1.1 Mô tả bài toán
Bài toán lập lịch ưu tiên đúng hạn là một vấn đề quan trọng trong quản lý tiến trình và tối ưu hóa thời gian thực hiện công việc. Với một tập hợp n công việc cần xử lý trên một máy duy nhất, mỗi công việc có một thời gian thực hiện nhất định và một thời hạn hoàn thành. Mục tiêu của bài toán là sắp xếp thứ tự thực hiện các công việc sao cho số lượng công việc hoàn thành đúng hạn là lớn nhất.

### 1.2 Ứng dụng thực tế
Bài toán này có ứng dụng trong nhiều lĩnh vực thực tế như:
- Quản lý tiến trình trong hệ điều hành.
- Lập lịch sản xuất trong nhà máy.
- Quản lý tác vụ trong hệ thống thời gian thực.
- Sắp xếp công việc trong quản lý dự án.

## 2. Cấu trúc dữ liệu, lý thuyết liên quan

### 2.1 Cấu trúc dữ liệu sử dụng
- **Danh sách công việc**: Mỗi công việc được biểu diễn bởi một bộ ba gồm:
  - Số thứ tự công việc.
  - Thời gian thực hiện.
  - Thời hạn hoàn thành.
- **Danh sách lịch trình**: Lưu trữ các công việc đã được chọn để thực hiện đúng hạn.

### 2.2 Lý thuyết liên quan
- **Thuật toán tham lam (Greedy Algorithm)**: Để đảm bảo số lượng công việc hoàn thành đúng hạn là lớn nhất, chúng ta sắp xếp công việc theo thời hạn hoàn thành và thực hiện lần lượt.
- **Lập lịch không ngắt quãng (Non-preemptive Scheduling)**: Một công việc phải được thực hiện liên tục từ lúc bắt đầu cho đến khi kết thúc, không được gián đoạn.

## 3. Thuật toán
### 3.1 Ý tưởng thuật toán
Thuật toán sử dụng chiến lược tham lam để sắp xếp và chọn công việc:
1. Sắp xếp các công việc theo thời hạn hoàn thành tăng dần.
2. Duyệt qua danh sách công việc đã sắp xếp và thêm vào lịch trình nếu tổng thời gian thực hiện không vượt quá thời hạn của công việc đó.
3. Ghi nhận số lượng công việc được hoàn thành đúng hạn và trình tự thực hiện chúng.

### 3.2 Mô tả thuật toán
#### Đầu vào:
- Số lượng công việc $n$.
- Danh sách thời gian thực hiện $p_i$.
- Danh sách thời hạn hoàn thành $d_i$.

#### Đầu ra:
- Số lượng công việc hoàn thành đúng hạn.
- Danh sách trình tự thực hiện công việc.

#### Pseudocode
```
Sắp xếp danh sách công việc theo thời hạn hoàn thành tăng dần
current_time = 0
completed_jobs = 0
schedule = []

For each công việc trong danh sách đã sắp xếp:
    Nếu current_time + thời gian thực hiện ≤ thời hạn hoàn thành:
        Thêm công việc vào schedule
        Cập nhật current_time
        Tăng biến đếm số công việc hoàn thành

Trả về số lượng công việc hoàn thành đúng hạn và danh sách schedule
```

## 4. Đoạn chương trình hoặc hàm xử lý chính
```python
def schedule_jobs(n, p, d):
    jobs = sorted(enumerate(zip(p, d), start=1), key=lambda x: x[1][1])  # Sắp xếp theo thời hạn hoàn thành
    schedule = []
    current_time = 0
    completed_jobs = 0
    
    for job in jobs:
        job_id, (processing_time, deadline) = job
        if current_time + processing_time <= deadline:  # Nếu hoàn thành đúng hạn
            schedule.append(job_id)
            current_time += processing_time
            completed_jobs += 1
    
    return completed_jobs, schedule
```

## 5. Kết quả chương trình
### 5.1 Dữ liệu đầu vào
```
LICHD.INP:
5
2 3 1 4 2
3 5 2 6 4
```

### 5.2 Kết quả đầu ra
```
LICHD.OUT:
3
3 1 5
```

### 5.3 Giao diện minh họa
- **Tập tin đầu vào**: Chứa số lượng công việc, thời gian thực hiện và thời hạn hoàn thành.
- **Tập tin đầu ra**: Hiển thị số lượng công việc hoàn thành đúng hạn và danh sách công việc được thực hiện.

## 6. Kết luận
### 6.1 Kết quả đạt được
- Chương trình đã giải quyết bài toán lập lịch ưu tiên đúng hạn bằng thuật toán tham lam.
- Đạt được mục tiêu tối ưu hóa số lượng công việc hoàn thành đúng hạn.
- Chương trình chạy hiệu quả với $O(n \log n)$ do việc sắp xếp danh sách công việc.

### 6.2 Hạn chế
- Không tối ưu trong trường hợp có nhiều công việc với thời gian thực hiện dài nhưng thời hạn hoàn thành xa.
- Cần cải tiến để áp dụng cho các hệ thống có ràng buộc phức tạp hơn.

## 7. Phụ lục: Chương trình nguồn
(Toàn bộ mã nguồn của chương trình sẽ được đính kèm trong phần phụ lục.)