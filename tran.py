from PIL import Image
import os

# Đường dẫn đến thư mục chứa ảnh gốc
input_folder = 'H'  # Thay thế bằng đường dẫn đến thư mục chứa ảnh của bạn
# Đường dẫn đến thư mục lưu ảnh sau khi chuyển đổi
output_folder = 'happy'

# Tạo thư mục output nếu chưa có
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Bộ đếm để đổi tên hình ảnh từ H1 đến Hn
counter = 1

# Duyệt qua tất cả các tệp trong thư mục input
for filename in os.listdir(input_folder):
    # Kiểm tra định dạng tệp ảnh
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        img_path = os.path.join(input_folder, filename)
        
        # Mở ảnh
        img = Image.open(img_path)
        
        # Chuyển sang ảnh trắng đen
        img = img.convert('L')
        
        # Thay đổi kích thước ảnh thành 48x48
        img = img.resize((48, 48))
        
        # Đổi tên hình ảnh, ví dụ: H1.png, H2.png, v.v.
        new_filename = f"H{counter}.png"
        output_path = os.path.join(output_folder, new_filename)
        
        # Lưu ảnh đã chuyển đổi vào thư mục output
        img.save(output_path)

        print(f"Đã xử lý và lưu: {output_path}")
        
        # Tăng bộ đếm
        counter += 1
