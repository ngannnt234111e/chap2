def convert_str_to_int(arr_str):
    arr_int=[]
    for s in arr_str:
        arr_int.append(int(s))
    return arr_int

def print_arr_perline(arr_int):
    for value in arr_int:
        print(value)
def get_even_digits(arr_int):
    arr_int_even=[]
    for value in arr_int:
        if value%2==0:
            arr_int_even.append(value)
        return arr_int_even
def even_numbers_way2(arr_int):
    return [x for x in arr_int if x%2==0 and x>0]


from urllib.parse import urlparse, parse_qs


def convert_str_to_int(arr_str):
    arr_int = []
    for s in arr_str:
        arr_int.append(int(s))
    return arr_int


def print_arr_perline(arr_int):
    for value in arr_int:
        print(value)


def get_even_digits(arr_int):
    arr_int_even = []
    for value in arr_int:
        if value % 2 == 0:
            arr_int_even.append(value)
    return arr_int_even


def even_numbers_way2(arr_int):
    return [x for x in arr_int if x % 2 == 0 and x > 0]


def analyze_url(url):
    parsed_url = urlparse(url)

    result = {
        "protocol": parsed_url.scheme,
        "hostname": parsed_url.hostname,
        "domain_name": parsed_url.netloc,
        "directory": '/'.join(parsed_url.path.split('/')[:-1]),
        "filename": parsed_url.path.split('/')[-1] if '/' in parsed_url.path else '',
        "query_parameters": parse_qs(parsed_url.query)
    }

    return result


def process_numbers():
    s = input("Nhap chuoi cac so co ngan cach []:")
    arr_str = s.split(";")
    arr_int = convert_str_to_int(arr_str)
    print("Original array:")
    print_arr_perline(arr_int)
    arr_int_even = get_even_digits(arr_int)
    print("Even numbers:")
    print_arr_perline(arr_int_even)
    print("counts", len(arr_int_even))


def process_url():
    url = input("Nhập URL bạn muốn phân tích: ")
    analyzed_data = analyze_url(url)
    print("\nPhân tích URL:")
    print(f"Giao thức (Protocol): {analyzed_data['protocol']}")
    print(f"Tên miền (Hostname): {analyzed_data['hostname']}")
    print(f"Tên miền đầy đủ (Domain name): {analyzed_data['domain_name']}")
    print(f"Thư mục (Directory): {analyzed_data['directory']}")
    print(f"Tên file (Filename): {analyzed_data['filename']}")
    print(f"Các thông số truy vấn (Query Parameters): {analyzed_data['query_parameters']}")


def main():
    process_numbers()
    print("\n" + "=" * 50 + "\n")
    process_url()


if __name__ == "__main__":
    main()

# For demonstration purposes, let's simulate user input and run the script
import io
import sys


def simulate_input(input_values):
    def mock_input(prompt):
        print(prompt, end='')
        return input_values.pop(0)

    original_stdin = sys.stdin
    sys.stdin = io.StringIO()
    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        main()
    finally:
        sys.stdin = original_stdin
        __builtins__.input = original_input


# Simulate user input
simulate_input([
    "1;2;3;4;5;6",
    "https://www.example.com/path/to/file.html?param1=value1&param2=value2"
])