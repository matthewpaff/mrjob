# Roadmap example

Input is one JSON object per line with `business_id` and numeric `rating` in the 0-5 range. `ReviewRatings` outputs each business's mean rating. Invalid records increment `input.invalid_review`. A combiner transports sums and counts rather than incorrectly averaging partial averages.

See RECONSTRUCTION.md for provenance and verification limits.
