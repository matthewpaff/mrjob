# Modern historical reconstruction, created 2026-11-04.
import json
import math
from mrjob.job import MRJob

class ReviewRatings(MRJob):
    def mapper(self, _, line):
        try:
            review = json.loads(line)
            if not isinstance(review, dict):
                raise ValueError("Expected an object")
            business_id = review["business_id"]
            rating = float(review["rating"])
            if not isinstance(business_id, (str, type(u""))) or not business_id:
                raise ValueError("Expected a business identifier")
            if math.isnan(rating) or math.isinf(rating) or not 0 <= rating <= 5:
                raise ValueError("Rating is outside 0-5")
        except (ValueError, TypeError, KeyError, OverflowError):
            self.increment_counter("input", "invalid_review", 1)
            return
        yield business_id, rating

    def reducer(self, business_id, ratings):
        total, count = 0.0, 0
        for rating in ratings:
            total += rating
            count += 1
        yield business_id, total / count

if __name__ == "__main__":
    ReviewRatings.run()
