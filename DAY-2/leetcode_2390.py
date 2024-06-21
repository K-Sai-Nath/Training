s="leet**cod*e"
st=[]
for i in range(len(s)):
  if s[i]!="*":
    st.append(s[i])
  else:
    st.pop()
res="".join(st)
print(res)
  