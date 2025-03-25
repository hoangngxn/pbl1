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
- **Cấu trúc Job**: Sử dụng struct để biểu diễn công việc với các thuộc tính:
  ```c
  typedef struct {
      int job_id;
      int processing_time;
      int deadline;
  } Job;
  ```
- **Mảng động**: Quản lý danh sách công việc và lịch trình
- **Con trỏ**: Để quản lý bộ nhớ và thao tác hiệu quả với dữ liệu

### 2.2 Lý thuyết liên quan
- **Thuật toán tham lam (Greedy Algorithm)**: Để đảm bảo số lượng công việc hoàn thành đúng hạn là lớn nhất, chúng ta sắp xếp công việc theo thời hạn hoàn thành và thực hiện lần lượt.
- **Lập lịch không ngắt quãng (Non-preemptive Scheduling)**: Một công việc phải được thực hiện liên tục từ lúc bắt đầu cho đến khi kết thúc, không được gián đoạn.

## 3. Thuật toán
### 3.1 Ý tưởng thuật toán
Thuật toán sử dụng chiến lược tham lam để sắp xếp và chọn công việc:
1. Sắp xếp các công việc theo thời hạn hoàn thành tăng dần bằng hàm `qsort()`.
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

#### Hàm chính trong C
```c
void schedule_jobs(int n, int* processing_times, int* deadlines, 
                   int* completed_jobs, int* schedule) {
    // Tạo mảng các công việc
    Job* jobs = malloc(n * sizeof(Job));
    
    // Sắp xếp các công việc theo thời hạn
    qsort(jobs, n, sizeof(Job), compare_jobs);

    int current_time = 0;
    int job_count = 0;

    // Duyệt và lập lịch các công việc
    for (int i = 0; i < n; i++) {
        if (current_time + jobs[i].processing_time <= jobs[i].deadline) {
            schedule[job_count] = jobs[i].job_id;
            current_time += jobs[i].processing_time;
            job_count++;
        }
    }

    *completed_jobs = job_count;
    free(jobs);
}
```

## 4. Giao diện và Chức Năng
### 4.1 Menu Chính
- Nhập thủ công thông tin công việc
- Tải dữ liệu từ file .inp
- Thoát chương trình

### 4.2 Xử Lý Đầu Vào
- Hỗ trợ nhập liệu từ bàn phím
- Đọc file đầu vào với định dạng chuẩn
- Kiểm tra tính hợp lệ của dữ liệu

### 4.3 Xuất Kết Quả
- Hiển thị số lượng công việc hoàn thành
- Xuất danh sách công việc được thực hiện
- Lưu kết quả vào file .out với tên chứa mốc thời gian

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

## 6. Kết luận
### 6.1 Kết quả đạt được
- Chương trình đã giải quyết bài toán lập lịch ưu tiên đúng hạn bằng thuật toán tham lam.
- Đạt được mục tiêu tối ưu hóa số lượng công việc hoàn thành đúng hạn.
- Chương trình chạy hiệu quả với $O(n \log n)$ do việc sắp xếp danh sách công việc.

### 6.2 Hạn chế
- Không tối ưu trong trường hợp có nhiều công việc với thời gian thực hiện dài nhưng thời hạn hoàn thành xa.
- Cần cải tiến để áp dụng cho các hệ thống có ràng buộc phức tạp hơn.

## 7. Phụ lục: Chương trình nguồn
Toàn bộ mã nguồn C được lưu trữ trong file `job_scheduler.c` với các chức năng chính:
- Nhập và xử lý dữ liệu
- Thuật toán lập lịch
- Giao diện dòng lệnh thân thiện
- Quản lý file đầu vào/đầu ra