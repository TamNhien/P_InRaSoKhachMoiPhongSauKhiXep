def assign_guests(N, M, doankhach):
    rooms = [0] * N  # Tạo list rooms chứa số lượng khách trong từng phòng, ban đầu tất cả phòng đều trống

    for guests in doankhach:
        for i in range(N):
            if guests == 0:  # Kiểm tra nếu không còn khách trong đoàn khách
                break

            if rooms[i] < 2:  # Nếu phòng chưa đủ 2 khách, xếp thêm khách vào phòng đó
                rooms[i] += 1
                guests -= 1
            elif i < N - 1 and rooms[i + 1] == 0:  # Nếu phòng kế tiếp trống và phòng hiện tại đã đủ 2 khách, xếp khách cuối vào phòng kế tiếp
                rooms[i + 1] = 1
                guests -= 1

    return rooms

# Ví dụ 1
N1, M1 = 7, 3
doankhach1 = [3, 7, 3]
result1 = assign_guests(N1, M1, doankhach1)
print(*result1)

# Ví dụ 2
N2, M2 = 5, 3
doankhach2 = [2, 3, 2]
result2 = assign_guests(N2, M2, doankhach2)
print(*result2)
