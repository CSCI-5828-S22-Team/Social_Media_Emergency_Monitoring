from test_functions import *
from mock_tweets import mock_tweets

print("\n----RUNNING DATA ACQUISITION TESTS----")
all_tests = [
    read_in_tweets(mock_tweets),
    check_length(mock_tweets),
    convert_to_dt(mock_tweets),
    check_all_types(mock_tweets),
    check_tweet_size(mock_tweets),
    check_tokens(access_token, access_token_secret, consumer_key, consumer_secret),
    mock_api(pickle_file)
    ]
out_str = ""
successes = 0

for test in all_tests:
    if test == True:
        out_str += '✅ '
        successes += 1
    else:
        out_str += '🚫 '
print('\n\t{0}'.format(out_str))
