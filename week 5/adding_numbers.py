import sys
def add_them_all(filename):
    sum = 0
    ### Your code here
    filename = []
    with open(filename, 'r') as file_name, open('filetotal.txt','w') as filetotal:
        contents = file_name.read()
        number_list = contents.split()
        counter = 0 
        for line in number_list:
            counter = counter + int(line)
            total = str(counter)
        print(total)
        filetotal.write(total)
    ### End of your code
    return sum
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))