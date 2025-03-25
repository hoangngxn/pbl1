#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Structure to represent a job
typedef struct {
    int job_id;
    int processing_time;
    int deadline;
} Job;

// Comparison function for qsort to sort jobs by deadline
int compare_jobs(const void* a, const void* b) {
    Job* job1 = (Job*)a;
    Job* job2 = (Job*)b;
    return job1->deadline - job2->deadline;
}

// Job scheduling function
void schedule_jobs(int n, int* processing_times, int* deadlines, int* completed_jobs, int* schedule) {
    // Create an array of Job structures
    Job* jobs = malloc(n * sizeof(Job));
    for (int i = 0; i < n; i++) {
        jobs[i].job_id = i + 1;
        jobs[i].processing_time = processing_times[i];
        jobs[i].deadline = deadlines[i];
    }

    // Sort jobs by deadline
    qsort(jobs, n, sizeof(Job), compare_jobs);

    int current_time = 0;
    int job_count = 0;

    // Iterate through sorted jobs
    for (int i = 0; i < n; i++) {
        // Check if job can be completed before its deadline
        if (current_time + jobs[i].processing_time <= jobs[i].deadline) {
            schedule[job_count] = jobs[i].job_id;
            current_time += jobs[i].processing_time;
            job_count++;
        }
    }

    // Set the number of completed jobs
    *completed_jobs = job_count;

    // Free dynamically allocated memory
    free(jobs);
}

// Function to get input manually
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

// Function to load input from file
int load_from_file(char* filename, int* n, int* processing_times, int* deadlines) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Không thể mở file %s\n", filename);
        return 0;
    }

    if (fscanf(file, "%d", n) != 1) {
        printf("Lỗi đọc số lượng công việc\n");
        fclose(file);
        return 0;
    }

    for (int i = 0; i < *n; i++) {
        if (fscanf(file, "%d", &processing_times[i]) != 1) {
            printf("Lỗi đọc thời gian xử lý\n");
            fclose(file);
            return 0;
        }
    }

    for (int i = 0; i < *n; i++) {
        if (fscanf(file, "%d", &deadlines[i]) != 1) {
            printf("Lỗi đọc thời hạn\n");
            fclose(file);
            return 0;
        }
    }

    fclose(file);
    return 1;
}

// Function to save output to a timestamped file
void save_output(int completed_jobs, int* schedule, int n) {
    // Generate timestamped filename
    time_t now;
    time(&now);
    struct tm *local = localtime(&now);
    char filename[50];
    sprintf(filename, "%04d%02d%02d_%02d%02d%02d.out", 
            local->tm_year + 1900, local->tm_mon + 1, local->tm_mday,
            local->tm_hour, local->tm_min, local->tm_sec);

    // Open file for writing
    FILE* outfile = fopen(filename, "w");
    if (outfile == NULL) {
        printf("Không thể tạo file kết quả\n");
        return;
    }

    // Write number of completed jobs
    fprintf(outfile, "%d\n", completed_jobs);

    // Write schedule
    for (int i = 0; i < completed_jobs; i++) {
        fprintf(outfile, "%d ", schedule[i]);
    }
    fprintf(outfile, "\n");

    fclose(outfile);
    printf("Kết quả đã được lưu vào file %s\n", filename);
}

int main() {
    int choice, n;
    int processing_times[100];  // Assuming max 100 jobs
    int deadlines[100];
    int schedule[100];
    int completed_jobs;
    char filename[100];

    while (1) {
        // Display menu
        printf("\n--- Lập Lịch Công Việc ---\n");
        printf("1. Nhập thủ công\n");
        printf("2. Tải từ file .inp\n");
        printf("3. Thoát\n");
        printf("Chọn: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                // Manual input
                manual_input(&n, processing_times, deadlines);
                break;
            case 2:
                // File input
                printf("Nhập tên file .inp: ");
                scanf("%s", filename);
                if (!load_from_file(filename, &n, processing_times, deadlines)) {
                    continue;
                }
                break;
            case 3:
                // Exit
                printf("Thoát chương trình.\n");
                return 0;
            default:
                printf("Lựa chọn không hợp lệ. Vui lòng thử lại.\n");
                continue;
        }

        // Schedule jobs
        schedule_jobs(n, processing_times, deadlines, &completed_jobs, schedule);

        // Print results to console
        printf("Số công việc hoàn thành: %d\n", completed_jobs);
        printf("Trình tự công việc: ");
        for (int i = 0; i < completed_jobs; i++) {
            printf("%d ", schedule[i]);
        }
        printf("\n");

        // Save output to timestamped file
        save_output(completed_jobs, schedule, n);
    }

    return 0;
}