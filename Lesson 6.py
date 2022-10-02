import requests
response = requests.get ('https://api.vk.com/method/friends.getOnline?v=5.131&access_token=vk1.a.4tj585eBc-qqDbzdw50-MTtf6iaLW-bG1W36bsnl0q0brm7uBxjOJYa0_Bqg8MY2nx079BS0sXHSop_O8Q2GII9Y_cW44gqvDSVdWFgA0Q2V2BvYxU1Duo4nY-zVbKcNbG_7ElHqvt_1dzwoRpjG8xTJeAH7xsQXQOBNDxC0CVVV22ZCcWmiiuNqxsQXex4n')
print (response.json())
userinf = requests.get ('https://api.vk.com/method/users.get?user_id=7185447&v=5.131&access_token=vk1.a.4tj585eBc-qqDbzdw50-MTtf6iaLW-bG1W36bsnl0q0brm7uBxjOJYa0_Bqg8MY2nx079BS0sXHSop_O8Q2GII9Y_cW44gqvDSVdWFgA0Q2V2BvYxU1Duo4nY-zVbKcNbG_7ElHqvt_1dzwoRpjG8xTJeAH7xsQXQOBNDxC0CVVV22ZCcWmiiuNqxsQXex4n')
print (userinf.json())
myinfo = requests.get ('https://api.vk.com/method/account.getProfileInfo?first_name?last_name&v=5.131&&access_token=vk1.a.4tj585eBc-qqDbzdw50-MTtf6iaLW-bG1W36bsnl0q0brm7uBxjOJYa0_Bqg8MY2nx079BS0sXHSop_O8Q2GII9Y_cW44gqvDSVdWFgA0Q2V2BvYxU1Duo4nY-zVbKcNbG_7ElHqvt_1dzwoRpjG8xTJeAH7xsQXQOBNDxC0CVVV22ZCcWmiiuNqxsQXex4n')
print (myinfo.json())