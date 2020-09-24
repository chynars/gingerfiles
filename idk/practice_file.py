

filename = input('enter the file name:')
with open(filename, 'r') as a_file, open("a_total.txt", "w") as a_total:
        contents = a_file.read()
        number_list = contents.split()
        counter = 0
        for number in number_list:
            counter = counter + int(number)
            sum_of = str(counter)
        print(counter)
        a_total.write(sum_of)
