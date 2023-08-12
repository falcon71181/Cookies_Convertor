import json

def parse_netscape_cookie_line(line):
    parts = line.strip().split('\t')
    if len(parts) >= 7:
        return {
            'domain': parts[0],
            'flag': parts[1] == 'TRUE',
            'path': parts[2],
            'secure': parts[3] == 'TRUE',
            'expiry': parts[4],
            'name': parts[5],
            'value': parts[6]
        }
    return None

input_filename = "cookies.net"
with open(input_filename, "r") as file:
    input_text = file.read()

input_lines = input_text.strip().split('\n')
cookies = [parse_netscape_cookie_line(line) for line in input_lines]
cookies = [cookie for cookie in cookies if cookie is not None]

# Convert to JSON format
json_output = json.dumps(cookies, indent=4)

# Write the output to cookies.json
output_filename = "cookies.json"
with open(output_filename, "w") as file:
    file.write(json_output)

print(f"Conversion completed ! JSON output saved to {output_filename}.")
