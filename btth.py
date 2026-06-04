blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("=======================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_inventory(blood_inventory)
        elif choice == "2":
            add_blood_bag(blood_inventory)
        elif choice == "3":
            update_expiry(blood_inventory)
        elif choice == "4":
            remove_blood_bag(blood_inventory)
        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

def display_inventory(inventory):
    print("\n--- DANH SÁCH KHO MÁU ---")
    if not inventory:
        print("Kho máu hiện chưa có túi máu nào.")
        return
        
    print(f"{'Mã Túi':<7} | {'Người Hiến':<15} | {'Nhóm Máu':<8} | {'Thể Tích':<8} | {'Ngày Hết Hạn'}")
    print("-" * 65)
    
    total_volume = 0
    for item in inventory:
        parts = item.split('-')
        ma_tui = parts[0]
        nguoi_hien = parts[1]
        nhom_mau = parts[2]
        the_tich = int(parts[3])
        ngay_het_han = parts[4]
        
        total_volume += the_tich
        print(f"{ma_tui:<7} | {nguoi_hien:<15} | {nhom_mau:<8} | {the_tich:<3} ml   | {ngay_het_han}")
        
    print("-" * 65)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")

def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")
    
    ma_tui = input("Nhập mã túi máu mới: ").strip()
    if not ma_tui:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    ma_tui = ma_tui.replace(" ", "").upper()
    
    for item in inventory:
        if item.split('-')[0] == ma_tui:
            print(f"Lỗi: Mã túi máu {ma_tui} đã tồn tại! Vui lòng nhập mã khác.")
            return

    nguoi_hien = input("Nhập tên người hiến: ").strip()
    if not nguoi_hien:
        print("Lỗi: Tên người hiến không được để trống!")
        return
    nguoi_hien = nguoi_hien.title()

    nhom_mau = input("Nhập nhóm máu: ").strip()
    if not nhom_mau:
        print("Lỗi: Nhóm máu không được để trống!")
        return
    nhom_mau = nhom_mau.replace(" ", "").upper()

    the_tich_str = input("Nhập thể tích (ml): ").strip()
    if not the_tich_str:
        print("Lỗi: Thể tích không được để trống!")
        return
    if not the_tich_str.isdigit() or int(the_tich_str) <= 0:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return
    the_tich = the_tich_str

    ngay_het_han = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()
    if not ngay_het_han:
        print("Lỗi: Ngày hết hạn không được để trống!")
        return

    new_bag = "-".join([ma_tui, nguoi_hien, nhom_mau, the_tich, ngay_het_han])
    inventory.append(new_bag)
    
    print(f"\nThành công: Đã nhập túi máu {ma_tui} vào kho!")
    print("\nSau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(new_bag)

def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    ma_tui = input("Nhập mã túi máu cần cập nhật: ").strip()
    if not ma_tui:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    ma_tui = ma_tui.replace(" ", "").upper()

    found_index = -1
    for i, item in enumerate(inventory):
        if item.split('-')[0] == ma_tui:
            found_index = i
            break

    if found_index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {ma_tui} trong kho!")
        return

    ngay_moi = input("Nhập ngày hết hạn mới: ").strip()
    if not ngay_moi:
        print("Lỗi: Ngày hết hạn mới không được để trống!")
        return

    parts = inventory[found_index].split('-')
    parts[4] = ngay_moi
    
    inventory[found_index] = "-".join(parts)
    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {ma_tui}!")

def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")
    ma_tui = input("Nhập mã túi máu cần xuất/hủy: ").strip()
    if not ma_tui:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    ma_tui = ma_tui.replace(" ", "").upper()

    found_item = None
    for item in inventory:
        if item.split('-')[0] == ma_tui:
            found_item = item
            break

    if found_item:
        inventory.remove(found_item)
        print(f"\nThành công: Đã xuất túi máu {ma_tui} khỏi kho!")
    else:
        print(f"Lỗi: Không tìm thấy túi máu {ma_tui} trong kho!")

if __name__ == "__main__":
    main()