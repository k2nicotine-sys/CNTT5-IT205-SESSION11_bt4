product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]
def input_positive_integer(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue
            return value
        except ValueError:
            print("Số lượng mua/Nhập kho không hợp lệ")
while True:
    try:
        choice = int(input("""
===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
2. Bán sản phẩm cho khách hàng
3. Nhập thêm hàng vào kho
4. Xem báo cáo doanh thu
5. Thoát chương trình
"""))
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    match choice:
        case 1:
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")
                for index, product in enumerate(product_list, start=1):
                    quantity = product["quantity"]
                    if quantity == 0:
                        status = "Hết hàng"
                    elif quantity <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(
                        f"{index}. "
                        f"Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Trạng thái: {status}"
                    )
        case 2:
            product_id = input(
                "Nhập mã sản phẩm khách muốn mua: "
            ).strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    buy_quantity = input_positive_integer(
                        "Nhập số lượng khách mua: "
                    )
                    if buy_quantity > product["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                    else:
                        product["quantity"] -= buy_quantity
                        product["sold"] += buy_quantity
                        total_money = (
                            buy_quantity * product["price"]
                        )
                        print("Bán hàng thành công")
                        print(
                            f"Khách cần thanh toán: {total_money}"
                        )
                    break
            if not found:
                print("Không tìm thấy sản phẩm cần bán")
        case 3:
            product_id = input(
                "Nhập mã sản phẩm cần nhập thêm: "
            ).strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    add_quantity = input_positive_integer(
                        "Nhập số lượng nhập thêm: "
                    )
                    product["quantity"] += add_quantity
                    print("Nhập kho thành công")
                    break
            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")
        case 4:

            total_revenue = 0
            max_sold = 0
            best_seller = ""
            sold_exist = False

            for product in product_list:
                if product["sold"] > 0:
                    sold_exist = True
                    break
            if not sold_exist:
                print("Chưa có doanh thu phát sinh.")
            else:
                print(
                    "\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY ====="
                )
                for index, product in enumerate(
                    product_list,
                    start=1
                ):
                    revenue = (
                        product["price"] * product["sold"]
                    )

                    total_revenue += revenue

                    print(
                        f"{index}. "
                        f"{product['product_name']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Doanh thu: {revenue}"
                    )

                    if product["sold"] > max_sold:
                        max_sold = product["sold"]
                        best_seller = product["product_name"]

                print(f"\nTổng doanh thu: {total_revenue}")
                print(
                    f"Sản phẩm bán chạy nhất: {best_seller}"
                )

        case 5:

            print("Thoát chương trình.")
            break

        case _:

            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")