import argparse
import glob
import os

import pandas as pd


def get_command_line_args():
    parser = argparse.ArgumentParser(description="ゲスのゲスによるゲスのための分析ツール")

    parser.add_argument("input", help="input file path")
    parser.add_argument("keywd", help="keyword to search")

    args = parser.parse_args()
    return args


def open_input_file(input: str) -> "DataFrame":
    try:
        input_df = pd.read_csv(input)
        return input_df
    except FileNotFoundError as e:
        print("cannot found {}\n{}".format(input, e))
    except Exception as e:
        print("{}".format(e))


if __name__ == "__main__":
    args = get_command_line_args()
    input_df = open_input_file(args.input)
    # print (input_df.columns)
    # print (input_df['tweet_full_text'])
    print(input_df.tail(20)["user_screen_name"])
    print(input_df.tail(20)["tweet_ceated_at"])
    print(input_df.tail(20)["tweet_full_text"])
    print(input_df[input_df["user_screen_name"].str.contains("Emb")]["user_screen_name"])
    print(input_df.iloc[10668])
    print(input_df["user_screen_name"].value_counts())
    print(input_df.iloc[23498]["tweet_full_text"])
    print(input_df.iloc[23499]["tweet_full_text"])
