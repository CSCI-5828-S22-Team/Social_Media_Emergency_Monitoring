mock_tweets = {
    1 : { "user_screen_name" : 'Cathy69118239', "created_at" : '2022-04-14 12:57:43', "text" : 'San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    2 : { "user_screen_name" : 'prasadraghava', "created_at" : '2022-04-14 15:41:18', "text" : 'KGF2 is not a fire or water.\nKGF2 is a VOLCANO🌋\nKGF2 is an EARTHQUAKE🌎\nKGF2 is a THUNDERSTORM⛈️\nKGF2 is a TSUNAMI🌀… https://t.co/qRhiOBzUpE' },
    3 : { "user_screen_name" : 'OpenSFHistory', "created_at" : '2022-04-14 13:00:01', "text" : 'View of Sweeny Observatory ruins, Golden Gate Park, 1906. Destroyed by the 1906 Earthquake and Fire, the observator… https://t.co/z89xIzQRW1' },
    4 : { "user_screen_name" : 'ukiyoeweb',     "created_at" : '2022-04-14 13:10:05', "text" : 'Artist Unknown, Japanese\nSketch of the Great Earthquake and Fire (Dai jishin kaji ryakuzu)\n\nUkiyoe web Online ukiy… https://t.co/jisKuOs6bm' },
    5 : { "user_screen_name" : 'Budgiekiller',  "created_at" : '2022-04-14 13:03:52', "text" : 'RT @abline11: San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    6 : { "user_screen_name" : 'Cathy69118239', "created_at" : '2022-04-14 12:57:43', "text" : 'San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    7 : { "user_screen_name" : 'prasadraghava', "created_at" : '2022-04-14 15:41:18', "text" : 'KGF2 is not a fire or water.\nKGF2 is a VOLCANO🌋\nKGF2 is an EARTHQUAKE🌎\nKGF2 is a THUNDERSTORM⛈️\nKGF2 is a TSUNAMI🌀… https://t.co/qRhiOBzUpE' },
    8 : { "user_screen_name" : 'OpenSFHistory', "created_at" : '2022-04-14 13:00:01', "text" : 'View of Sweeny Observatory ruins, Golden Gate Park, 1906. Destroyed by the 1906 Earthquake and Fire, the observator… https://t.co/z89xIzQRW1' },
    9 : { "user_screen_name" : 'ukiyoeweb',     "created_at" : '2022-04-14 13:10:05', "text" : 'Artist Unknown, Japanese\nSketch of the Great Earthquake and Fire (Dai jishin kaji ryakuzu)\n\nUkiyoe web Online ukiy… https://t.co/jisKuOs6bm' },
    10 : { "user_screen_name" : 'Budgiekiller', "created_at" : '2022-04-14 13:03:52', "text" : 'RT @abline11: San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    11 : { "user_screen_name" : 'Cathy69118239', "created_at" : '2022-04-14 12:57:43', "text" : 'San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    12 : { "user_screen_name" : 'prasadraghava', "created_at" : '2022-04-14 15:41:18', "text" : 'KGF2 is not a fire or water.\nKGF2 is a VOLCANO🌋\nKGF2 is an EARTHQUAKE🌎\nKGF2 is a THUNDERSTORM⛈️\nKGF2 is a TSUNAMI🌀… https://t.co/qRhiOBzUpE' },
    13 : { "user_screen_name" : 'OpenSFHistory', "created_at" : '2022-04-14 13:00:01', "text" : 'View of Sweeny Observatory ruins, Golden Gate Park, 1906. Destroyed by the 1906 Earthquake and Fire, the observator… https://t.co/z89xIzQRW1' },
    14 : { "user_screen_name" : 'ukiyoeweb',     "created_at" : '2022-04-14 13:10:05', "text" : 'Artist Unknown, Japanese\nSketch of the Great Earthquake and Fire (Dai jishin kaji ryakuzu)\n\nUkiyoe web Online ukiy… https://t.co/jisKuOs6bm' },
    15 : { "user_screen_name" : 'Budgiekiller',  "created_at" : '2022-04-14 13:03:52', "text" : 'RT @abline11: San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    16 : { "user_screen_name" : 'Cathy69118239', "created_at" : '2022-04-14 12:57:43', "text" : 'San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    17 : { "user_screen_name" : 'prasadraghava', "created_at" : '2022-04-14 15:41:18', "text" : 'KGF2 is not a fire or water.\nKGF2 is a VOLCANO🌋\nKGF2 is an EARTHQUAKE🌎\nKGF2 is a THUNDERSTORM⛈️\nKGF2 is a TSUNAMI🌀… https://t.co/qRhiOBzUpE' },
    18 : { "user_screen_name" : 'OpenSFHistory', "created_at" : '2022-04-14 13:00:01', "text" : 'View of Sweeny Observatory ruins, Golden Gate Park, 1906. Destroyed by the 1906 Earthquake and Fire, the observator… https://t.co/z89xIzQRW1' },
    19 : { "user_screen_name" : 'ukiyoeweb',     "created_at" : '2022-04-14 13:10:05', "text" : 'Artist Unknown, Japanese\nSketch of the Great Earthquake and Fire (Dai jishin kaji ryakuzu)\n\nUkiyoe web Online ukiy… https://t.co/jisKuOs6bm' },
    20 : { "user_screen_name" : 'Budgiekiller',  "created_at" : '2022-04-14 13:03:52', "text" : 'RT @abline11: San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    21 : { "user_screen_name" : 'Cathy69118239', "created_at" : '2022-04-14 12:57:43', "text" : 'San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
    22 : { "user_screen_name" : 'prasadraghava', "created_at" : '2022-04-14 15:41:18', "text" : 'KGF2 is not a fire or water.\nKGF2 is a VOLCANO🌋\nKGF2 is an EARTHQUAKE🌎\nKGF2 is a THUNDERSTORM⛈️\nKGF2 is a TSUNAMI🌀… https://t.co/qRhiOBzUpE' },
    23 : { "user_screen_name" : 'OpenSFHistory', "created_at" : '2022-04-14 13:00:01', "text" : 'View of Sweeny Observatory ruins, Golden Gate Park, 1906. Destroyed by the 1906 Earthquake and Fire, the observator… https://t.co/z89xIzQRW1' },
    24 : { "user_screen_name" : 'ukiyoeweb',     "created_at" : '2022-04-14 13:10:05', "text" : 'Artist Unknown, Japanese\nSketch of the Great Earthquake and Fire (Dai jishin kaji ryakuzu)\n\nUkiyoe web Online ukiy… https://t.co/jisKuOs6bm' },
    25 : { "user_screen_name" : 'Budgiekiller',  "created_at" : '2022-04-14 13:03:52', "text" : 'RT @abline11: San Francisco 1906 on 14th April just 4 days before the earthquake and fire. On a cable car, the camera records a trip down M…' },
}