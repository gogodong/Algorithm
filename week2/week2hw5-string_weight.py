input = "1101"
len = 4

dp = [1]
ans = 1
for i in range(1, len):
    if input[i] == input[i - 1]:
        dp.append(dp[i - 1] + 1)
    elif input[i] != input[i - 1]:
        dp.append(dp[i - 1] + i + 1)
    ans = ans + dp[i]

print(ans)

# 本题关键：如果在尾部位置i再添加一个字符，与之i-1不相同，那么此时以原字符串i-1结尾的所有子串的权值增加1
# 例如11结尾加一个0，
# 此时11以第二个1结尾的子串1,11,其权值为1,1
# 加上0后，10,110其权值变为2,2，每一个都增加1
