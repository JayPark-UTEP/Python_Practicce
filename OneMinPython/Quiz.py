#Make a program that generates passwords

''''EX) Rules
1: Skip http// => naver.com
2: Skip the first period(.) => naver
3: password = First three chars + number of the chars + number of 'e' in the word
+ "1" '''

#My answer
website_name = 'http://naver.com'
tem_password = ''

website_name = website_name[7:-4]

tem_password = website_name[:3] + str(len(website_name)) + str(website_name.count('e')) + '!'

print(tem_password)

#Answer
url = "http://naver.com"
my_str = url.replace("http://", "")

my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print("The password for {0} is {1}".format(url, password))