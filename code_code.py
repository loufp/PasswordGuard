def per(): # The function processes passwords (from the pas.txt function) <--> Функция обрабатывает пароли (из функции pas.txt
    with open('/Users/kirillkirill13let/Desktop/арppassword — основания/minicode/codes/pas.txt', 'r') as file:
        for line in file:
            password = line.strip()
            if password:
                yield [password]
                
def main(): # The function counts the number of passwords <--> Функция считает количество паролей
    count = 0
    with open('/Users/kirillkirill13let/Desktop/арppassword — основания/minicode/codes/pas.txt', 'r') as f:
        for line in f:  
            if line.strip():
                count += 1
    return count
