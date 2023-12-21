import datetime

if __name__ == "__main__":
   raise RuntimeError("Please run the main.py file !")

def print_warning(text):
  current_time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
  colored_text = f"\033[93m{current_time} [WARN] : {text}\033[0m"
  print(colored_text)

def print_error(text):
  current_time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
  colored_text = f"\033[91m{current_time} [ERROR] : {text}\033[0m"
  print(colored_text)

def print_info(text):
  current_time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
  colored_text = f"\033[94m{current_time} [INFO] : {text}\033[0m"
  print(colored_text)