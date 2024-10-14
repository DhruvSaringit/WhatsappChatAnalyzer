# import re
# import pandas as pd
# def preprocess(data):
#     pattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{1,2}\s(?:am|pm)\s-\s'
#     messages = re.split(pattern, data)[1:]
#     dates = re.findall(pattern, data)
#     df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
#
#     df.rename(columns={'message_date': 'date'}, inplace=True)
#     users = []
#     messages = []
#     for message in df['user_message']:
#         entry = re.split('([\w\W]+?):\s', message)
#         if entry[1:]:  # user name
#             users.append(entry[1])
#             messages.append(" ".join(entry[2:]))
#         else:
#             users.append('group_notification')
#             messages.append(entry[0])
#     df['date'] = pd.to_datetime(df['date'])
#     df['user'] = users
#     df['message'] = messages
#     df.drop(columns=['user_message'], inplace=True)
#     df['only_date'] = df['date'].dt.date
#     df['year'] = df['date'].dt.year
#     df['month_num'] = df['date'].dt.month
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day
#     df['day_name'] = df['date'].dt.day_name()
#     df['hour'] = df['date'].dt.hour
#     df['minute'] = df['date'].dt.minute
#     return df
#
#
#
#












    # messages = re.split(pattern, data)[1:]
    # dates = re.findall(pattern, data)
    #
    # df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # # convert message_date type
    # df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
    #
    # df.rename(columns={'message_date': 'date'}, inplace=True)
    #
    # users = []
    # messages = []
    # for message in df['user_message']:
    #     entry = re.split('([\w\W]+?):\s', message)
    #     if entry[1:]:  # user name
    #         users.append(entry[1])
    #         messages.append(" ".join(entry[2:]))
    #     else:
    #         users.append('group_notification')
    #         messages.append(entry[0])
    #
    # df['user'] = users
    # df['message'] = messages
    # df.drop(columns=['user_message'], inplace=True)
    #
    # df['only_date'] = df['date'].dt.date
    # df['year'] = df['date'].dt.year
    # df['month_num'] = df['date'].dt.month
    # df['month'] = df['date'].dt.month_name()
    # df['day'] = df['date'].dt.day
    # df['day_name'] = df['date'].dt.day_name()
    # df['hour'] = df['date'].dt.hour
    # df['minute'] = df['date'].dt.minute
    # return df
import re
import pandas as pd


def preprocess(data):
    # Regex pattern to identify date and time format in the chat data
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{1,2}\s(?:am|pm)\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)


    print("Date strings:", dates[:10])

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})


    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ', errors='coerce')

    if df['message_date'].isna().any():
        print("Parsing errors in message_date column. Some dates could not be converted.")
        print(df[df['message_date'].isna()])

    df.rename(columns={'message_date': 'date'}, inplace=True)


    users = []
    msgs = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            msgs.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            msgs.append(entry[0])

    df['user'] = users
    df['message'] = msgs
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df


