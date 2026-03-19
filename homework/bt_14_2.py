import json

def main():
# Đường dẫn đến file json của bạn
    file_path = 'D:\\VS Code\\AIGEN\\data\\processed\\vector_store.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                # Vì data là một list các dictionary:
                # Chúng ta lấy độ dài của list nằm trong key "embedding" của từng phần tử
        dimensions = []
        for item in data:
            if 'embedding' in item:
                dimensions.append(len(item['embedding']))
        
        # Kiểm tra tính đồng nhất
        unique_dimensions = set(dimensions)
        print(f"Tổng số vector: {len(data)}")
        
        if len(unique_dimensions) == 1:
            dim = list(unique_dimensions)[0]
            print(f"✅ Tất cả các vector đều cùng số chiều: {dim}")
        else:
            print(f"❌ Cảnh báo: Các vector CÓ ĐỘ DÀI KHÁC NHAU!")
            print(f"Các loại số chiều tìm thấy: {unique_dimensions}")
            
            # In ra các ID có số chiều khác biệt để kiểm tra
            # for key, dim in dimensions.items():
            #     # Ví dụ: chỉ in 5 cái đầu tiên nếu có quá nhiều
            #     print(f" - ID: {key} có số chiều: {dim}")

    except Exception as e:
        print(f"Lỗi: {e}")
if __name__ == "__main__":
    main()