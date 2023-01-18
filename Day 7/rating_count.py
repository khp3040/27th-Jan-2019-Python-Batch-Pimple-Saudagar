ratings = open('ml-1m/ratings.dat', 'r')

rating_count = dict()
for row in ratings:
    row = row.strip()
    columns = row.split('::')
    movieId = columns[1]
    if movieId in rating_count:
        rating_count[movieId] += 1
    else:
        rating_count[movieId] = 1

for movieId, count in sorted(rating_count.items(), key=lambda x:x[1],reverse=True)[:5]:
    print movieId, count

