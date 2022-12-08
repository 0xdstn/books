#!/usr/bin/env python3

import csv

print('')
print('[*] Importing from goodreads_library_export.csv')
print('')

output = ''

with open('goodreads_library_export.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        print('[+] ' + row[1])
        print('    Author:     ' + row[2])
        print('    ISBN:       ' + row[5])
        print('    ISBN13:     ' + row[6])
        print('    Rating:     ' + row[7])
        print('    Date Read:  ' + row[14])
        print('    Date Add:   ' + row[15])
        print('    Shelves:    ' + row[16])
        print('    Ex Shelf:   ' + row[18])
        print('    Review:     ' + row[19])
        print('    Read Count: ' + row[22])
        print('')

        status = 'WANT'
        if row[18] == 'read':
            status = 'READ'
        elif row[18] == 'currently-reading':
            status = 'CURR'

        review = 'NONE'
        if row[19] != '':
            review = row[19]

        startDate = 'MISSING'
        if row[15] != '':
            startDate = row[15].replace('/','-')

        endDate = 'NONE'
        if row[18] == 'read':
            if row[14] != '':
                endDate = row[14].replace('/','-')
            elif row[15] != '':
                endDate = row[15].replace('/','-')

        #line = 'CURR | 9781935209539 | Be Free Where You Are | Thich Nhat Hanh | buddhism,self | 0000-00-00 | 0000-00-00 | 0 | This is a review'
        line = ' | '.join([
            status,
            row[1].split(' (')[0], # title
            row[2], # author
            endDate,
            row[7], # rating
            review
        ])
        output += line+'\n'

#print(output)

dataFile = open("data.txt", "w")
dataFile.write(output)
dataFile.close()

# 0 Book Id
# 1 Title
# 2 Author
# 3 Author l-f
# 4 Additional Authors
# 5 ISBN
# 6 ISBN13
# 7 My Rating
# 8 Average Rating
# 9 Publisher
# 10 Binding
# 11 Number of Pages
# 12 Year Published
# 13 Original Publication Year
# 14 Date Read
# 15 Date Added
# 16 Bookshelves
# 17 Bookshelves with positions
# 18 Exclusive Shelf
# 19 My Review
# 20 Spoiler
# 21 Private Notes
# 22 Read Count
# 23 Owned Copies
