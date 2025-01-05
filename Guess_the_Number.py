import random
import time

# Leaderboard to track high scores
leaderboard = []

def guess_the_number():
    print("🎉 Welcome to the Ultimate Guessing Game 2.0! 🎉")
    print("Can you beat the AI's challenge?")
    time.sleep(1)

    # Choose difficulty level
    print("\nSelect a difficulty level:")
    print("1. Easy (1 to 50, unlimited guesses)")
    print("2. Medium (1 to 100, 10 guesses)")
    print("3. Hard (1 to 200, 5 guesses)")
    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == '1':
        max_num, max_attempts = 50, float('inf')
    elif difficulty == '2':
        max_num, max_attempts = 100, 10
    elif difficulty == '3':
        max_num, max_attempts = 200, 5
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        max_num, max_attempts = 100, 10

    secret_number = random.randint(1, max_num)
    attempts = 0
    score = 100
    hints_used = 0
    start_time = time.time()

    print(f"\n🎯 I'm thinking of a number between 1 and {max_num}. Can you guess it?")
    if max_attempts != float('inf'):
        print(f"💡 You have {max_attempts} attempts. Use them wisely!")

    while attempts < max_attempts:
        try:
            guess = input("\nYour guess (or type 'hint' for help): ").strip().lower()
            
            # Provide a hint if requested
            if guess == 'hint':
                hints_used += 1
                score -= 5
                if secret_number % 2 == 0:
                    print("🔍 Hint: The number is even.")
                else:
                    print("🔍 Hint: The number is odd.")
                continue
            
            # Easter egg mode
            if guess == 'cheat':
                print(f"🤫 The secret number is {secret_number}. (Score penalty applied!)")
                score -= 20
                continue

            guess = int(guess)
            attempts += 1
            score -= 10

            # Check the guess
            if guess < secret_number:
                print("📉 Too low!")
            elif guess > secret_number:
                print("📈 Too high!")
            else:
                time_taken = round(time.time() - start_time, 2)
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts and {time_taken} seconds!")
                print(f"🏆 Your final score is: {score}")
                
                # Add to leaderboard
                leaderboard.append({"attempts": attempts, "score": score, "time": time_taken})
                leaderboard.sort(key=lambda x: (-x['score'], x['time']))
                
                print("\n📜 Leaderboard:")
                for rank, entry in enumerate(leaderboard[:5], 1):
                    print(f"{rank}. Score: {entry['score']}, Attempts: {entry['attempts']}, Time: {entry['time']}s")
                
                break
        except ValueError:
            print("❌ Please enter a valid number.")

        # Check if attempts are exhausted
        if attempts == max_attempts:
            print(f"\n💔 You've run out of attempts! The secret number was {secret_number}. Better luck next time!")
    
    # Replay option
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("\nThanks for playing! See you next time. 👋")

# Start the game
guess_the_number()
