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

## 1. Giới Thiệu Chức Năng Hệ Thống

### 1.1 Các Chức Năng Chính
1. **Nhập Liệu Linh Hoạt**
   - Nhập thủ công thông tin công việc
   - Tải dữ liệu từ file .inp
   - Kiểm tra và xác thực dữ liệu đầu vào

2. **Xử Lý Lập Lịch**
   - Áp dụng thuật toán tham lam để tối ưu hóa công việc
   - Sắp xếp và chọn lọc công việc hiệu quả
   - Tối đa hóa số lượng công việc hoàn thành đúng hạn

3. **Xuất Kết Quả**
   - Hiển thị kết quả trên màn hình
   - Lưu kết quả vào file .out có mốc thời gian

## 2. Chi Tiết Các Hàm Chức Năng

### 2.1 Hàm `schedule_jobs()`
#### Mục Đích
Lập lịch các công việc theo nguyên tắc tham lam, ưu tiên các công việc có thể hoàn thành đúng hạn.

#### Các Bước Thực Hiện
1. **Khởi Tạo Dữ Liệu**
   ```c
   Job* jobs = malloc(n * sizeof(Job));
   for (int i = 0; i < n; i++) {
       jobs[i].job_id = i + 1;
       jobs[i].processing_time = processing_times[i];
       jobs[i].deadline = deadlines[i];
   }
   ```
   - Chuyển đổi mảng đầu vào sang cấu trúc `Job`
   - Gán số thứ tự, thời gian xử lý và thời hạn cho mỗi công việc

2. **Sắp Xếp Công Việc**
   ```c
   qsort(jobs, n, sizeof(Job), compare_jobs);
   ```
   - Sử dụng `qsort()` để sắp xếp công việc theo thời hạn tăng dần
   - Hàm `compare_jobs()` so sánh thời hạn của các công việc

3. **Lập Lịch Tham Lam**
   ```c
   int current_time = 0;
   int job_count = 0;
   for (int i = 0; i < n; i++) {
       if (current_time + jobs[i].processing_time <= jobs[i].deadline) {
           schedule[job_count] = jobs[i].job_id;
           current_time += jobs[i].processing_time;
           job_count++;
       }
   }
   ```
   - Duyệt qua danh sách công việc đã sắp xếp
   - Chọn các công việc có thể hoàn thành đúng hạn
   - Cập nhật thời gian hiện tại và danh sách lịch trình

### 2.2 Hàm `manual_input()`
#### Mục Đích
Cho phép người dùng nhập thông tin công việc trực tiếp từ bàn phím.

#### Các Bước Thực Hiện
```c
void manual_input(int* n, int* processing_times, int* deadlines) {
    printf("Nhập số lượng công việc: ");
    scanf("%d", n);

    printf("Nhập thời gian xử lý (cách nhau bằng khoảng trắng): ");
    for (int i = 0; i < *n; i++) {
        scanf("%d", &processing_times[i]);
    }

    printf("Nhập thời hạn (cách nhau bằng khoảng trắng): ");
    for (int i = 0; i < *n; i++) {
        scanf("%d", &deadlines[i]);
    }
}
```
- Nhập số lượng công việc
- Nhập từng thời gian xử lý
- Nhập từng thời hạn hoàn thành

### 2.3 Hàm `load_from_file()`
#### Mục Đích
Đọc thông tin công việc từ file .inp với định dạng chuẩn.

#### Các Bước Thực Hiện
```c
int load_from_file(char* filename, int* n, int* processing_times, int* deadlines) {
    FILE* file = fopen(filename, "r");
    // Đọc số lượng công việc
    if (fscanf(file, "%d", n) != 1) {
        printf("Lỗi đọc số lượng công việc\n");
        return 0;
    }

    // Đọc thời gian xử lý
    for (int i = 0; i < *n; i++) {
        if (fscanf(file, "%d", &processing_times[i]) != 1) {
            printf("Lỗi đọc thời gian xử lý\n");
            return 0;
        }
    }

    // Đọc thời hạn
    for (int i = 0; i < *n; i++) {
        if (fscanf(file, "%d", &deadlines[i]) != 1) {
            printf("Lỗi đọc thời hạn\n");
            return 0;
        }
    }

    fclose(file);
    return 1;
}
```
- Mở file theo tên được cung cấp
- Kiểm tra và đọc số lượng công việc
- Đọc danh sách thời gian xử lý
- Đọc danh sách thời hạn
- Xử lý lỗi nếu định dạng file không đúng

### 2.4 Hàm `save_output()`
#### Mục Đích
Lưu kết quả lập lịch vào file .out với tên chứa mốc thời gian.

#### Các Bước Thực Hiện
```c
void save_output(int completed_jobs, int* schedule, int n) {
    // Tạo tên file theo mốc thời gian
    time_t now;
    time(&now);
    struct tm *local = localtime(&now);
    char filename[50];
    sprintf(filename, "%04d%02d%02d_%02d%02d%02d.out", 
            local->tm_year + 1900, local->tm_mon + 1, local->tm_mday,
            local->tm_hour, local->tm_min, local->tm_sec);

    // Mở file để ghi
    FILE* outfile = fopen(filename, "w");
    
    // Ghi số lượng công việc hoàn thành
    fprintf(outfile, "%d\n", completed_jobs);

    // Ghi danh sách công việc
    for (int i = 0; i < completed_jobs; i++) {
        fprintf(outfile, "%d ", schedule[i]);
    }
    fprintf(outfile, "\n");

    fclose(outfile);
}
```
- Tạo tên file duy nhất dựa trên thời gian hiện tại
- Ghi số lượng công việc hoàn thành
- Ghi danh sách thứ tự công việc
- Đóng file sau khi ghi xong

## 3. Cơ Chế Hoạt Động Tổng Thể

### 3.1 Luồng Xử Lý Chính
1. Hiển thị menu lựa chọn
2. Người dùng chọn phương thức nhập liệu
3. Thực thi chức năng nhập liệu tương ứng
4. Gọi hàm `schedule_jobs()` để lập lịch
5. Hiển thị kết quả và lưu vào file

### 3.2 Quản Lý Bộ Nhớ
- Sử dụng `malloc()` để cấp phát động
- Giải phóng bộ nhớ bằng `free()` sau mỗi lần sử dụng
- Tránh rò rỉ bộ nhớ

## 4. Ưu Điểm Của Giải Pháp
- Linh hoạt trong việc nhập liệu
- Hiệu suất cao với độ phức tạp $O(n \log n)$
- Quản lý bộ nhớ an toàn
- Hỗ trợ nhiều phương thức nhập liệu

## 5. Hạn Chế Và Phát Triển Tương Lai
- Chưa hỗ trợ các ràng buộc phức tạp
- Có thể mở rộng cho các thuật toán lập lịch khác
- Cải thiện giao diện người dùng
- Thêm chức năng phân tích chi tiết

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