#!/usr/bin/env python3

header = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" /><link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="main.css" /><title>Books</title></head><body><h1><a href="index.html">Books</a></h1>'
header += '<nav>'
header += '<a href="2022.html">2022</a> | <a href="2021.html">2021</a> | <a href="2020.html">2020</a> | <a href="2019.html">2019</a> | <a href="prior.html">prior</a><br><br>'
header += '<a href="tags.html">tags</a> | <a href="toread.html">to read</a>'
header += '</nav>'
footer = '</body></html>'

index = header

with open('current.txt') as f:
    current = [x.strip().split(' | ') for x in f.readlines()]
    f.close()

index += '<h2>Currently Reading</h2>'

index += '<ul>'
for b in current:
    index += '<li><strong>' + b[0] + '</strong> <em>by ' + b[1] + '</em></li>'
index += '</ul>'

index += '<p>'
index += '<em>Source code: <a href="https://github.com/0xdstn/books" target="_blank">https://github.com/0xdstn/books</a></em><br>'
index += '<em>About: <a href="https://tilde.town/~dustin/projects/books" target="_blank">https://tilde.town/~dustin/projects/books</a></em>'
index += '</p>'

index += footer

indexFile = open('index.html', "w+")
indexFile.write(index)
indexFile.close()

for yr in ["2022","2021","2020","2019","prior"]:
    year = header

    with open('read-'+yr+'.txt') as f:
        y = [x.strip().split(' | ') for x in f.readlines()]
        f.close()

    year += '<h2>'+yr+'</h2>'

    year += '<ul>'
    for b in y:
        year += '<li><strong>' + b[0] + '</strong> <em>by ' + b[1] + '</em></li>'
    year += '</ul>'

    year += footer

    yearFile = open(yr+'.html', "w+")
    yearFile.write(year)
    yearFile.close()

toRead = header

with open('toread.txt') as f:
    tor = [x.split(' | ') for x in f.readlines()]
    f.close()

toRead += '<h2>To Read</h2>'

toRead += '<ul>'
for b in tor:
    tags = b[2].strip().split(',')
    tHtml = ''
    if tags[0] != '':
        tHtml += ' ('
        for t in tags:
            tHtml +=  '<a href="tag-'+t+'.html">'+t+'</a>,' 
        tHtml = tHtml[:len(tHtml)-1]
        tHtml += ')'
    else:
        tHtml += '(<a href="tag-untagged.html">untagged</a>)'
    toRead += '<li><strong>' + b[0] + '</strong> <em>by ' + b[1] + '</em>' + tHtml + '</li>'
toRead += '</ul>'

toRead += footer

toReadFile = open('toread.html', "w+")
toReadFile.write(toRead)
toReadFile.close()

allTags = []
books = []
for b in tor:
    tags = b[2].strip().split(',')
    if tags[0] != '':
        for t in tags:
            if t not in allTags:
                allTags.append(t)
                books.append([b])
            else:
                books[allTags.index(t)].append(b)
    else:
        if 'untagged' not in allTags:
            allTags.append('untagged')
            books.append([b])
        else:
            books[allTags.index('untagged')].append(b)

for i,t in enumerate(allTags):
    tag = header

    tag += '<h2>Tag: ' + t + '</h2>'

    tag += '<ul>'
    for b in books[i]:
        tag += '<li><strong>' + b[0] + '</strong> <em>by ' + b[1] + '</em></li>'
    tag += '</ul>'

    tag += footer

    tagFile = open('tag-' + t + '.html', "w+")
    tagFile.write(tag)
    tagFile.close()

tags = header

tags += '<h2>Tags:</h2>'

tags += '<ul>'
for i,t in enumerate(allTags):
    tags += '<li><a href="tag-'+t+'.html">' + t + '</strong> <em>(' + str(len(books[i])) + ')</em></li>'
tags += '</ul>'

tags += footer

tagsFile = open('tags.html', "w+")
tagsFile.write(tags)
tagsFile.close()

