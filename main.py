from dotenv import load_dotenv
from ia.bot import Bot


def main() -> None:
    load_dotenv()

    name_to_find = "Michel Jackson"

    bot = Bot("assistant", [
        {
            "role": "system",
            "content": f"character is a celebrity named {name_to_find}. User will ask character question about his history and personnality, trying to find the name of the character. character will never give his name, unless the user find who he is."
        }
    ])

    while True:
        user_input = input("\n> ")
        print(bot.send_message_and_get_response(user_input))
        if name_to_find in user_input:
            break
    
    print("\nCongrats, you win!")


if __name__ == "__main__":
    main()
