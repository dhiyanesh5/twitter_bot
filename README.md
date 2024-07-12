# Twitter Bot with Tweepy

This project is a Twitter bot that interacts with your Twitter account using the Tweepy library. It performs actions such as following users and liking tweets based on specific keywords.

## Features

- Prints your Twitter account details
- Follows users who meet certain criteria
- Likes tweets based on a search keyword

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/dhiyanesh5/twitter_bot.git
    cd twitter-bot
    ```

2. **Install the required packages**:
    ```sh
    pip install tweepy
    ```

3. **Set up your Twitter Developer Account**:
    - Go to the [Twitter Developer site](https://developer.twitter.com/en/apps) and sign in with your Twitter account.
    - Create an application to obtain your API Key, API Secret Key, Access Token, and Access Token Secret.

4. **Configure your credentials**:
    - Rename the `.env.example` file to `.env`.
    - Add your Twitter API credentials to the `.env` file:
      ```env
      CONSUMER_KEY=your_consumer_key
      CONSUMER_SECRET=your_consumer_secret
      ACCESS_TOKEN=your_access_token
      ACCESS_TOKEN_SECRET=your_access_token_secret
      ```

## Usage

1. **Run the script**:
    ```sh
    python twitter_bot.py
    ```

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.
