# Modern historical reconstruction, created 2026-11-04.
import json
from mrjob.job import MRJob

class ReviewRatings(MRJob):
    def mapper(self, _, line):
        review = json.loads(line)
        yield review["business_id"], float(review["rating"])

    def reducer(self, business_id, ratings):
        total, count = 0.0, 0
        for rating in ratings:
            total += rating
            count += 1
        yield business_id, total / count

if __name__ == "__main__":
    ReviewRatings.run()
