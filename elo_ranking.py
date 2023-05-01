import sys
import math

# Function to calculate the expected outcome of a match
def expected_outcome(rating_a, rating_b):
    return 1 / (1 + math.pow(10, (rating_b - rating_a) / 400))

# Function to update the Elo ratings after a match
def update_elo(rating, expected, actual, k_factor=32):
    return rating + k_factor * (actual - expected)

# Main function
def main(items):
    # Initialize Elo ratings
    elo_ratings = {item: 1200 for item in items}

    # Iterate through all unique pairs of items
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            # Get user input for comparison
            print(f"Compare {items[i]} and {items[j]} (1/2/equal): ")
            result = input().strip().lower()

            # Calculate expected outcomes for each item
            expected_i = expected_outcome(elo_ratings[items[i]], elo_ratings[items[j]])
            expected_j = expected_outcome(elo_ratings[items[j]], elo_ratings[items[i]])

            # Update Elo ratings based on user input
            if result == '1':
                elo_ratings[items[i]] = update_elo(elo_ratings[items[i]], expected_i, 1)
                elo_ratings[items[j]] = update_elo(elo_ratings[items[j]], expected_j, 0)
            elif result == '2':
                elo_ratings[items[i]] = update_elo(elo_ratings[items[i]], expected_i, 0)
                elo_ratings[items[j]] = update_elo(elo_ratings[items[j]], expected_j, 1)
            elif result == 'equal':
                elo_ratings[items[i]] = update_elo(elo_ratings[items[i]], expected_i, 0.5)
                elo_ratings[items[j]] = update_elo(elo_ratings[items[j]], expected_j, 0.5)

    # Sort items by Elo rating
    sorted_items = sorted(elo_ratings.items(), key=lambda x: x[1], reverse=True)

    # Print the ranking
    print("Ranking:")
    for rank, (item, rating) in enumerate(sorted_items, start=1):
        print(f"{rank}. {item} ({rating:.2f})")

if __name__ == "__main__":
    main(sys.argv[1:])
