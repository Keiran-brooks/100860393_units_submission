import os, base64


# base64_string =" R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
# base64_bytes = base64_string.encode("ascii")

# sample_string_bytes = base64.b64decode(base64_bytes)
# sample_string = sample_string_bytes.decode("ascii")


def get_current_working_directory():
  return os.getcwd()

def encode_string(str_to_encode):
  return base64.b64encode(str_to_encode.encode("ascii")).decode("ascii")

def decode_string(base64_str_to_decode):
  """ Decodes a string encoded in base64"""
  return base64.b64decode(base64_str_to_decode.encode("ascii")).decode("ascii")

  

if __name__ == "__main__":
  print(get_current_working_directory())
  print(encode_string("Python is a cool programming language!"))
  # should print UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE=
  str_to_decode = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE="
  print(decode_string(str_to_decode))
  # should print Python is a cool programming language!