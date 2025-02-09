from dotenv import load_dotenv
from ia.bot import Bot


def main() -> None:
    load_dotenv()

    bot = Bot("character", [
        {
            "role": "system",
            "content": "character is a celebrity named Michel Jakson. User will ask character question about his history and personnality, trying to find the name of the character. character will never give his name, unless the user find who he is."
        }
    ])

    while True:
        user_input = input("> ")
        print(bot.send_message_and_get_response(user_input))
        # if user_input.find("Michel Jakson"):
        #     break
    
    print("\nCongrats, you win!")


if __name__ == "__main__":
    main()
